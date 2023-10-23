import asyncio

async def main():
    task = asyncio.create_task(name('Tayyeba')) # tell the event loop to execute as soon as possible

async def name(Tayyeba): # defining a coroutine
    print(Tayyeba) # printing the name
    await asyncio.sleep(1)
    print("Finished") # printing the message after 5 seconds

asyncio.run(main()) # starting the event loop