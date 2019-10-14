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

        
