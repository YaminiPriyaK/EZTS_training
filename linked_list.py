# linked list insertion, deleted

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        temp = self.head

        # If the head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the previous node
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # If key was not present in the linked list
        if temp == None:
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
        
if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_end(1)
    llist.insert_at_end(2)
    llist.insert_at_end(3)
    llist.insert_at_beginning(0)
    
    print("Linked List after insertion:")
    llist.print_list()
    
    llist.delete_node(2)
    
    print("Linked List after deletion of node with data 2:")
    llist.print_list()
