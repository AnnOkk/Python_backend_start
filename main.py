# ## Write class MyStackInt with the following methods
#
#
# - push(num: int) adds number at top of the stack
#
#
# - pop() →int removes number from the top of stack with returning the number. Raises IndexError for empty stack
#
#
# - max() → int retuns maximal number in the stack. Raises IndexError for empty stack
#
#
# ## Note: all the above methods should have complexity O(1)
#
#
# ## Write tests for class MyStackInt

class MyStackInt:
    def __init__(self):
        self.stack = []
        self.max_stack = []
        # self.max_num = None #?

    def push(self, num: int) -> None:

        if len(self.max_stack) !=0 and num >= self.max_stack[-1]:
            self.max_stack.append(num)
        elif len(self.max_stack) !=0 and num <= self.max_stack[-1]:
            self.max_stack.append(self.max_stack[-1])
        elif len(self.max_stack) == 0:
            self.max_stack.append(num)
        return self.stack.append(num)



    def pop(self) -> int:
        if len(self.stack)==0:
            raise IndexError('Stack is empty')
        self.max_stack.pop()
        return self.stack.pop()

    def max(self) -> int:
        if len(self.stack)==0:
            raise IndexError('Stack is empty')
        return self.max_stack[-1]


# stack1 = MyStackInt()
# print(stack1.stack)
#
#
# stack1.push(1)
# stack1.push(2)
#
# print(stack1.stack)
#
# stack1.push(3)
# print(stack1.max())
# print(stack1.pop())
