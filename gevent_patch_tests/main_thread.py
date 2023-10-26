import asyncio

from gevent_patch_tests.patch import patch_all

patch_all()

async def main():
    print("Hello asyncio!")

asyncio.run(main())