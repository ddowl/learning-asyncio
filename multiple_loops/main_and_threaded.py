import asyncio

from coro_runner import ThreadedCoroRunner

runner = ThreadedCoroRunner()
thread_fut = runner.run(asyncio.sleep(1))
asyncio.run(asyncio.sleep(1))
thread_fut.result()
