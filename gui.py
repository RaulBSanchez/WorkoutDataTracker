from tkinter import *
import mysql.connector
from mysql.connector import Error
import biking as Bike
import running as Run

root = Tk()
root.title("Work Out Data Tracker")
root.geometry("400x200")



def run(value):

	action = value
	
	if action == "Calories":
		cals = Run.runsql_query("Calories")
		entry.delete(0, END)
		entry.insert(0, cals)
	elif action == "Sum of Distance":
		totalMiles = Run.runsql_query("Sum of Distance")
		entry.delete(0, END)
		entry.insert(0, totalMiles)
	elif action == "Pace":
		speed = Run.runsql_query("Pace")
		entry.delete(0, END)
		entry.insert(0, speed)

def bike(value):

	action = value
	
	if action == "Calories":
		cals = Bike.bikesql_query("Calories")
		entry_bike.delete(0, END)
		entry_bike.insert(0, cals)
	elif action == "Sum of Distance":
		totalMiles = Bike.bikesql_query("Sum of Distance")
		entry_bike.delete(0, END)
		entry_bike.insert(0, totalMiles)

	elif action == "Pace":
		#Bike.bikesql_query("Pace")
		speed = Bike.bikesql_query("Pace")
		entry_bike.delete(0, END)
		entry_bike.insert(0, speed)


#entries
entry = Entry(root, width = 35)
entry.insert(0, "Running Data")
entry.grid(row = 0, column = 3)

entry_bike = Entry(root, width = 35)
entry_bike.insert(0, "Biking Data")
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

run_query = Button(root, text = "Run Query", command = lambda: run(dataPoint_run.get()))
run_query.grid(row = 0, column = 2)

run_query_bike = Button(root, text = "Run Query", command = lambda: bike(dataPoint_bike.get()))
run_query_bike.grid(row = 1, column = 2)





root.mainloop()


