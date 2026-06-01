class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None for _ in range(capacity)]
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        size = self.getSize()
        capacity = self.getCapacity()
        if size == capacity:
            self.resize()
        self.arr[size] = n
        self.size += 1



    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.arr = self.arr + [None] * self.getCapacity()

    def getSize(self) -> int:
        return self.size 
    
    def getCapacity(self) -> int:
        return len(self.arr)