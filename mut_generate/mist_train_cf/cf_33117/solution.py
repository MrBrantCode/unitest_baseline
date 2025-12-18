"""
QUESTION:
Implement a function `check_reservation(codice: str, start: str, username: str) -> bool` that checks if a reservation exists in the database for a given course code, start time, and username. The function should query the `mrbs_entry`, `mrbs_room`, and `Reservations` tables to check for existing reservations and return a boolean value indicating whether the reservation exists or not.
"""

def check_reservation(codice: str, start: str, username: str) -> bool:
    con = sqlite3.connect('reservation_database.db')  
    cur = con.cursor()

    query = "SELECT * FROM `mrbs_entry` E JOIN `mrbs_room` R ON E.room_id = R.id WHERE E.id_corso LIKE ? AND E.start_time >= ?"
    cur.execute(query, ('%' + codice + '%', start))

    for row in cur.fetchall():
        reservation_query = "SELECT * FROM Reservations WHERE id_lezione = ? AND username = ?"
        cur.execute(reservation_query, (row[0], username))
        reservation = cur.fetchone()
        if reservation:
            return True  

    return False  