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


