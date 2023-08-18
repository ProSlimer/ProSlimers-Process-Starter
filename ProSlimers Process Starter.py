#ProSlimer's Process Starter

#I probably don't need all of these, but I can't remember why I added them and I am too lazy to figure it out
from cProfile import run
from concurrent.futures import process
from multiprocessing.sharedctypes import Value
import os
from urllib import response
import psutil
import time
from datetime import datetime
import PySimpleGUI as sg
import subprocess

#GUI Elements:
sg.theme('Dark Grey 13')
layout = [[sg.Text('Program Name')],
          [sg.Input()],
          [sg.Text('Executable Location')],
          [sg.Input(), sg.FileBrowse()],
          [sg.Text('Check Frequency (In seconds)')],
          [sg.Input()],
          [sg.OK('Start'), sg.Cancel()]]

window = sg.Window("ProSlimer's Process Starter", layout)

#GUI Logic:
while True:
    #Read data from the input fields of the window
    event, values = window.read()
    #If the "Start" button is pressed, pass the data and delete the window
    if event == 'Start':
        window.close(); del window
        break 
    #If the window is closed or the "Cancel" button is pressed, quit the program
    elif event ==sg.WIN_CLOSED or event == 'Cancel':
        quit()

#Set named variables to list items returned from the GUI window
program = values[0]
path = values[1]
delay = int(values[2])

print ("DEBUG:\nPROGRAM:",program, "\nPATH:",path ,"\nDELAY:",delay) #DEBUG: PATH VERIFICATON

def checkIfProcessRunning(program):

    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
    # Check if process name contains the given name string.
            if program.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def runprogram():

    # Check if given process was running or not.
    if checkIfProcessRunning(program):
        time.sleep(0) #Doesn't do anything.
    else:
    #Get current date and time.
        dateTimeObj = datetime.now()
    #Print date and time
        print(dateTimeObj)
    #Start given file
        os.startfile(path)
    #Log that the file was started
        print(program, "seems to have stopped, restarting")

print("Process starter is now looking for", program, "in", path, "every", delay, "seconds.\n")
#Set value = True to start infinate loop
while (True): 
    runprogram() 
    time.sleep (delay) 
