class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # print('contains', self.value)
        if target == self.value:
            return True

        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            return False
