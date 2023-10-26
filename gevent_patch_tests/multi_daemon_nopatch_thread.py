import asyncio

from gevent_patch_tests.patch import patch_all

patch_all(thread=False, select=False)

from coro_runner import ThreadedCoroRunner

num_runners = 100
futs = [ThreadedCoroRunner().run(asyncio.sleep(1)) for _ in range(num_runners)]
for futs in futs:
    futs.result()