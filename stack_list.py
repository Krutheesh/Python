

#implementaion of stack using list with no size limit
class Stack:
  def __init__(self):
      self.list=[]
  def is_empty(self):
    if self.list==[]:
      return True
    return False
  def push(self,value):
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
      print(self.list,)
    else:
      for i in range(len(self.list)-1,-1,-1):
        print(self.list[i])

s=Stack() 
s.display()
print(s.is_empty() ) 
s.push(1)
s.push(2)
s.push(-30000000000000000000000)
s.push(4000000000000000000000000000)
s.display()
print(s.peek())
s.pop()
#s.delete()
print("--")
s.display()
    
      
      
    