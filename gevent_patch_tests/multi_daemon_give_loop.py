import asyncio

from gevent_patch_tests.patch import patch_all

patch_all()

from coro_runner import ThreadedCoroRunner

loop = asyncio.get_event_loop()
futs = [ThreadedCoroRunner(loop).run(asyncio.sleep(1)) for _ in range(2)]
for futs in futs:
    futs.result()