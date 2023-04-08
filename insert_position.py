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
            while index<location-1:
              tempnode=tempnode.next
              index+=1
            newnode.next=tempnode.next
            tempnode.next=newnode
        except BaseException:
          print('location not present to insert ')
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
  def dele(self):
    print("krutheesg")
    h=t=self.head
    while t.next:
      if t.value<t.next.value:
        print(t.value)
        h.next=t.next
        h=h.next
        t=t.next
      else:
        t=t.next
       
        
        
      
      
    
    
sll=SLinkedList()






sll.insertsll(9,0)
sll.insertsll(5,0)
sll.insertsll(1,0)
sll.insertsll(2,0)
sll.insertsll(7,0)
sll.insertsll(9,0)
sll.insertsll(4,0)
sll.insertsll(5,0)
sll.insertsll(2,0)
sll.insertsll(6,0)
sll.dele() 

sll.display() 

        
     
        
    
    
    

