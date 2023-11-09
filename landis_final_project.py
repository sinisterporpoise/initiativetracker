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
        self.middle_frame = tk.Frame(self.ProgWindow)
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
    # get the necessary stats, an  then it will roll the random dice, adding the initiative
    # modifier. Getting values from Tkinter interfaces can be a little tricky, but it is not
    # impossible.
    #
    #---------------------------------------------------------------------------------------------
    def calculate(self):
        x = 1
        player_list = []
        

        # This is a kludge because the initial design was poor. I will, if I pursue this project,
        # convet the initial items into a list. For now, this is just being

        #Let's see if they set the variables. If they're not set, print an erro message
        # and return 
        try:
            loopcounter = int(self.diceNumberEntry.get())
            dieType = int(self.diceSidesEntry.get())
        except:
            tkinter.messagebox.showinfo("Warining!", "You must set both the die type and number of sides.")
            return
        
        record = []

        while (x <= 5):
            
            initiative = 0
            if x == 1: 
                try:
                    name = self.iniText1.get()
                    modifier = int(self.iniModText1.get())
                except:
                    return  # This assumes the user didn't put anything after this
    

            if x == 2:
                try:
                    name = self.iniText2.get()
                    modifier = int(self.iniModText2.get())
                except: 
                    break
                
            if x == 3:
                try:
                    name = self.iniText3.get()
                    modifier = int(self.iniModText3.get())
                except: 
                    break

             
            if x == 4:
                try:
                    name = self.iniText4.get()
                    modifier = int(self.iniModText4.get())
                except: 
                    break

            if x == 5:
                try:
                    name = self.iniText5.get()
                    modifier = int(self.iniModText5.get())
                except: 
                    break

            for i in range(0, loopcounter):
                initiative = initiative + rnd.randint(0,dieType) + modifier
                print (initiative)

            record.append([name,initiative])            
            x += 1

        
        # Let's just do bubble sort here, because with the small volume
        # of likely items, bubble sort is actually more efficient than
        # some of the more complex sorting algorithms, even though its
        # O(n**2)
        tuple_to_sort = ""
        tuple2_to_sort = ""
       
        

        for i in range(len(record)):
            swapped = False
            for j in range(len(record) - i - 1):
                int1 = record[j]    
                int2 = record[j+1]
                
                if int1[1] == int2[1]:
                   continue 
                if int1[1] < int2[1]:
                    record[j], record[j+1] = record[j+1], record[j]
                    swapped = True
        
                if not swapped:
                    break
            
        
        print(record)
                  
        # Again, I know this is a kludge as a reuslt of bad initial design.
        try:
            if (record[0]):
                self.resultsLabel1 = tk.Label(text=str(record[0]), padx=5, pady=5)
                self.resultsLabel1.grid(row =6, column=0)
        except:
            pass
    
        try:
            if (record[1]):
                self.resultsLabel2 = tk.Label(text=str(record[1]), padx=5, pady=5)
                self.resultsLabel2.grid(row=7, column=0)
        except:
            pass
    
        try:
            if (record[2]):
                self.resultsLabel3 = tk.Label(text=str(record[2]), padx=5, pady=5)
                self.resultsLabel3.grid(row=8, column=0)
        except:
            pass
        
        try:
            if (record[3]):
                self.resultsLabel4 = tk.Label(text=str(record[3]), padx=5, pady=5)
                self.resultsLabel4.grid(row=9, column=0)
        except:
            pass
    
        try:
            if (record[4]):
                self.resultsLabel5 = tk.Label(text=str(record[4]), padx=5, pady=5)
                self.resultsLabel5.grid(row=10, column=0)
        except: 
            pass
    
            
##===============================================================================================
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