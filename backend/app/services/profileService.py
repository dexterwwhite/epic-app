from . import getDB, closeDB

def getAllUsers():
    conn = getDB()
    cursor = conn.cursor(dictionary=True)  # dictionary=True returns results as dictionaries
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()  # Fetch all the rows
    cursor.close()  # Always close the cursor when done
    return users