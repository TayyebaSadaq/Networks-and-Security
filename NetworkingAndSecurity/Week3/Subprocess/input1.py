user_data = input("Enter some data, empty string to quit: ")#

li = []

while user_data != "":
    li.append(user_data) # add the data to the list
    user_data = input("Enter some data, empty string to quit: ") # ask for more data
    
for item in (li):
    print(item)