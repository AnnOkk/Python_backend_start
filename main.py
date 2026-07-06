from collections.abc import Iterator


class Fibonacci(Iterator):
    def __init__(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an integer")
        self.quantity = quantity
        self.counter = 0
        self.prev = 1
        self.prev_prev = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.quantity:
            raise StopIteration
        self.counter += 1
        if self.counter <= 2:
            return 1
        current = self.prev + self.prev_prev
        self.prev_prev = self.prev
        self.prev = current
        return current

# class Fibonacci:
#     def __init__(self,quantity):
#         self.quantity = quantity
#     def __iter__(self):
#         prev = 1
#         prev_prev = 1
#         counter = 1
#         while counter <= self.quantity:
#             if counter <= 2:
#                 yield 1
#             else:
#                 current = prev
#                 prev = prev + prev_prev
#                 prev_prev = current
#                 yield prev
#             counter += 1
