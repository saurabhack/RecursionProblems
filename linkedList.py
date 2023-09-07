class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedLists:
    def __init__(self):
        self.head=None
    def push(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
            return
        new.next=self.head
        self.head=new
    def printlist(self):
        current=self.head
        while current!=None:
            print(current.data,end=" ")
            current=current.next
    def reversr(self):
        prev=None
        current=self.head
        while current!=None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
        return
if __name__=='__main__':
    d=LinkedLists()
    s=str(input())
    for i in s:
        d.push(i)
    d.printlist()
    d.reversr()
    print()
    d.printlist()