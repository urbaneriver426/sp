class Node:

	def __init__(self, v):
		self.value = v
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def add_in_tail(self, item):
		if self.head is None:
			self.head = item
		else:
			self.tail.next = item
		self.tail = item

	def print_all_nodes(self):
		node = self.head
		while node != None:
			print(node.value)
			node = node.next

	def find(self, val):
		node = self.head
		while node is not None:
			if node.value == val:
				return node
			node = node.next
		return None

	def find_all(self, val):
		node = self.head
		listOfNodes = []
		while node is not None:
			if node.value == val:
				listOfNodes.append(node)
				node = node.next
			else:
				node = node.next
		return listOfNodes

	def delete(self, val, all=False):
		currentNode = self.head
		previousNode = None
		if self.head is None:
			return
		else:
			if self.head.value == val:
				if self.len() == 1:
					self.head = None
					self.tail = None
					return
				else:
					previousNode, currentNode  = self.head, self.head.next
					self.head = currentNode
					if all==False:
						return
		if all==False:
			while currentNode is not None:
				if currentNode.value == val:
					previousNode.next = currentNode.next
					if currentNode is self.tail:
						self.tail = previousNode
					return
				else:
					previousNode = currentNode
					currentNode = currentNode.next
			return
		else:
			while currentNode is not None:
				if currentNode.value == val:
					previousNode.next = currentNode.next
					if currentNode is self.tail:
						self.tail = previousNode
					currentNode = currentNode.next
				else:
					previousNode = currentNode
					currentNode = currentNode.next

	def clean(self):
		self.head = None
		self.tail = None

	def len(self):
		count = 0
		currentNode = self.head
		while currentNode is not None:
			count += 1
			currentNode = currentNode.next
		return count

	def insert(self, afterNode, newNode):
		if self.len() == 0:
			self.add_in_tail(newNode)
		else:
			currentNode = self.head
			previousNode = None
			while currentNode is not None:
				if currentNode.value == afterNode.value:
					newNode.next, currentNode.next = currentNode.next, newNode
					if currentNode is self.tail:
						self.tail = newNode
					return
				else:
					currentNode = currentNode.next
			if currentNode is None:
				self.add_in_tail(newNode)
