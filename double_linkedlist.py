from tkinter.messagebox import NO


class Node:
  def __init__(self,value=None):
      self.prev=None
      self.value=value
      self.next=None
class DLL:
  def __init__(self):
      self.head=None
      self.tail=None
  def inserting_nodes(self,value,location):
    newnode=Node(value)
    if self.head==None:
      self.head=newnode
      self.tail=newnode
    else:
      if location==0:
        self.head.prev=newnode
        newnode.next=self.head
        self.head=newnode
      elif location==-1:
        newnode.next=None
        self.tail.next=newnode
        newnode.prev=self.tail
        self.tail=newnode
      else:
          try:
            tempnode=self.head
            index=0
            if location <-1:
              print("location not present to insert")
            else:
              while index<location-1:
                tempnode=tempnode.next
                index+=1
              newnode.prev=tempnode
              newnode.next=tempnode.next
              tempnode.next=newnode
          except BaseException:
            print('location not present to insert ')
  def deleting_nodes(self,location):
    if self.head==None:
      print("empty doubly linkedlist")
    else:
      if location==0:
        if self.head==self.tail:
          self.head=self.tail=None
        else:
          self.head=self.head.next
          self.head.prev=None
      elif location==-1:
        if self.head==self.tail:
          self.head=self.tail=None
        else:
          self.tail=self.tail.prev
          self.tail.next=None
      else:
        try:
          if location<-1:
            print("location not present")
          else:
            tempnode=self.head
            index=0
            while index<location-1:
              tempnode=tempnode.next
              index+=1
            tempnode.next=tempnode.next.next
            if tempnode.next!=None: 
              tempnode.next.prev=tempnode
        except BaseException:
          print("node not present at a given location")    
  def delete_dll(self):
      if self.head==None:
        print("doubly linked not present to delete")
      else:
        temp=self.head
        while temp:
          temp.prev=None
          temp=temp.next
        self.head=None
        self.tail=None 
  def reverse_dll(self):
    l=[]
    if self.head==None:
      print("doubly link list not present to reverse \n",l)
    else:
      temp=self.tail
      while temp:
        l.append(temp.value)
        temp=temp.prev
      print(l)
      
                
        
  def display(self):
    l=[]
    temp=self.head
    if self.head==None:
      print(l)
    else:
      while temp!=None:
        l.append(temp.value)
        temp=temp.next
      print(l)
dll=DLL()
dll.inserting_nodes(1,0)
dll.inserting_nodes(0,0)
dll.inserting_nodes(2,0)
dll.inserting_nodes(7,0)
dll.inserting_nodes(6,0)
dll.inserting_nodes(8,0)
dll.inserting_nodes(5,0)
dll.inserting_nodes(9,-1)


#dll.deleting_nodes(6)


#dll.delete_dll()

      

dll.display()
dll.reverse_dll()   

      
    
