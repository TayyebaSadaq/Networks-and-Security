import asyncio

async def main():
    print("Tayyeba")
    await asyncio.sleep(1) # await keyword is used to wait for the coroutine to finish
    print("Sadaq")
    await asyncio.sleep(5)
    print("Finished")

asyncio.run(main()) # starting the event loop