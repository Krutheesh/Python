from textwrap import indent


class Node:
  def __init__(self,value=None):
    self.value=value
    self.next=None
class SLinkedList:
  def __init__(self):
      self.head=None
      self.tail=None
  def insertsll(self,value,location):
    newnode=Node(value)
    if self.head==None:
      self.head=newnode
      self.tail=newnode
    else:
      if location==0:
        newnode.next=self.head
        self.head=newnode
      elif location==-1:
        newnode.next=None
        self.tail.next=newnode
        self.tail=newnode
      else:
        try:
          tempnode=self.head
          index=0
          if location <-1:
            print("location not present to insert")
          else:
            while index<location-2:
              tempnode=tempnode.next
              index+=1
            newnode.next=tempnode.next
            tempnode.next=newnode
        except BaseException:
          print('location not present to insert ')
  def display(self):
    temp=self.head
    if self.head==None:
      print("empty linked list")
    else:
      while temp!=None:
        print(temp.value,end=' ')
        temp=temp.next
  def deleting_nodes(self,location):
    if self.head==None:
      print("empty linked list ,no nodes to delete")
    else:
      if location==0:
        if self.head==self.tail:
          self.head=self.tail=None
        else:
          self.head=self.head.next
      elif location==-1:
        if self.head==self.tail:
          self.head=self.tail=None
        else:
          temp=self.head
          while temp!=None:
            if temp.next==self.tail:
              break
            temp=temp.next
          temp.next=None
          self.tail=temp
    
         
          
        
sll=SLinkedList()
sll.insertsll(1,0) 
sll.insertsll(2,0) 
sll.insertsll(3,0)      
sll.insertsll(4,0) 
sll.insertsll(5,2) 
sll.insertsll(10,-1)
#sll.insertsll(7,30)
sll.display()
        
        
        
      
    
    

