from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, root=None):
        if root == None: self.root = None
        else: self.root = Node(root)

    def _insert(self, v):
        # if self.root == None: self.root.value = v
        parent = self.root
        child = self.root
        while child != None:
            parent = child
            if parent.value <= v:
                child = parent.left
            else:
                child = parent.right

        if parent.value <= v:
            parent.left = Node(v)
        else:
            parent.right = Node(v)

    def tree_from_list(self, a):
        if len(a) == 0: return
        self.root = Node(a[0])
        for i in range(1, len(a)):
            self._insert(a[i])

    def _find(self, v):
        parent = self.root
        if parent.value == v: return parent

        child = self.root
        while child != None:
            parent = child
            if parent.value <= v:
                child = parent.left
            else:
                child = parent.right
        if parent.value == v: return parent
        else: return -1


    def height(self, node):
        if node is None: return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max( left_height, right_height)


    def preorder(self, start, result = ''):
        '''Root > Left > Right'''
        if start is not None:
            result += str(start.value) + '-'
            result = self.preorder(start.left, result)
            result = self.preorder(start.right, result)
        return result


    def inorder(self, start, result = ''):
        '''Left > Root > Right'''
        if start is not None:
            result = self.inorder(start.left, result)
            result += str(start.value) + '-'
            result = self.inorder(start.right, result)
        return result

    def postorder(self, start, result = ''):
        '''Left > Right > Root'''
        if start is not None:
            result = self.postorder(start.left, result)
            result = self.postorder(start.right, result)
            result += str(start.value) + '-'
        return result


    def levelorder(self, start):
        if start:
            result = ''
            queue = deque([start])
            while len(queue) > 0:
                temp = queue.popleft()
                result += str(temp.value) + '-'
                if temp.left: queue.append(temp.left)
                if temp.right: queue.append(temp.right)
            return result[:-1]
        return None


    def reverse_levelorder(self, start):
        if start:
            result = ''
            queue = deque([start])
            stack = deque()
            while len(queue) > 0:
                temp = queue.pop()
                stack.appendleft(temp.value)
                if temp.left: queue.append(temp.left)
                if temp.right: queue.append(temp.right)
            for i in stack: result += str(i) + '-'
            return result[:-1]
        return None


if __name__ == '__main__':

    # tree = BinaryTree(1)
    # tree.root.left = Node(2)
    # tree.root.right = Node(3)
    # tree.root.left.left = Node(4)
    # tree.root.left.right = Node(5)
    # tree.root.right.left = Node(6)
    # tree.root.right.right = Node(7)


    a = [1,2,3,4,5,6,7]
    tree = BinaryTree()
    tree.tree_from_list(a)

    print('preorder:', tree.preorder(tree.root))
    print('inorder:', tree.inorder(tree.root))
    print('postorder:', tree.postorder(tree.root))
    print('levelorder:', tree.levelorder(tree.root))
    print('reverse_levelorder:', tree.reverse_levelorder(tree.root))

    print('height:', tree.height(tree.root))