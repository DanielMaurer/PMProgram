'''
This will be the View for the PMProgram. These classes will consist of various
windows that allow the user to interact with the program. As we move forward,
I will continue to add functionality.

'''

# Importing tkinter and additional stuff
import tkinter as tk
from tkinter import ttk

# Declaring font constants
LARGE_FONT = ("Verdana", 12)
TITLE_FONT = ("Verdana", 24)
SUBTITLE_FONT = ("Verdana", 16)

class PMProgram(tk.Tk): # inherited Tk from tkinter

    # PMProgram constructor
    def __init__(self, *args, **kwargs): # args shows that we can pass anything in, kwargs represents passing dictionaries

        tk.Tk.__init__(self, *args, **kwargs) # initialize Tkinter too

        # Creating the initial window
        containter = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True) # fill will make sure that both ends are covered. Expand will make the fill go until there is no space.
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} # frames that will be a list that contains the windows of the application

        # Function that takes the pages and adds them to the frames list
        for f in (MainPage, PageOne, PageTwo, PageThree):
            frame = f(container, self) # This defines the frame and gives it access to the contanier
            self.frames[f] = frame
            frame.grid(row = 0, column = 0, sticky='nsew') # sticky defines the directions the frame should stretch to

        self.show_frrame(MainPage):

    def show_frame(self, key):

        frame = self.frames[key] # key will tell us what frame we are in
        frame.tkraise() # brings the desired frame to be viewed


class MainPage(tk.Frame):
    

        
