import time
import threading
import asyncio

def sync_task(name):
    print(f"[SYNC] Bắt đầu {name}")
    time.sleep(2)
    print(f"[SYNC] Kết thúc {name}")

def run_sync():
    print("=== Chạy đồng bộ ===")
    start = time.time()
    for i in range(3):
        sync_task(f"Tác vụ {i+1}")
    print(f"⏱️ Tổng thời gian (Sync): {time.time() - start:.2f} giây\n")

# ----------- Threading -----------
def thread_task(name):
    print(f"[THREAD] Bắt đầu {name}")
    time.sleep(2)
    print(f"[THREAD] Kết thúc {name}")

def run_threading():
    print("=== Chạy đa luồng ===")
    start = time.time()
    threads = []
    for i in range(3):
        t = threading.Thread(target=thread_task, args=(f"Tác vụ {i+1}",))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(f"⏱️ Tổng thời gian (Threading): {time.time() - start:.2f} giây\n")

# ----------- AsyncIO -----------
async def async_task(name):
    print(f"[ASYNCIO] Bắt đầu {name}")
    await asyncio.sleep(2)
    print(f"[ASYNCIO] Kết thúc {name}")

async def run_asyncio():
    print("=== Chạy AsyncIO ===")
    start = time.time()
    tasks = [async_task(f"Tác vụ {i+1}") for i in range(3)]
    await asyncio.gather(*tasks)
    print(f"⏱️ Tổng thời gian (AsyncIO): {time.time() - start:.2f} giây\n")

# ----------- Main -----------
if __name__ == "__main__":
    run_sync()
    run_threading()
    asyncio.run(run_asyncio())
