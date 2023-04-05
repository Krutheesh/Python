class Node:
  def __init__(self,value=None):
    self.value=value
    self.next=None
class SLL:
  def __init__(self):
    self.head=None
    self.tail=None
  def insert_begin(self,value):
    newnode=Node(value)
    if self.head==None:
      self.head=self.tail=newnode
    else:
      newnode.next=self.head
      self.head=newnode
  def insert_end(self,value):
    newnode=Node(value)
    if self.head==None:
      self.head=self.tail=newnode
    else:
      newnode.next=None
      self.tail.next=newnode
      self.tail=newnode
  def display(self):
    temp=self.head
    if self.head==None:
      print("empty linked list")
    else:
      while temp!=None:
        print(temp.value,end=' ')
        temp=temp.next
    
sll1=SLL()
'''sll1.insert_begin(1)
sll1.insert_begin(2)
sll1.insert_begin(3)
sll1.insert_begin(4)
sll1.insert_end(1)
sll1.insert_end(2)'''
sll1.insert_end(3)
sll1.insert_end(4)
sll1.display()

        
    
      
      
    
      


      