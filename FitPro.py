######################################################################
# Author: Joyce Nimely
# Username: Nimely_J
#
# FinalProject: FitPro App
#
# Purpose: A python based fitness tracking application that allows user to log workouts,
# set fitness goal, and track progress
#This project uses the Tkinter module to build a user-friendly graphical
# interface (GUI).

# A GUI widget is a graphical component such as a button, text label as shown below.
# GUI widgets also exist to make drop-down menus and scroll bars, display images, etc...
# Tkinter gives you the ability to create GUI Windows containing widgets.
# This program is a simple exploration.
#######################################################################
# Acknowledgements:
####################################################################################

import tkinter as tk
from tkinter import messagebox
import turtle

class User:
    """A class for the user information for FitPro.
    """
    def __init__(self, name, age, height):
        self.name= name
        self.age= age
        self.height= height
        self.workouts = []

    def log_workout(self, workout):
        """
        A function for the user's workouts

        :arg: a workout object to be added to the list
        """
        self.workouts.append(workout)

    def __str__(self):
        """"
        :returns: string representing the user age, name, height
        """
        return f"User(name={self.name}, age= {self.age}, height= {self.height})"

class Workout:
    """
    A class for the workout session
    """
    def __init__(self, workout_type, duration, calories):
        """initializes a workout instance with workout_type, duration, calories
        """
        self.workout_type = workout_type
        self.duration = duration
        self.calories= calories

class FitPro:
    """" A class for the FitPro application
     """
    def __init__(self, root):
        self.root= root
        self.root.title("FitPro Workout Tracker")

        self.user=None

        self.create_user_frame()
        self.create_workout_frame()

    def create_user_frame(self):
        """"
        creates the user information frame """

        user_frame = tk.Frame(self.root)
        user_frame.pack(pady = 10)

        tk.Label(user_frame, text = "Name:").grid(row =0, column = 0, padx= 5, pady= 5)
        self.name_entry = tk.Entry(user_frame)
        self.name_entry.grid(row= 0, column = 1, padx=5, pady= 5)

        tk.Label(user_frame, text="Age:").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(user_frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(user_frame, text="Height (cm):").grid(row=2, column=0, padx=5, pady=5)
        self.height_entry = tk.Entry(user_frame)
        self.height_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(user_frame, text = "Save User", command=self.save_user).grid(row= 3, columnspan= 2, pady=10)

    def save_user(self):
        """"
        This function saves the user information """

        try:
            name = self.name_entry.get().strip()
            age = int(self.age_entry.get())
            height = float(self.height_entry.get())

            if not name:
                raise ValueError("Invalid Input ", "Please add a name.")

            self.user = User(name, age, height) #creates an instance of the user class using name, age and height as input
            messagebox.showinfo("Success",f"User name saved: {self.user}") #displays a  message when the user enters the right info
        except ValueError as e:
            messagebox.showerror("Error",f"Invalid input: {e}") #displays an error message when the user enters the wrong info

        #This clears the input fields
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)

    def create_workout_frame(self):
        """
        creates the workout logging and progress fame
        """
        workout_frame = tk.Frame(self.root)
        workout_frame.pack(pady=10)

        tk.Label(workout_frame, text = "Workout Type:").grid(row = 0, column = 0, padx= 5, pady = 5 )
        self.workout_type_entry = tk.Entry(workout_frame)
        self.workout_type_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(workout_frame, text="Duration (minutes):").grid(row=1, column=0, padx=5, pady=5)
        self.duration_entry = tk.Entry(workout_frame)
        self.duration_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(workout_frame, text="Calories Burned:").grid(row=2, column=0, padx=5, pady=5)
        self.calories_entry= tk.Entry(workout_frame)
        self.calories_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(workout_frame, text="Log Workout", command=self.log_workout).grid(row=3, columnspan=2, pady=10)
        tk.Button(self.root, text= "View Progress", command=self.view_progress).pack(pady=5)

    def log_workout(self):
        """"
        Log the workout for the user
        """
        if not self.user:
            messagebox.showwarning("No User","Please save user information first")
            return

        try:
            workout_type = self.workout_type_entry.get().strip()
            duration = int(self.duration_entry.get())
            calories = int(self.calories_entry.get())

            if not workout_type:
                raise ValueError("Please enter the workout type")
            if duration <= 0 or calories <= 0:
                raise ValueError("Enter a positive number")

            #Create and log the workouts
            workout = Workout(workout_type, duration, calories)
            self.user.log_workout(workout)

            #this clears input fields
            self.workout_type_entry.delete(0, tk.END)
            self.duration_entry.delete(0, tk.END)
            self.calories_entry.delete(0, tk.END)

            messagebox.showinfo(" Success", f"workout logged successfully: {workout_type}")
        except ValueError as e:
            messagebox.showerror("Error", "Invalid input: {e}")


    def view_progress(self):
        """This function displays the user's workout progress"""
        if not self.user:
            messagebox. showwarning("Missing User Info", "Please enter the user information first")
            return

        total_workouts = len(self.user.workouts)
        total_duration = sum(w.duration for w in self.user.workouts)
        total_calories = sum (w.calories for w in self.user.workouts)

        progress_message = (
        f"Total Workouts: {total_workouts}\n"
        f"Total Duration: {total_duration} minutes\n"
        f"Total Calories Burned:{total_calories} kcal")

        messagebox.showinfo("Workout Progress", progress_message)


if __name__ == "__main__":
    root = tk.Tk()
    app = FitPro(root)
    root.mainloop()








