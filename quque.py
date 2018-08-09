
# queue is a datastructure that stores data in a manner
# that first in first out(FIFO). Queue suppose to be faster than
# a list, this implementation is only for practice purpose.
class queue:
    def __init__(self, firstItem=None):
        self.data = [firstItem]

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        # check if queue is empty
        if self.data[0] == None:
            return -1;
        else:
            return self.data.pop(0)

    def peak(self):
        return self.data[0]

# testing code
first = queue(1)

first.enqueue(2)
print first.peak()

print first.data


