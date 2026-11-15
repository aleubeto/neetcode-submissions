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
        self._items.pop()

class Solution:
    def isValid(self, s: str) -> bool:
        closure_chars = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        open_chars = Stack()
        for char in s:
            if char in closure_chars:
                if not open_chars.is_empty() and open_chars.peek() == closure_chars[char]:
                    open_chars.pop()
                else:
                    return False
            else:
                open_chars.push(char)
        return True if open_chars.is_empty() else False