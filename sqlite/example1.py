import sqlite3
import time
import datetime
import random

#definir conexion
conn = sqlite3.connect('ejemplo.db')

#cursor
curs = conn.cursor()

def create_table():
    #cursor hace todas las ejecuciones de queries
    curs.execute('CREATE TABLE IF NOT EXISTS tabla1(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

#input data a la bd
def entrada_datos():
    curs.execute("INSERT INTO tabla1 VALUES(1451255552, '2016-01-02', 'Python', 8)")
    #grabar modificacion de bd
    conn.commit()
    curs.close()
    conn.close()

def entrada_dinamica_datos():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d  %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    curs.execute("INSERT INTO tabla1 (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
                 (unix, date, keyword, value))
    conn.commit()

#para leer de la bd SELECT
def leer_de_bd():
    curs.execute('SELECT * FROM tabla1')

    #seleccionar todo
    #data = curs.fetchall()
    #data = curs.fetchone()
    #print(data)

    #iterator
    for fila in curs.fetchall():
        print(fila)
    

#create_table()
#entrada_datos()
    
#for i in range(10):
#    entrada_dinamica_datos()
#    time.sleep(5)


#correr leer data from db
leer_de_bd()

curs.close()
conn.close()


























