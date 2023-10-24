import logging #for logging messages
import threading #for logging messages
import time #for sleep

def thread_function(name):
    logging.info("Thread %s: starting", name) #logs a message when the thread starts 
    time.sleep(2) #stimulate some work by sleeping for 2 seconds
    logging.info("Thread %s: finishing", name) #logs a message when the thread finishes 

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s" #sets the log messafge format adn logging level 
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
#log a message before creating the thread
    logging.info("Main    : before creating thread")
#create a nre thread with the thread_function and arguements
    x = threading.Thread(target=thread_function, args=(1,))
#log a message before starting the thread
    logging.info("Main    : before running thread")
    x.start() #start the thread
    logging.info("Main    : wait for the thread to finish")
    #log a message indicating that the main program is waiting to finish 
    # x.join() #uncomment if you want the main program to complete and then join 
    logging.info("Main    : all done")
    #log a message to indicate that all actions are done and it may still be running as x.join is still commented out