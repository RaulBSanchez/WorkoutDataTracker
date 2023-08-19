import mysql.connector
from mysql.connector import Error
import datetime

#this will all the functions for biking so the GUI's just have widgets
def hello():
	print("hello")

def submit(sqlDate, cals, pace, dis, heartRate):

	#print(sqlDate, cals, pace, dis, heartRate)

	try:
		connection = get_connection()
		cursor = connection.cursor()
		query = """INSERT INTO WorkOutData.Biking(Date, Calories, Pace, Distance, HeartRate)
		Values(%s, %s, %s, %s, %s)"""
		data = (sqlDate, cals, pace, dis, heartRate)
		cursor.execute(query, data)
		connection.commit()
			
		print(cursor.rowcount, "was inserted.")

	except(Exception, mysql.connector.Error) as error:
		print("error", error)
def get_connection():
	connection = mysql.connector.connect (host='localhost',
                                         database='WorkOutData',
                                         user='root',
                                         password='')

	return connection 

def close_connection(connection):
	if connection:
		connection.close()