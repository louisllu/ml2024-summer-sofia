class Data:
    def __init__(self):
        self.nums = {}
        self.index = 1
        self.length = 0
        
    def initialize(self, length):
        self.length = int(length)
    
    def insert(self, input):
        self.nums[input] = self.nums.get(input, [])
        self.nums[input].append(self.index)
        self.index += 1

    def search(self, target):
        if target not in self.nums:
            return -1
        else:
            return self.nums[target]
