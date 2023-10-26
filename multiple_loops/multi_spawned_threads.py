import asyncio

from coro_runner import ThreadedCoroRunner

num_runners = 100
futs = [ThreadedCoroRunner().run(asyncio.sleep(1)) for _ in range(num_runners)]

for fut in futs:
    fut.result()