# Singly Linked List Implementation


class Node:
    # Create a node object to store items and the next
    # item they point to in memory

    def __init__(self, data, next_item):
        """
        :param data: value of data in node
        :param next_item: next value in the LinkedList
        """

        self.data_ = data
        self.next_ = next_item


class SinglyLinkedList:
    # Implementation of the most basic LinkedList
    # Methods
    # -> Insertions
    # -> Deletions
    # TODO - Add other methods; insert in-between, deletion in-between

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, data):
        """
        Inserts an item at the beginning and end of
        the LinkedList

        Time-complexity: O(1)

        :param data: an insert item into Linked List
        :return: None
        """

        insert_node = Node(data=data, next_item=None)

        if self.head is None:
            self.head = insert_node
            self.tail = insert_node
        else:
            self.tail.next_ = insert_node
            self.tail = insert_node

        self.length += 1

    def deletion(self):
        """
        Delete item at the head of the Linked List
        time-complexity: O(1)

        :return: data of deleted item
        """

        if self.head is None:
            return "Linked List is empty"
        else:
            delete_node = self.head

            # TODO Running error here; fix code below
            self.head = delete_node.next
            delete_node.next = None

            self.length -= 1

            return delete_node


# Instantiate Linked List
linked_list = SinglyLinkedList()

# Inserts
linked_list.insert("David")  # Insert item one
linked_list.insert("Mathews")  # Insert item two
linked_list.insert("John")  # Insert item three
linked_list.insert("Zachee")  # Insert item four

# Deletion
print(linked_list.deletion())
print(linked_list.deletion())
print(linked_list.deletion())
