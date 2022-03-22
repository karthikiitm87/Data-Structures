class Node:
    def __init__(self, data=None):
      self.data = data
      self.next = None

class sLInkedLIst:
    def __init__(self):
        self.head = None

    def listprint(self):
        curr = self.head
        while(curr != None):
            print(curr.data)
            curr = curr.next
        return

    def InsertAtBeggining(self, data):
        Newnode = Node(data)
        Newnode.next = self.head
        self.head = Newnode
        return

    def InsertAtEnd(self, data):
        Newnode = Node(data)
        if(self.head == None):
            self.head = Newnode
            return
        else:
            curr = self.head
            while(curr.next != None):
                curr = curr.next
            curr.next = Newnode
            return

    def InsertatNode(self, refnode, data):
        if(refnode == None):
            print('Reference Node is absent')
            return

        Newnode = Node(data)
        Newnode.next = refnode.next
        refnode.next = Newnode
        return

    def delwithkey(self, key):
        curr = self.head
        if(self.head.data == key):
            self.head = self.head.next
            curr = None
            return

        # Traversing the list until next node has the key to be removed
        while(curr.next.data != key):
            curr = curr.next
            if(curr.next == None):
                print('Key not found')
                return


        temp = curr.next
        curr.next = curr.next.next
        temp = None
        return



list = sLInkedLIst()
list.head = Node(2)
e2 = Node(3)
e3 = Node(4)
list.head.next = e2
e2.next = e3

list.InsertAtBeggining(5)
list.InsertAtEnd(5)
list.InsertatNode(e2, 8)
#list.listprint()

list.delwithkey(8)
list.listprint()