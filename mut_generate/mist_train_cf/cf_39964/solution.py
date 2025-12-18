"""
QUESTION:
Design a database schema that includes the necessary tables and columns to store information about lost cards and user activity tracking. Define the relationships between the tables to ensure data integrity and efficient querying. The schema should include two tables: lost_cards and users. The lost_cards table should have columns to store information about lost cards, including deposit details and any observations related to the loss, as well as the users who created and modified the records. The users table should track user activity and include basic user information. The schema should establish a relationship between the lost cards and the users who created or modified the records.
"""

def entrance(boleta_deposito, cuenta, banco, fecha_deposito, monto, ci_visitante, observacion_perdida, creado_por, modificado_por):
    lost_cards = {
        "id": None,
        "boleta_deposito": boleta_deposito,
        "cuenta": cuenta,
        "banco": banco,
        "fecha_deposito": fecha_deposito,
        "monto": monto,
        "ci_visitante": ci_visitante,
        "observacion_perdida": observacion_perdida,
        "creado_por": creado_por,
        "modificado_por": modificado_por
    }

    users = {
        "id": creado_por,
        "name": "",
        "email": "",
        "created_at": "",
        "updated_at": ""
    }
    return lost_cards, users