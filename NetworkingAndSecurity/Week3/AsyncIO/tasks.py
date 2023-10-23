import asyncio

async def main():
    task = asyncio.create_task(name('Tayyeba')) # tell the event loop to execute as soon as possible
    await task # lets task run before following line is printed
    print("Finished")

async def name(Tayyeba): # defining a coroutine
    print(Tayyeba) # printing the name
    await asyncio.sleep(1)

asyncio.run(main()) # starting the event loop