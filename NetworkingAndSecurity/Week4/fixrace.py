#basic synchronisation with lock 

import logging
import time
import threading
import concurrent.futures


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)

    def update(self, name):
        #log a message to indicate the threa is starting the update
        logging.info("Thread %s: starting update", name)
        #make a local copy of the value to work with 
        local_copy = self.value
        local_copy += 1 #update the local copy 
        time.sleep(0.1) #stimulate some processing time with a sleep 
        self.value = local_copy #update the shared value in the database
        logging.info("Thread %s: finishing update", name)
        #log a message to indicate the thread has finished the update 

if __name__ == "__main__":
    #configure logging
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)
    #create an instance of Fakedatabase
    database = FakeDatabase()
    #log the intial value of the database
    logging.info("Testing update. Starting value is %d.", database.value)
    #use ThreadPoolExecutor to run two threads that call the 'update' methods
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)
    #log the final value of the database (may not be updated yet, as threads are synchronous)