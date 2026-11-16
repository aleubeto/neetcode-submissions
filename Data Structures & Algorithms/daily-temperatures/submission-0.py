class Stack:
    def __init__(self):
        self._items = []

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return self.size() == 0

    def push(self, item) -> None:
        self._items.append(item)

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot pick from empty stack")
        return self._items[-1]

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        return self._items.pop()

# O(n)
# O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = Stack()
        for i, t in enumerate(temperatures):
            while not stack.is_empty() and t > stack.peek()[1]:
                stack_i, stack_t = stack.pop()
                output[stack_i] = i-stack_i
            stack.push((i,t))
        return output