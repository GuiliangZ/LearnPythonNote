# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#           
#                 ex. background tasks, garbage collection, waiting for input, long running processing
# 
import time
import threading

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")

# x = threading.Thread(target=timer)
# set the thread to a daemon thread, it will be killed automatically when the main thread is finished
x = threading.Thread(target=timer, daemon=True)
# x.setDaemon(True)
# x.isDaemon()      (return true or false)
x.start()

answer = input ("Do you wish to exit?")













