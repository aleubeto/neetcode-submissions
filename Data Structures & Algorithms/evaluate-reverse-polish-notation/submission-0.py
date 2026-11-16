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
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ("+","-","*","/")
        numbers = Stack()
        for token in tokens:
            if token not in operators:
                numbers.push(int(token))
            else:
                n1 = numbers.pop()
                n2 = numbers.pop()
                if token == "+":
                    numbers.push(n1+n2)
                elif token == "-":
                    numbers.push(n2-n1)
                elif token == "*":
                    numbers.push(n1*n2)
                elif token == "/":
                    numbers.push(int(n2/n1))
        return numbers.peek()