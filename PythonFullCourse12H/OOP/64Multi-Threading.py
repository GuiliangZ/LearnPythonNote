# thread = a flow of execution. Like a separate order of instruction
#           However each thread takes a turn running to achieve concurrency
#           GIL = (global interpreter lock),
#           allows only on thread to hold the control of the python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events(CPU intensive)
#             use multiprocessing

# io bound =  program/task spends most of it's time waiting for external events (user input, web scraping)
#             use multithreading

import threading
import time

#number of the active thread that is running
print(threading.active_count())
# print a list of all of the thread that is running
print(threading.enumerate())
# The one thread that is running is called the main thread
# can have more than one thread that is running, more than the main thread
# can have another thread running other program, like a count down timer (two thread running concurrently)
# They all take turns when one of the them is ideled


def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drink coffee")

def study():
    time.sleep(5)
    print("You finished studied")

# multitask ==> multi-threading
#Have 4 thread running, take about 5 secend to run, The main thread running its own task
x = threading.Thread(target = eat_breakfast, args = ())
x.start()

y = threading.Thread(target = drink_coffee, args = ())
y.start()

z = threading.Thread(target = study, args = ())
z.start()

#thread sychronization, the main thread wait for x, y, z thread to sychronized and finish 
x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
'''
eat_breakfast()
drink_coffee()
study()
# This program takes 12 sec to complete, complete those task sequentially 
'''





