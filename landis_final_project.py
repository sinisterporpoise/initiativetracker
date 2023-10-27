#!/usr/bin/env python3
#===========================================================================================
# Lara Landis
# CS 499
# Dr. Hy
# 10/03/2023
#
#
# This is the final assignment for the Senior Seminar CS 499 class. While a more complex
# program might have been more interesting, I was not sure how many assignments there were
# in the class and if I would have 60 points by then or not, and even if I did, it is bad form
# for me to slack off just becasue I'm' a senior who has what I need to pass if I do not want
# the high school students I interact with to assume it is okay for them to do the same..
# 
# This is an initiative program that will use Tkinter to provide a graphical user interface.
# The user will put in  the names of the players, the monster type and number, the initiative
# tracking stat for each, any modifiers that can affect the outcome of the roll, etc.
#============================================================================================
import tkinter as tk
import tkinter.messagebox
import random as rnd
import math
import sys 

#------------------------------------------------------------------------------------------------
#
# This class defines an introductory window that just lets the user know they have started the
# program. it hasa  title, a label, and a button, whe nthe button is clicked, it hides the window
#
#---------------------------------------------------------------------------------------------------
class Intro_Window:

    def __init__ (self, program):
        self.program = program
        self.intro = tk.Tk()
        self.intro.title ('Sinister Software Solutions')
        self.Label1 = tk.Label(text = "Initiative Tracker Program")
        self.button1 = tk.Button(text="OK", width=2, height=1, fg='white', bg='royalblue', command=self.hide)

        self.Label1.pack()
        self.button1.pack()

        self.intro.mainloop()

    def hide(self):
        self.Label1.pack_forget()
        self.button1.pack_forget()
        self.intro.withdraw()
        

#------------------------------------------------------------------------------------------------------
#
# This class defines the main program window where the user will do most of his or her work. It will
# get the players, the  type and number of dice to roll, and different types of monsters. It will
# then generate random initiatives and print the players out.  
#``
#----------------------------------------------------------------------------------------------------
class Program_Window:
    
    def __init__(self):
        self.ProgWindow = tk.Toplevel()
        self.top_frame = tk.Frame(self.ProgWindow)
        self.bottom_frame = tk.Frame(self.ProgWindow)
        self.ProgWindow.title('System Agnostic Initiative Tracker')

        # Create labels and entry widgets for player/monster 1
        self.iniLabel1 = tk.Label(self.top_frame, text="Player Name/Monster Type")
        self.iniText1 = tk.Entry(self.top_frame, text="", width=24)
        self.iniModLabel1 = tk.Label(self.top_frame, text="Modifier")
        self.iniModText1 = tk.Entry(self.top_frame, text="", width=3)

        # ... Repeat the same pattern for player/monster 2, 3, 4, and 5
        self.iniText2 = tk.Entry(self.top_frame, text="", width=24)
        self.iniModText2 = tk.Entry(self.top_frame, text="", width=3)
        self.iniText3 = tk.Entry(self.top_frame, text="", width=24)
        self.iniModText3 = tk.Entry(self.top_frame, text="", width=3)
        self.iniText4 = tk.Entry(self.top_frame, text="", width=24)
        self.iniModText4 = tk.Entry(self.top_frame, text="", width=3)
        self.iniText5 = tk.Entry(self.top_frame, text="", width=24)
        self.iniModText5 = tk.Entry(self.top_frame, text="", width=3)

        # Create labels for dice options
        self.diceNumber = tk.Label(self.bottom_frame, text="Number of dice")
        self.diceNumberEntry = tk.Entry(self.bottom_frame, text ="", width=3)
        self.diceSides = tk.Label(self.bottom_frame, text="No. of Sides")
        self.diceSidesEntry = tk.Entry(self.bottom_frame, text = "", width=3)
        # Create buttons
        self.AddButton = tk.Button(self.bottom_frame, text="Add Player/Monster", width=20, height=2, fg='white', bg='royalblue', command=self.add_player)
        self.CalcButton = tk.Button(self.bottom_frame, text="Calculate", fg='white', bg='royalblue', width=20, height=2, command=self.calculate)

        # Pack widgets
        self.iniLabel1.grid(row=0, column=0)
        self.iniText1.grid(row=1, column=0)
        self.iniModLabel1.grid(row=0, column=1)
        self.iniModText1.grid(row=1, column=1)
        self.iniText2.grid (row=2, column=0)
        self.iniModText2.grid(row=2, column=1)
        self.iniText3.grid(row=3, column = 0)
        self.iniModText3.grid(row = 3, column = 1)
        self.iniText4.grid(row=4, column=0)
        self.iniModText4.grid(row=4, column=1)
        self.iniText5.grid(row=5, column=0)
        self.iniModText5.grid(row=5, column=1)


        # ... Repeat the same pattern for player/monster 2, 3, 4, and 5

        self.diceNumber.grid(row=0, column=0)
        self.diceSides.grid(row=0, column=1)
        self.diceNumberEntry.grid(row=1, column=0)
        self.diceSidesEntry.grid(row=1, column=1)
        self.AddButton.grid(row=2, column=0)
        self.CalcButton.grid(row=2, column=1)

        self.top_frame.pack()
        self.bottom_frame.pack()


    def show_program_window(self):
        self.ProgWindow.deiconify()

    #-----------------------------------------------------------------------------------------------
    # 
    # If I get around to adding this code, it will allow the user to add additional players or
    # monsters to help the GM keep track of who goes when.
    #
    #-----------------------------------------------------------------------------------------------
    def add_player(self):
        pass


    #--------------------------------------------------------------------------------------------
    #
    # This will calculate the messages and then it will display the initiatives in order. It will
    # get the necessary stats, and then it will roll the random dice, adding the initiative
    # modifier. Getting values from Tkinter interfaces can be a little tricky, but it is not
    # impossible.
    #
    #---------------------------------------------------------------------------------------------
    def calculate(self):
        pass
       
#================================================================================================
#
# THIS IS  THE MAIN FUNCTION. THIS IS THE MAIN FUNCTION. THIS IS THE MAIN FUNCTION. THIS IS THE
#
#==================================================================================================
def main ():
    
    programWindow = Program_Window()
    Intro = Intro_Window(programWindow)
    programWindow.ProgWindow.mainloop()

if __name__ == "__main__":
    main()