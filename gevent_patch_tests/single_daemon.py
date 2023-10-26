import asyncio

from gevent_patch_tests.patch import patch_all

patch_all()

from coro_runner import ThreadedCoroRunner

ThreadedCoroRunner().run(asyncio.sleep(1)).result()
