class Node:
  def __init__(self,value=None):
    self.value=value
    self.next=None
class SLinkedList:
  def __init__(self):
      self.head=None
      self.tail=None
  def __iter__(self):
    node=self.head
    while node:
      yield node
      node=node.next
  def insertsll(self,value,location):
    newnode=Node(value)
    if self.head==None:
      self.head=newnode
      self.tail=newnode
    else:
      if location==0:
        newnode.next=self.head
        self.head=newnode
      elif location==1:
        newnode.next=None
        self.tail.next=newnode
        self.tail=newnode
      else:
        tempnode=self.head
        index=0
        while index<=location-3:
          tempnode=tempnode.next
          index+=1
        newnode.next=tempnode.next
        tempnode.next=newnode
  
      
sll=SLinkedList()
sll.insertsll(6,1) 
sll.insertsll(1,1) 
sll.insertsll(1,1)      
sll.insertsll(1,1) 
sll.insertsll(4,100) 
print([node.value for node in sll])
        
        
        
      
    
    

