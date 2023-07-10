from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from mysql.connector import Error


root = Tk()
root.title("Work Out Data Tracker")
root.geometry("200x200")




"""
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='WorkOutData',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

"""

def get_connection():
	connection = mysql.connector.connect (host='localhost',
                                         database='WorkOutData',
                                         user='root',
                                         password='')

	return connection 

def close_connection(connection):
	if connection:
		connection.close()

def test_connection():
	try:
		connection = get_connection()
		cursor = connection.cursor()
		cursor.execute("SELECT version();")
		db_version = cursor.fetchone()
		print("SQL version ", db_version)
		close_connection(connection)
	except(Exception, mysql.connector.Error) as error:
		print("Error", error)


def excecute_query(action):
	global records
	command = action
	if command == "Average":
		try: 
			connection = get_connection()
			cursor = connection.cursor()
			select_query = """SELECT AVG(Pace) FROM WorkOutData.Running;"""
			cursor.execute(select_query)
			records = cursor.fetchone()
			print(records)
			return records

		except(Exception, mysql.connector.Error) as error:
			print("error", error)

	else:
		print("sorry")




entry = Entry(root, width = 35)
entry.insert(0, "Default Text")
entry.grid(row = 0, column = 3)

def query(value):
	entry.delete(0, END)
	entry.insert(0, value)
	#test_connection()

	action = value
	print(action)

	excecute_query("Average")
	pace = excecute_query("Average")
	print("this is the pace", pace)

	#pace = self.excecute_query()
	entry.insert(0, pace)







#workout label
run_workout = Label(root, text = "Running")
run_workout.grid(row =0, column = 0)


#selection
option = ["Average", "Sum of Distance", "Pace"]

dataPoint = StringVar()
dataPoint.set(option[0])

#create drop down menu
drop = OptionMenu(root, dataPoint, *option)
drop.grid(row = 0, column = 1)

run_query = Button(root, text = "Run Query", command = lambda: query(dataPoint.get()))
run_query.grid(row = 0, column = 2)







root.mainloop()