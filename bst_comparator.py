class TreeComparator(object):

	def compare_trees(self, node1, node2):

		if not nodel or not node2:
			return node1 == node2

		if node1.data is not node2.data:
			return False 

		return self.compare_trees(node1.leftChild, node2.leftChild) and self.compare_trees(node1.rightChild, node2.rightChild)


class Node(object):

	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None

class BinarySearchTree(object):

	def __init__(self):
		self.root = None

	def insert(self, data):
		if not self.root:
			self.root = Node(data)

		else:
			self.insertNode(data, self.root)

	def insertNode(self, data, node):

		if data < node.data:
			if node.leftChild:
				self.insertNode(data, node.leftChild)

			else:
				node.leftChild = Node(data)

		else:
			if node.rightChild:
				self.insertNode(data, node.rightChild)

			else:
				node.rightChild = Node(data)


	def remove(self, data):
		if self.root:
			self.root = self.removeNode(data, self.root)

	def removeNode(self, data, node):
		if not node:
			return node

		if data < node.data:
			node.leftChild = self.removeNode(data, node.leftChild)

		elif data > node.data:
			node.rightChild = self.removeNode(data, node.rightChild)

		else:

			if not node.leftChild and not node.rightChild:
				print("Removing a leaf node....")
				del node
				return None

			if not node.leftChild:
				print("Removing node with single right child ")

				tempNode = node.rightChild
				del node
				return tempNode

			elif not node.rightChild:
				print("Removing node with single left child ")

				tempNode = node.leftChild
				del node
				return tempNode

			print("Removing node with 2 children")

			tempNode = self.getPredecessor(node.leftChild)
			node.data = tempNode.data
			node.leftChild = self.removeNode(tempNode.data, node.leftChild)

		return node


	def getPredecessor(self, node):

		if node.rightChild:
			return self,getPredecessor(node.rightChild)

		return node


	def getMinValue(self):
		if self.root:
			return self.getMin(self.root)

	def getMin(self, node):
		if node.leftChild:
			return self.getMin(node.leftChild)

		return node.data

	def getMaxValue(self):
		if self.root:
			return self.getMax(self.root)

	def getMax(self, node):
		if node.rightChild:
			return self.getMax(node.rightChild)

		return node.data

	def traverse(self):
		if self.root:
			self.traverseInOrder(self.root)

	def traverseInOrder(self, node):

		if node.leftChild:
			self.traverseInOrder(node.leftChild)

		print("%s" % node.data)

		if node.rightChild:
			self.traverseInOrder(node.rightChild)


if __name__ == "__main__":

	bst1 = BinarySearchTree()

	bst1.insert(10)
	bst1.insert(13)
	bst1.insert(2)
	bst1.insert(14)

	bst2 = BinarySearchTree()

	bast2.insert(10)
	bast2.insert(13)
	bast2.insert(2)
	bast2.insert(14)

	comparator = TreeComparator()

	print(comparator.compare_trees(bst1.root, bst2.root))


