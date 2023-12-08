#!/usr/bin/env python3
import concurrent.futures
import logging
import random
import threading

SENTINEL = object()


class Pipeline:
    """
    Class to allow a single element pipeline
    between producer and consumer.
    """

    def __init__(self):
        self.message = 0 # stores message to pass
        # these are both threading.Lock objects
        self.producer_lock = threading.Lock() # restricts access to the message by the producer thread
        self.consumer_lock = threading.Lock() # restricts access to the message by the consumer thread
        self.consumer_lock.acquire()

    def get_message(self, name):
        logging.debug("%s:about to acquire getlock", name)
        self.consumer_lock.acquire() # make consumer wait until a message is ready
        logging.debug("%s:have getlock", name)
        message = self.message # get message
        logging.debug("%s:about to release setlock", name)
        self.producer_lock.release() # allows the producer to insert the next message into the pipeline
        logging.debug("%s:setlock released", name)
        return message

    def set_message(self, message, name):
        logging.debug("%s:about to acquire setlock", name)
        self.producer_lock.acquire() # make producer wait until consumer is done with previous message
        logging.debug("%s:have setlock", name)
        self.message = message # set message
        logging.debug("%s:about to release getlock", name)
        self.consumer_lock.release() # allows consumer to retrieve next message from pipeline
        logging.debug("%s:getlock released", name)


def producer(pipeline): # Producer thread reads from network and puts message into pipeline
    """Pretend we're getting a message from the network."""
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    # Send a sentinel message to tell consumer we're done
    pipeline.set_message(SENTINEL, "Producer")


def consumer(pipeline): # reads message from pipeline and writes it to a fake database, printing it out
    """Pretend we're saving a number in the database."""
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S") # configure logging
    logging.getLogger().setLevel(logging.DEBUG) # see exactly where each thread acquires and releases the locks

    pipeline = Pipeline() # create pipeline object
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor: # create thread pool with 2 threads
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)