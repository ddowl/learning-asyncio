import asyncio

from coro_runner import ThreadedCoroRunner
from gevent_patch_tests.patch import patch_all

runners = [ThreadedCoroRunner() for _ in range(2)]

patch_all()

futs = [runner.run(asyncio.sleep(1)) for runner in runners]
for futs in futs:
    futs.result()