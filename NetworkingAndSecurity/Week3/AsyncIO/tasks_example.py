import asyncio

async def fetch_data(): # async function
    print("start fetching")
    await asyncio.sleep(2) # await keyword to wait for the sleep function to finish
    print("done fetching") # this will be printed after the sleep function is done
    return {"data": 1} # return a dictionary

async def print_numbers():
    for i in range(10): # print numbers from 0 to 9
        print(i) # print the number
        await asyncio.sleep(0.25) # wait for 0.25 seconds

async def main():
    task1 = asyncio.create_task(fetch_data()) # create a task
    task2 = asyncio.create_task(print_numbers()) # create another task

    value = await task1 # wait until the first task is done
    print(value) # print the returned value
    await task2 # wait until the second task is done

asyncio.run(main()) # run the main function