#implementation of stack using list with size limit
from numpy import triu_indices


class Stack():
  def __init__(self,limit):
    self.list=[]
    self.limit=limit
  def is_empty(self):
      if self.list==[]:
        return True
      return False
  def is_full(self):
    if len(self.list)==self.limit:
      return True
    return False

  def push(self,value):
    if self.is_full():
      print("the stack is full")
    else:
      self.list.append(value)
      return "value is pushed into the stack successfully"
  def pop(self):
    if self.is_empty():
      return("stack is empty ")
    else:
      return self.list.pop()
  def peek(self):
    if self.is_empty():
      return "list is empty"
    else:
      return self.list[len(self.list)-1]
  def delete(self):
    self.list=[]
  def display(self):
    if self.is_empty():
      print(self.list)
    else:
      for i in range(len(self.list)-1,-1,-1):
        print(self.list[i])
s=Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.display()
s.push(6)
s.delete()
s.display()
