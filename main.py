#Importing the necessary modules
from tkinter import *
#import parser
from math import factorial


root = Tk()
root.title('Calculator')

#It keeps the track of current position on the input text field
i = 0
# Receives the digit as parameter and display it on the input field
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1
 
# Calculate function scans the string to evaluates and display it
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
 
# Function which takes operator as input and displays it on the input field
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length
 
#Function to clear the input field 
def clear_all():
    display.delete(0,END)
#Function which works like backspace
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")

#Function to calculate the factorial and display it
def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

#--------------------------------------UI Design ---------------------------------------------

#adding the input field
display = Entry(root)
display.grid(row=1,columnspan=6,sticky=N+E+W+S)
 
#Code to add buttons to the Calculator

Button(root,text="1",command = lambda :get_variables(1)).grid(row=2,column=0, sticky=N+S+E+W)
Button(root,text=" 2",command = lambda :get_variables(2)).grid(row=2,column=1, sticky=N+S+E+W)
Button(root,text=" 3",command = lambda :get_variables(3)).grid(row=2,column=2, sticky=N+S+E+W)
