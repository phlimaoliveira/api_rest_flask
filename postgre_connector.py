import psycopg2

def connect():
    connector = psycopg2.connect(host="localhost",
                                 user="postgres",
                                 password="postgres",
                                 dbname="postgres")

    return connector

def query(sql):
    cursor = connect().cursor()
    cursor.execute(sql)
    return cursor.fetchall()

def execute(sql):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()