#global.py
import threading

alist = [0]*5

def accumulate(i):
	s = i*10
	acc = 0
	for n in range(s, s+10):
		acc += n
	alist[i] = acc
	tid = threading.get_native_id()
	print(f"Accumulated value in thread [{tid} -> {i}] is {acc}")

def main():

	thread1 = threading.Thread(target = accumulate, args = (0,))
	thread2 = threading.Thread(target = accumulate, args = (1,))
	thread3 = threading.Thread(target = accumulate, args = (2,))
	thread4 = threading.Thread(target = accumulate, args = (3,))
	thread5 = threading.Thread(target = accumulate, args = (4,))
	
	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()
	thread5.start()
	
	thread1.join()
	thread2.join()
	thread3.join()
	thread4.join()
	thread5.join()
	
	total = sum(alist)
	
	print(f"Total is: {total}")
	
if __name__ == '__main__':
	main()