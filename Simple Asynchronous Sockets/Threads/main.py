import threading
import time

done = False

def count():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)
        
threading.Thread(target=count).start() #allows for multiple threads to run at the same time
#in this case it would be the count fuction and the input function

input("Press enter to quit\n") # Wait for user to press enter (or any key) to quit
done = True