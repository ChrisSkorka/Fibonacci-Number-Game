class FibonacciSequenceGenerator:
    def __init__(self, limit=None):

        if type(limit) not in [type(None), int, float]:
            raise TypeError

        self.limit = None if limit == None else int(limit)
        self.last = None
        self.secend_last = None
        self.count = 0

    def __iter__(self):
        self.last = None
        self.secend_last = None
        self.count = 0
        return self

    def __next__(self):
        if self.limit != None and self.count >= self.limit:
            raise StopIteration

        if self.last == None:
            next_value = 0
        elif self.secend_last == None:
            next_value = 1
        else:
            next_value = self.last + self.secend_last

        self.secend_last, self.last = self.last, next_value
        self.count += 1
        return next_value
