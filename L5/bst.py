class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1

    def find_min(self):
        """ Find smallest node in subtree at this node
        """
        node = self
        while node.left is not None:
            node = node.left
        return node

    def next_largest(self):
        """ Find minimum node in subtree at this node that is greater than
        this node
        """
        if self.right is not None:
            return self.find_min()
        node = self
        while node.parent is not None and node.parent.right == node:
            node = node.parent
        return node.parent

    def update_size(self):
        self.size = (1 if self.left is None else self.left.size) + \
            (1 if self.right is None else self.right.size)

    def delete(self):
        """ Delete this node from the tree
        """
        if self.left is None and self.right is None:
            if self == self.parent.left:
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.left is None:
            if self == self.parent.left:
                self.parent.left = self.right
            else:
                self.parent.right = self.right
        elif self.right is None:
            if self == self.parent.left:
                self.parent.left = self.left
            else:
                self.parent.right = self.left
        else:
            successor = self.next_largest()
            self.data = successor.data
        current = self.parent
        while current is not None:
            current.update_size()
            current = current.parent
        return self

    def rank(self, data):
        """ Number of nodes <= data in the subtree at this node
        """
        left_size = 0 if self.left is None else self.left.size
        if data == self.data:
            return left_size + 1
        elif data < self.data:
            if self.left is None:
                return 0
            else:
                return self.left.rank(data)
        else:
            if self.right is None:
                return left_size + 1
            else:
                return self.right.rank(data) + left_size + 1


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new = Node(data)
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                node.size += 1
                if data < node.data:
                    if node.left is None:
                        node.left = new
                        new.parent = node
                        break
                    node = node.left
                elif data >= node.data:
                    if node.right is None:
                        node.right = new
                        new.parent = node
                        break
                    node = node.right
        return new

    def insert_multiple(self, items):
        for item in items:
            self.insert(item)

    def height(self):
        def traverse(root):
            right = left = max_height = 0
            if root:
                r = traverse(root.right) + 1 if root.right else 0
                l = traverse(root.left) + 1 if root.left else 0
                max_height += max(r, l)
            return max_height
        return traverse(self.root)

    def find_min(self):
        return self.root.find_min()

    def find_max(self):
        node = self.root
        while True:
            if node.right:
                node = node.right
            else:
                return node

    def find_val(self, data):
        node = self.root
        while node is not None:
            if data == node.data:
                return node
            elif data < node.data:
                node = node.left
            else:
                node = node.right

    def remove(self, data):
        node = self.find_val(data)
        if node:
            if node == self.root:
                self.root = node.right or node.left
            else:
                node.delete()
        return None

    def rank(self, data):
        """ Number of nodes <= data in the tree
        """
        if self.root is None:
            return 0
        else:
            return self.root.rank(data)

# ==============================================================================
# Traversal Algorithms
# ==============================================================================


def breadth_first_traverse(root):
    if root is None:
        return []
    visited, queue = [], [root]
    while queue:
        n = queue.pop()
        if n not in visited:
            visited.append(n)
            # don't add if child is None
            queue.extend(filter(None, [n.right, n.left]))
    return visited


def in_order_traverse(root):
    result = []

    def traverse(root):
        if root:
            traverse(root.left)
            result.append(root)
            traverse(root.right)

    traverse(root)
    return result


def pre_order_traverse(root):
    result = []

    def traverse(root):
        if root:
            result.append(root)
            traverse(root.left)
            traverse(root.right)

    traverse(root)
    return result


def post_order_traverse(root):
    result = []

    def traverse(root):
        if root:
            traverse(root.left)
            traverse(root.right)
            result.append(root)

    traverse(root)
    return result


if __name__ == '__main__':
    items = [10, 20, 15, 40, 30, 25, 5]
    tree = BinarySearchTree()
    tree.insert_multiple(items)

    max_node = tree.find_max()
    assert(max_node.data == max(items))
    print('Maximum value: ', max_node.data)

    min_node = tree.find_min()
    assert(min_node.data == min(items))
    print('Minimum value: ', min_node.data)

    print('Next largest after minimum value:',
          min_node.next_largest().data)

    height = tree.height()
    assert(height == 4)
    print('Tree Height: ', height)

    breadth_first = breadth_first_traverse(tree.root)
    breadth_first_data = [node.data for node in breadth_first]
    assert(breadth_first_data == [10, 5, 20, 15, 40, 30, 25])
    print('Breadth-First Traversal: {}'.format(breadth_first_data))

    in_order = in_order_traverse(tree.root)
    in_order_data = [node.data for node in in_order]
    assert(in_order_data == [5, 10, 15, 20, 25, 30, 40])
    print('In-order Traversal: {}'.format(in_order_data))

    pre_order = pre_order_traverse(tree.root)
    pre_order_data = [node.data for node in pre_order]
    assert(pre_order_data == [10, 5, 20, 15, 40, 30, 25])
    print('Pre-order Traversal: {}'.format(pre_order_data))

    post_order = post_order_traverse(tree.root)
    post_order_data = [node.data for node in post_order]
    assert(post_order_data == [5, 15, 25, 30, 40, 20, 10])
    print('Post-order Traversal: {}'.format(post_order_data))

    for node in post_order:
        print('Node value: {}, size: {}'.format(node.data, node.size))

    remove_val = 5
    tree.remove(remove_val)
    post_order = post_order_traverse(tree.root)
    post_order_data = [node.data for node in post_order]
    assert(5 not in post_order_data)
    print('Remove node with value ', remove_val)
    print('Post-order Traversal: {}'.format(post_order_data))

    for node in post_order:
        print('Node value: {}, size: {}'.format(node.data, node.size))

    remove_val = 10
    print('Current root: ', tree.root.data)
    tree.remove(remove_val)
    post_order = post_order_traverse(tree.root)
    post_order_data = [node.data for node in post_order]
    assert(remove_val not in post_order_data)
    print('Remove node with value {} (root node)'.format(remove_val))
    print('Post-order Traversal: {}'.format(post_order_data))
    print('New root node: ', tree.root.data)

    for node in post_order:
        print('Node value: {}, size: {}'.format(node.data, node.size))

    rank_val = 20
    print('Rank({}): {}'.format(rank_val, tree.rank(rank_val)))

    rank_val = 15
    print('Rank({}): {}'.format(rank_val, tree.rank(rank_val)))

    rank_val = 40
    print('Rank({}): {}'.format(rank_val, tree.rank(rank_val)))
