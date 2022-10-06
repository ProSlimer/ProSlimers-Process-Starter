from cProfile import run
from concurrent.futures import process
from multiprocessing.sharedctypes import Value
import os
from sys import path_hooks
from urllib import response
import psutil
import time
from datetime import datetime

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
        print(program, "seems to have stopped, restarting");
        
program = input("What is the name of the program we are looking for?\n")
path = input("And where is the file located? (Full path)\n")
delay = int(input("How often would you like to check? (in seconds; checking mroe often increases resource usage)\n"))
print('Process starter is now looking for', program, 'in', path, 'every', delay, 'seconds.\n')
#Start infinate loop
while (True): 
    runprogram() 
    time.sleep (0) 
