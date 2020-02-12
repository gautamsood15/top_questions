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

		 