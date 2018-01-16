def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def parent(i):
    return i // 2


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def max_heapify(A, i, max_i):
    l = left(i)
    r = right(i)
    if l < max_i and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < max_i and A[r] > A[largest]:
        largest = r
    if largest != i:
        swap(A, i, largest)
        max_heapify(A, largest, max_i)


def build_max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        max_heapify(A, i, len(A))


def heap_sort(A):
    build_max_heap(A)
    n = len(A)
    while n > 0:
        swap(A, 0, n - 1)
        max_heapify(A, 0, n - 1)
        n -= 1


def print_tree(A, i=0, indent=0):
    if i < len(A):
        print('  ' * indent, A[i])
        print_tree(A, i * 2 + 1, indent + 1)
        print_tree(A, i * 2 + 2, indent + 1)


class PriorityQueue:
    """ Note: When using self.size as an **index** self.size - 1 is used due to
    0-based indexing. self.size is the same as len(self.heap), just updated
    'manually' for learning the algorithm.
    """

    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, x, k):
        """ Insert val x into the queue with priority k.
        """
        self.heap.append([x, float("-inf")])
        self.size += 1
        self.update_key(self.size - 1, k)

    def get_max(self):
        """ Returns the maximum priority item in the queue
        """
        return self.heap[0]

    def extract_max(self):
        # cleaner syntax:
        if self.size < 1:
            raise ValueError('heap underflow')
        max_ = self.heap.pop(0)
        self.size -= 1
        max_heapify(self.heap, 0, self.size - 1)
        return max_

    def update_key(self, i, k):
        if k < self.heap[i][1]:
            raise ValueError('new key is smaller than current key')
        self.heap[i][1] = k
        while i > 0 and self.heap[parent(i)][1] < self.heap[i][1]:
            swap(self.heap, i, parent(i))
            i = parent(i)


if __name__ == '__main__':
    a = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    print('Max Heap Demo:')
    print('Initial: {}'.format(a))
    a_copy = a[:]
    build_max_heap(a_copy)
    print('Max Heap: ')
    print_tree(a_copy)
    heap_sort(a)
    print('Heap Sorted: {}'.format(a))

    print('\nPriority Queue Demo:')
    q = PriorityQueue()
    q.insert('Top Priority', 3)
    q.insert('Third Priority', 2)
    q.insert('Second Priority', 1)
    q.insert('Also Second Priority', 1)
    q.insert('Also Top Priority', 3)
    print('Heap: {}'.format(q.heap))
    print('get_max: {}'.format(q.get_max()))
    print('update_key(1,5):')
    q.update_key(1, 5)
    print('get_max: {}'.format(q.get_max()))
    print('extract_max: {}'.format(q.extract_max()))
    print('Heap: {}'.format(q.heap))
