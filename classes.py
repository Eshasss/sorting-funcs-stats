class MyList(list):
    def __init__(self, data):
        super().__init__(data)
        self.read = 0
        self.write = 0
    
    def __setitem__(self, key, item):
        self.write += 1
        super().__setitem__(key, item)

    def __getitem__(self, key):
        self.read += 1
        return super().__getitem__(key)
        
    def read(self):
        return self.read
    
    def write(self):
        return self.write
    
# b = MyList([3,4,5])
# print(b)
# b[0] = 1

# print(b.__setitem__(2,10))
# print(b.__getitem__(1))
# print(b.__getitem__(1))s
# print(b.__getitem__(1))