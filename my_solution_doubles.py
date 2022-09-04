class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]


    def sort(self):
        return sorted(self.lst)

if __name__ == "__main__":
    some_inst = SomeClass()
    print(some_inst.sort())