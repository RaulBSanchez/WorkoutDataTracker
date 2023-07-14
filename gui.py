from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from mysql.connector import Error


root = Tk()
root.title("Work Out Data Tracker")
root.geometry("400x200")






def get_connection():
	connection = mysql.connector.connect (host='localhost',
                                         database='WorkOutData',
                                         user='root',
                                         password='')

	return connection 

def close_connection(connection):
	if connection:
		connection.close()




def excecute_query(action):
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
			entry.delete(0, END)
			entry.insert(0, entry_speed)
			#print(records)
			return True

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
			entry.delete(0, END)
			entry.insert(0, entry_calories)
			#print(records)
			return True

		except(Exception, mysql.connector.Error) as error:
			print("error", error)

	elif command == "Sum of Distance":
		try: 
			connection = get_connection()
			cursor = connection.cursor()
			select_query = """SELECT SUM(Distance) FROM WorkOutData.Running;"""
			cursor.execute(select_query)
			records = cursor.fetchone()
			#print("This is datatype of records", type(records))
			distance = str(records[0])
			entry_distance = distance + " Miles"
			entry.delete(0, END)
			entry.insert(0, entry_distance)
			#print(records)
			return True

		except(Exception, mysql.connector.Error) as error:
			print("error", error)

	else:
		print("sorry")






def query(value):
	#entry.delete(0, END)
	#entry.insert(0, value)
	#test_connection()

	action = value
	#print(type(action))

	if action == "Calories":
		excecute_query("Calories")
	elif action == "Sum of Distance":
		excecute_query("Sum of Distance")
	elif action == "Pace":
		excecute_query("Pace")




#entries
entry = Entry(root, width = 35)
entry.insert(0, "Default Text")
entry.grid(row = 0, column = 3)

entry_bike = Entry(root, width = 35)
entry_bike.insert(0, "Default Text")
entry_bike.grid(row = 1, column = 3)


#workout label
run_workout = Label(root, text = "Running", anchor= "w")
run_workout.grid(row =0, column = 0)

#bike
bike_workout = Label(root, text = "Biking   ", anchor= "w")
bike_workout.grid(row=1, column = 0)


#selection
option = ["Calories", "Sum of Distance", "Pace"]

dataPoint_run = StringVar()
dataPoint_run.set(option[0])

dataPoint_bike = StringVar()
dataPoint_bike.set(option[0])

#create drop down menu
drop_run = OptionMenu(root, dataPoint_run, *option)
drop_run.grid(row = 0, column = 1)

drop_bike = OptionMenu(root, dataPoint_bike, *option)
drop_bike.grid(row = 1, column = 1)

run_query = Button(root, text = "Run Query", command = lambda: query(dataPoint_run.get()))
run_query.grid(row = 0, column = 2)

run_query_bike = Button(root, text = "Run Query", command = lambda: query(dataPoint_run.get()))
run_query_bike.grid(row = 1, column = 2)





root.mainloop()


