import mysql.connector
import os
from flask import g

def getDB():
    if 'database' not in g:
        g.database = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
    return g.database

def closeDB():
    database = g.pop('database', None)
    if database is not None:
        database.close()