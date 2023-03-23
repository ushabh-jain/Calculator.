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