import asyncio
import threading

from coroutines.id import async_id


class ThreadedCoroRunner:
    def __init__(self, loop=None):
        self.threaded_loop = asyncio.new_event_loop() if loop is None else loop

        def threaded_loop_runner(loop: asyncio.AbstractEventLoop):
            asyncio.set_event_loop(loop)
            loop.run_forever()

        self.thread = threading.Thread(target=threaded_loop_runner, args=(self.threaded_loop,), daemon=True)
        self.thread.start()

    def run(self, coro):
        return asyncio.run_coroutine_threadsafe(coro, self.threaded_loop)

if __name__ == "__main__":
    coro_runner = ThreadedCoroRunner()
    print(coro_runner.run(async_id(1)).result(timeout=10))
