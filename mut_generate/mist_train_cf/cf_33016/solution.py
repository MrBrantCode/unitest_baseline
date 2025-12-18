"""
QUESTION:
Implement a Python function `add_image_with_faces(conn, image_id, image_path, detected_faces)` that adds a new image and its associated detected faces to a SQLite database. The function should perform two tasks:
- Insert a new record into the `images` table with the provided `image_id` and `image_path`.
- Insert records into the `faces` table for each detected face in the `detected_faces` list, including `image_id`, `face_id`, `top_left_x`, `top_left_y`, `width`, and `height`.

Assumptions:
- `conn` is a valid SQLite database connection.
- `image_id` is a unique identifier for the image.
- `image_path` is a string representing the file path of the image.
- `detected_faces` is a list of dictionaries, each containing `face_id`, `top_left_x`, `top_left_y`, `width`, and `height`.

Return `True` if the image and faces are successfully added to the database, and `False` if any error occurs during the insertion process.
"""

import sqlite3

def add_image_with_faces(conn, image_id, image_path, detected_faces):
    try:
        c = conn.cursor()

        # Insert image record into images table
        c.execute("INSERT INTO images (image_id, image_path) VALUES (?, ?)", (image_id, image_path))

        # Insert detected faces into faces table
        for face in detected_faces:
            c.execute("INSERT INTO faces (image_id, face_id, top_left_x, top_left_y, width, height) VALUES (?, ?, ?, ?, ?, ?)",
                      (image_id, face['face_id'], face['top_left_x'], face['top_left_y'], face['width'], face['height']))

        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error adding image with faces: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()