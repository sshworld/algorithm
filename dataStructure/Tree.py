class Node :
    
    def __init__(self, item) :
        self.data = item
        self.left = None
        self.right = None

    def size(self) :
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self) :
        leftDepth = self.left.depth() if self.left else 0
        rightDepth = self.right.depth() if self.right else 0
        return leftDepth + 1 if leftDepth >  rightDepth else rightDepth + 1

class BinaryTree :

    def __init__(self, r) :
        self.root = r

    def size(self) :
        if self.root : return self.root.size()
        else : return 0

    def depth(self) :
        if self.root : return self.root.depth()
        else : return 0

def init_tree() :
    global root

    new_node = Node('A')
    root = new_node

    new_node = Node('B')
    root.left = new_node
    new_node = Node('C')
    root.right = new_node

    new_node1 = Node('D')
    new_node2 = Node('E')
    node = root.left
    node.left = new_node1
    node.right = new_node2

    new_node1 = Node('F')
    new_node2 = Node('G')
    node = root.right

    node.left = new_node1
    node.right = new_node2

def preorder_traverse(node) :
    if node == None : return
    print(node.data, end = '->')
    preorder_traverse(node.left)
    preorder_traverse(node.right)

def inorder_traverse(node) :
    if node == None : return
    inorder_traverse(node.left)
    print(node.data, end = '->')
    inorder_traverse(node.right)

def postorder_traverse(node) :
    if node == None : return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.data, end = "->")
    

if __name__ == "__main__" :
    init_tree()

    preorder_traverse(root)
    print()
    inorder_traverse(root)
    print()
    postorder_traverse(root)
    print()
    print(root.size())
    print(root.depth())