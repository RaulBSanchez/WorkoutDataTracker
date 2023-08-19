from tkinter import *
import mysql.connector
from mysql.connector import Error
import datetime

root = Tk()
root.title("Work Out Data Tracker")
root.geometry("450x300")


#connections to database
def get_connection():
	connection = mysql.connector.connect (host='localhost',
                                         database='WorkOutData',
                                         user='root',
                                         password='Catfish1030!')

	return connection 

def close_connection(connection):
	if connection:
		connection.close()
'''
def testGettingValues():
	
	text = workoutType.get()
	
	date = b_date.get()
	#format = '%Y/%m/%d'
	#print(type(date))
	sqlDate = datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%Y-%m-%d")
	

	cals = b_calories.get()
	pace = b_pace.get()
	dis = b_distance.get()
	heartRate = b_heartRate.get()
	print("getting values")
	print( sqlDate, cals, pace, dis, heartRate)
'''

#create submit function
def submit():
	date = b_date.get()
	#format = '%Y/%m/%d'
	#print(type(date))
	sqlDate = datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%Y-%m-%d")
	

	cals = b_calories.get()
	pace = b_pace.get()
	dis = b_distance.get()
	heartRate = b_heartRate.get()

	command = workoutType.get()
	#print('this is the command ', command)
	#try query
	if command == "Biking":
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

	elif command == "Running":
		try:
			connection = get_connection()
			cursor = connection.cursor()
			query = """INSERT INTO WorkOutData.Running(Date, Calories, Pace, Distance, HeartRate)
			Values(%s, %s, %s, %s, %s)"""
			data = (sqlDate, cals, pace, dis, heartRate)
			cursor.execute(query, data)
			connection.commit()
			
			print(cursor.rowcount, "was inserted.")
		
		except(Exception, mysql.connector.Error) as error:
			print("error", error)
		
	else:
		print("didnt work")



	b_date.delete(0, END)
	b_calories.delete(0, END)
	b_pace.delete(0, END)
	b_distance.delete(0, END)
	b_heartRate.delete(0, END)




# text boxes
b_date = Entry(root, width = 30)
b_date.grid(row = 0, column = 1, padx = 20)

b_calories = Entry(root, width = 30)
b_calories.grid(row = 1, column = 1)

b_pace = Entry(root, width = 30)
b_pace.grid(row = 2, column = 1)

b_distance = Entry(root, width = 30)
b_distance.grid(row = 3, column = 1)

b_heartRate = Entry(root, width = 30)
b_heartRate.grid(row = 4, column = 1)

# text box labels
b_date_label = Label(root, text= "Date", anchor = "e")
b_date_label.grid(row = 0, column = 0)

b_calories_label = Label(root, text = "Calories", anchor = "e")
b_calories_label.grid(row = 1, column = 0)

b_pace_label = Label(root, text ="Pace", anchor = "e")
b_pace_label.grid(row = 2, column = 0)

b_distance_label = Label(root, text = "Distance", anchor = "e")
b_distance_label.grid(row = 3, column = 0)

b_hearRate_label = Label(root, text = "Heart Rate", anchor = "e")
b_hearRate_label.grid(row = 4, column = 0)

# create submit button

submit_button = Button(root, text = "Add Workout", command =submit)
submit_button.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx=100)


#dropdown button
option = ['Biking', 'Running']
workoutType = StringVar()
workoutType.set(option[0])

dropdown = OptionMenu(root, workoutType, *option)
dropdown.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx=100)


root.mainloop()