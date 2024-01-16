# thread.py.
import sys
import time
import threading

def print_tid():
	tid = threading.get_native_id()
	print(f"[TID = {tid}]")
	
def sleep(s):
	print('==========')
	print_tid()
	for n in range(s):
		print('...z...')
		time.sleep(1)
	print('==========')
def main():
	s = 5
	
	# Create a Thread object.
	t = threading.Thread(target = sleep, args = (s,))
	
	# Start the thread.
	t.start()
	
	#Wait for the thread to finish
	t.join()
	
#Check if code is being exeuted in a top-level code environment
if __name__ == '__main__':
	main()