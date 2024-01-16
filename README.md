# threading
Python Script that demostrates the use of threading and multithreading on a Linux Machine. This project was made for my System Programming for Engineers class.

THREAD.PY FILE

Function print_tid:
  Uses threading.get_native_id() to get the native thread ID.
  Prints the thread ID.
Function sleep(s):
  Takes a parameter s for the number of seconds to sleep.
  Prints the thread ID using print_tid.
  Sleeps for the specified number of seconds, printing '...z...' during each second.
  Prints '==========' after waking up.
Function main:
  Sets s to 5.
  Creates a Thread object (t) targeting the sleep function with s as an argument.
  Starts the thread using t.start().
  Waits for the thread to finish using t.join().
  Conditional check for top-level execution:
  
If the script is executed as the main program, it calls the main function.

GLOBAL.PY FILE

Global variable alist:
  Defines a list of size 5 initialized with zeros.
Function accumulate(i):
  Takes a parameter i as an index.
  Calculates a starting value s based on the index.
  Accumulates values in the alist from s to s + 10.
  Prints the accumulated value and the native thread ID using threading.get_native_id().
Function main:
  Creates five threads (thread1 to thread5), each targeting the accumulate function with a different index.
  Starts all threads.
  Waits for all threads to finish.
  Calculates the total sum of the alist.
  Prints the total.
  Conditional check for top-level execution:

If the script is executed as the main program, it calls the main function.

thread.py demonstrates the use of threading to create and start a thread that sleeps for a specified duration.
global.py showcases multithreading with a shared global list. Each thread accumulates values into the shared list, and the main program calculates the total sum of the list after all threads finish.
