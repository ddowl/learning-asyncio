import asyncio

from gevent_patch_tests.patch import patch_all

patch_all()

from coro_runner import ThreadedCoroRunner

futs = [ThreadedCoroRunner().run(asyncio.sleep(1)) for _ in range(2)]
for futs in futs:
    futs.result()