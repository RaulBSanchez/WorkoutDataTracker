from tkinter import *
import mysql.connector
from mysql.connector import Error
import datetime
import biking as Bike
import running as Run
root = Tk()
root.title("Work Out Data Tracker")
root.geometry("450x300")


#connections to database
def get_connection():
	connection = mysql.connector.connect (host='localhost',
                                         database='WorkOutData',
                                         user='root',
                                         password='')

	return connection 

def close_connection(connection):
	if connection:
		connection.close()


#create submit function
def submit():
	
	# reformat date for sql table
	date = date_entry.get()
	sqlDate = datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%Y-%m-%d")
	

	cals = calories_entry.get()
	pace = pace_entry.get()
	distance = distance_entry.get()
	heartRate = heartRate_entry.get()

	command = workoutType.get()
	'''
	#print('this is the command ', command)
	#try query
	if command == "Biking":
		Bike.submit(sqlDate, cals, pace, distance, heartRate)
	elif command =="Running":
		Run.submit(sqlDate, cals, pace, distance, heartRate)
	'''
	print(sqlDate, cals, pace, distance, heartRate)
	date_entry.delete(0, END)
	calories_entry.delete(0, END)
	pace_entry.delete(0, END)
	distance_entry.delete(0, END)
	heartRate_entry.delete(0, END)




# text boxes
date_entry = Entry(root, width = 30)
date_entry.grid(row = 0, column = 1, padx = 20)

calories_entry = Entry(root, width = 30)
calories_entry.grid(row = 1, column = 1)

pace_entry = Entry(root, width = 30)
pace_entry.grid(row = 2, column = 1)

distance_entry = Entry(root, width = 30)
distance_entry.grid(row = 3, column = 1)

heartRate_entry = Entry(root, width = 30)
heartRate_entry.grid(row = 4, column = 1)

workoutTime_entry = Entry(root, width = 30)
workoutTime_entry.grid(row=5, column=1)

elevation_entry = Entry(root, width=30)
elevation_entry.grid(row=6, column=1)

# text box labels
date_label = Label(root, text= "Date", anchor = "e")
date_label.grid(row = 0, column = 0)

calories_label = Label(root, text = "Calories", anchor = "e")
calories_label.grid(row = 1, column = 0)

pace_label = Label(root, text ="Pace", anchor = "e")
pace_label.grid(row = 2, column = 0)

distance_label = Label(root, text = "Distance", anchor = "e")
distance_label.grid(row = 3, column = 0)

hearRate_label = Label(root, text = "Heart Rate", anchor = "e")
hearRate_label.grid(row = 4, column = 0)

workoutTime_label = Label(root, text = "Length of workout", anchor = "e")
workoutTime_label.grid(row=5, column = 0)

elevation_label = Label(root, text = "Elevation", anchor = "e")
elevation_label.grid(row=6, column = 0)


# create submit button

submit_button = Button(root, text = "Add Workout", command =submit)
submit_button.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx=100)


#dropdown button
option = ['Biking', 'Running']
workoutType = StringVar()
workoutType.set(option[0])

dropdown = OptionMenu(root, workoutType, *option)
dropdown.grid(row = 8, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx=100)


root.mainloop()