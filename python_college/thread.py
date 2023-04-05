#thread
#executing several tasks simultaneously where each task is independent seperate part of  same program is called thread thread based multitasking and each part is called a thread.
# ways of creating a thread
#1)creating a thread without using any class
# from threading import *
# def display():
#   for i in range(1,11):
#     print("Child Thread")
# t=Thread(target=display)
# t.start()
# for i in range(1,11):
#   print("  Main Thread")
  
#2)creating a thread with extending thread class
# from threading import*
# class Mythread(Thread):
#   def run (self):
#     for i in range(10):
#       print("-Child Thread-1-")
# t=Mythread()
# t.start()
# for i in range(10):
#   print("-main-")
    
#3)creating a thread without extending the thread class
from threading import*
class Mythread:
  def run(self):
    for i in range(10):
      print("-Child Thread-1-")
o=Mythread()
t=Thread(target=o.run)
t.start()
for i in range(10):
  print("-main-")
 