import asyncio

from gevent_patch_tests.patch import patch_all

patch_all()

from coro_runner import ThreadedCoroRunner

loop = asyncio.get_event_loop()
ThreadedCoroRunner(loop).run(asyncio.sleep(1)).result()
