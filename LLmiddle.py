class Node(object):

	def __init__(self, data):
		self.data = data
		self.nextNode = None


class LinkedList(object):

	def __init__(self):
		self.head = None
		self.size = 0


	def insert_start(self, data):

		self.size = self.size + 1
		newNode = Node(data)

		if not self.head:
			self.head = newNode

		else:
			newNode.nextNode = self.head
			self.head = newNode


	def remove(self, data):

		if not self.head:
			return 

		self.size = self.size - 1

		currNode = self.head
		prevNode = None

		while currNode.data != data:
			prevNode = currNode
			currNode = currNode.nextNode   

		if prevNode is None:
			self.head = currNode.nextNode
		else:
			prevNode.nextNode = currNode.nextNode

	def size1(self):
		return self.size

	def size2(self):

		actualNode = self.head
		size = 0

		while actualNode is not None:
			actualNode = actualNode.nextNode
			size+=1

		return size


	def insertEnd(self, data):

		self.size = self.size + 1
		newNode = Node(data)

		actualNode = self.head

		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode

		actualNode.nextNode = newNode

	def traverse(self):

		actualNode = self.head

		while actualNode is not None:
			print("%d" % actualNode.data)
			actualNode = actualNode.nextNode


linkedlist = LinkedList()

linkedlist.insert_start(12)
linkedlist.insert_start(122)
linkedlist.insert_start(3)
linkedlist.insertEnd(31)

linkedlist.traverse()

linkedlist.remove(3)
linkedlist.remove(12)
linkedlist.remove(122)
linkedlist.remove(31)

print(linkedlist.size2())


















