import mysql.connector
from mysql.connector import Error
import datetime

def get_connection():
	connection = mysql.connector.connect (host='localhost',
                                         database='WorkOutData',
                                         user='root',
                                         password='')

	return connection 

def close_connection(connection):
	if connection:
		connection.close()

def submit(sqlDate, cals, pace, dis, heartRate):

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

def runsql_query(action):
	

	#print("testing testing", action)
	#global records
	
	command = action
	if command == "Pace":
		try: 
			connection = get_connection()
			cursor = connection.cursor()
			select_query = """SELECT AVG(Pace) FROM WorkOutData.Running;"""
			cursor.execute(select_query)
			records = cursor.fetchone()
			#print("This is datatype of records", type(records))
			speed = str(records[0])
			entry_speed = speed + " MPH"
			return entry_speed
			

			

		except(Exception, mysql.connector.Error) as error:
			print("error", error)
	
	elif command == "Calories":
		try: 
			connection = get_connection()
			cursor = connection.cursor()
			select_query = """SELECT SUM(Calories) FROM WorkOutData.Running;"""
			cursor.execute(select_query)
			records = cursor.fetchone()
			#print("This is datatype of records", type(records))
			total_calories = str(records[0])
			entry_calories = total_calories + " Calories"
			return entry_calories
			
			

		except(Exception, mysql.connector.Error) as error:
			print("error", error)

	elif command == "Sum of Distance":
		try: 
			connection = get_connection()
			cursor = connection.cursor()
			select_query = """SELECT SUM(Distance) FROM WorkOutData.Running;"""
			cursor.execute(select_query)
			records = cursor.fetchone()
			
			distance = str(records[0])
			entry_distance = distance + " Miles"
			return entry_distance
			
			

		except(Exception, mysql.connector.Error) as error:
			print("error", error)

	else:
		print("sorry")