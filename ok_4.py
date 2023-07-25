# Python implementation of above approach
# link list node
class LNode:
	def __init__(self, data):
		self.data = data
		self.next = None
			
# binary tree node
class TNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
# function to print nodes in a given linked list
def printList(node):
	while(node is not None):
		print(node.data)
		node = node.next
	
def preOrder(root):
	if(root is None):
		return
	print(root.data)
	preOrder(root.left)
	preOrder(root.right)
	
def sortedListToBSTRecur(vec, start, end):
	if(start > end):
		return None
	mid = start + (int)((end-start)/2)
	if((end-start)%2 != 0):
		mid = mid+1
	root = TNode(vec[mid])
	root.left = sortedListToBSTRecur(vec, start, mid-1)
	root.right = sortedListToBSTRecur(vec, mid+1, end)
	return root
	

def sortedListToBST(head):
	vec = []
	temp = head
	while(temp is not None):
		vec.append(temp.data)
		temp = temp.next
	return sortedListToBSTRecur(vec, 0, len(vec)-1)


# let us create a sorted linked list to test the functions
# created linked list will be 1->2->3->4->5->6->7
head = LNode(1)
head.next = LNode(2)
head.next.next = LNode(3)
head.next.next.next = LNode(4)
head.next.next.next.next = LNode(5)
head.next.next.next.next.next = LNode(6)
head.next.next.next.next.next.next = LNode(7)
head.next.next.next.next.next.next.next = LNode(9)
head.next.next.next.next.next.next.next.next = LNode(22)
head.next.next.next.next.next.next.next.next.next = LNode(15)
head.next.next.next.next.next.next.next.next.next.next = LNode(55)
head.next.next.next.next.next.next.next.next.next.next.next = LNode(45)
head.next.next.next.next.next.next.next.next.next.next.next.next = LNode(23)
head.next.next.next.next.next.next.next.next.next.next.next.next.next =LNode(24)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next = LNode(26)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = LNode(28) 

print("Given Linked List : ")
printList(head)
print(" ")

# covert list to bst
root = sortedListToBST(head)
print("PreOrder Traversal of constructed BST : ")
preOrder(root)
