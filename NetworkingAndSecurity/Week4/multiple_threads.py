import logging
import threading
import time

#define a function that represents the behaviour of each thread
def thread_function(name):
    #log a message when the thread starts
    logging.info("Thread %s: starting", name)
    time.sleep(2) #stimulate some work by sleeping for 2 seocnds
    logging.info("Thread %s: finishing", name)
    #log a messge when the thread finishes 

if __name__ == "__main__":
    #configure logging with a specfic message format and level
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    #create a list to store references to the threads
    threads = list()
    for index in range(3):
        #log a message before creating and starting a thread
        logging.info("Main    : create and start thread %d.", index)
        #create a new thread, passing the thread function and arguement (index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        #Add the thread to the list for the later reference
        x.start()
        #start the thread

    #Iterate through the list of threads and wait for each one to finsih 
    for index, thread in enumerate(threads):
        #Log a message before waiting for the thread to finish 
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        #wait for the thread to finish 
        logging.info("Main    : thread %d done", index)
        #log a message indicating that the thread has finished