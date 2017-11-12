class Heap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, value):
        self.heap_list.append(value)
        self.current_size += 1
        self.parent_up()

    def remove(self, idx=1):
        temp = self.heap_list[idx]
        self.heap_list[idx] = self.heap_list[self.current_size]
        self.heap_list.pop()
        self.current_size -= 1
        self.parent_down(idx)
        return temp

    def peek(self):
        return self.heap_list[1]

class MinHeap(Heap):

    def parent_up(self):
        idx = self.current_size
        while idx // 2 > 0:
            if self.heap_list[idx // 2] > self.heap_list[idx]:
                temp = self.heap_list[idx // 2]
                self.heap_list[idx // 2] = self.heap_list[idx]
                self.heap_list[idx] = temp
            idx //= 2

    def parent_down(self, idx):
        idx = idx
        while idx * 2 <= self.current_size:
            mv = self.min_val(idx)
            if self.heap_list[idx] > self.heap_list[mv]:
                temp = self.heap_list[idx]
                self.heap_list[idx] = self.heap_list[mv]
                self.heap_list[mv] = temp
            idx = mv

    def min_val(self, idx):
        if idx * 2 + 1 > self.current_size:
            return idx * 2
        else:
            if self.heap_list[idx * 2 + 1] > self.heap_list[idx * 2]:
                return idx * 2
            else:
                return idx * 2 + 1

class MaxHeap(Heap):

    def parent_up(self):
        idx = self.current_size
        while idx // 2 > 0:
            if self.heap_list[idx // 2] < self.heap_list[idx]:
                temp = self.heap_list[idx // 2]
                self.heap_list[idx // 2] = self.heap_list[idx]
                self.heap_list[idx] = temp
            idx //= 2

    def parent_down(self, idx):
        idx = idx
        while idx * 2 <= self.current_size:
            mv = self.max_val(idx)
            if self.heap_list[mv] > self.heap_list[idx]:
                temp = self.heap_list[mv]
                self.heap_list[mv] = self.heap_list[idx]
                self.heap_list[idx] = temp
            idx = mv

    def max_val(self, idx):
        if idx * 2 + 1 > self.current_size:
            return idx * 2
        else:
            if self.heap_list[idx * 2] > self.heap_list[idx * 2 + 1]:
                return idx * 2
            else:
                return idx * 2 + 1
