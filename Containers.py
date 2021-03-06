import itertools
class BST:
    def __init__(self):
        self.root = None
        self.set_mode(BST.NODUP)
    def push(self, value):
        node = BST.__Node(value)
        if self.root is None:
            self.root = node
        else:
           self.__insert(self,self.root,node)

    def set_mode(self,mode):
        if isinstance(mode,BST.__Mode):
            self.__insert = mode.run

    @staticmethod
    def binary_insert_wdup(tree, root, node):
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                tree.binary_insert_wdup(tree, root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                tree.binary_insert_wdup(tree, root.right, node)

    @staticmethod
    def binary_insert_ndup(tree, root, node):
        while True:
            if root.data > node.data:
                if root.left is None:
                    root.left = node
                    break
                else:
                    root = root.left
            elif root.data < node.data:
                if root.right is None:
                    root.right = node
                    break
                else:
                    root = root.right
            else:
                break

    def print(self):
        print(self.toList())

    def toList(self):
        out = list()
        temp = list()
        c = self.root
        if c is None:
            return out
        while True:
            if c.left is not None:
                temp.append(c)
                c = c.left
                continue
            elif c.right is not None:
                out.append(c.data)
                c = c.right
                continue
            elif len(temp) is 0:
                out.append(c.data)
                break
            else:
                out.append(c.data)
                c = temp.pop()
                out.append(c.data)
                while c.right is None and len(temp) is not 0:
                    c = temp.pop()
                    out.append(c.data)
                if c.right is None:
                    break
                c = c.right
                continue
        return out

    @staticmethod
    def search(tree, root, key):
        while True:
            if root.data > node.data:
                if root.left is None:
                    root.left = node
                    break
                else:
                    root = root.left
            elif root.data < node.data:
                if root.right is None:
                    root.right = node
                    break
                else:
                    root = root.right
            else:
                break


    class __Node:
        def __init__(self, val):
            self.left = None
            self.right = None
            self.data = val

    class __Mode:
        def __init__(self, ru):
            self.run = ru

    WDUP = __Mode(binary_insert_wdup.__get__(object))
    NODUP = __Mode(binary_insert_ndup.__get__(object))
class Algorithm:
    @staticmethod
    def binary_search(array, target):
        lower = 0
        upper = len(array)
        while lower < upper:  # use < instead of <=
            x = lower + (upper - lower) // 2
            val = array[x]
            if target == val:
                return x
            elif target > val:
                if lower == x:  # this two are the actual lines
                    break  # you're looking for
                lower = x
            elif target < val:
                upper = x

if __name__ is "__main__":
    for n in itertools.permutations(range(0,11)):
        tree = BST()
        for j in n:
            tree.push(j)
            print(j)