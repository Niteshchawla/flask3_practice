import time
from threading import Thread

def do_work():
	print("Starting work")
	time.sleep(1) # downloading an image
	print("Work done")
	
ti = time.time()

for _ in range(5):
	do_work()

print("Time taken without threading:", time.time()-ti)

ti = time.time()

threads = []
for _ in range(5):
	t = Thread(target=do_work)
	t.start()
	threads.append(t)

for t in threads:
	t.join() # wait for the thread to finish

print("Time taken with threading:", time.time()-ti)