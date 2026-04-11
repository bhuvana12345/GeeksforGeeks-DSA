class myQueue:
    def __init__(self, n):
        self.size = n
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def isFull(self):
        return len(self.queue) == self.size
    
    def enqueue(self, x):
        if not self.isFull():
            self.queue.append(x)
    
    def dequeue(self):
        if not self.isEmpty():
            self.queue.pop(0)
    
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.queue[0]
    
    def getRear(self):
        if self.isEmpty():
            return -1
        return self.queue[-1]