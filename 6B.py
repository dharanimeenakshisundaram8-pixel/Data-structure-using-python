class Stack:
    def __init__(self):
        self.items = []
       
    def push(self, item):
        self.items.append(item)
       
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
       
    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = deque()
       
    def enqueue(self, item):
        self.items.append(item)
       
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None
       
    def is_empty(self):
        return len(self.items) == 0

class PalindromeChecker:
    def is_palindrome(self, text):
        stack = Stack()
        queue = Queue()
        for ch in text:
            if ch.isalnum():
                ch = ch.lower()
                stack.push(ch)
                queue.enqueue(ch)
       
        while not stack.is_empty():
            if stack.pop() != queue.dequeue():
                return False
        return True


text_input = input("Enter a string: ")
checker = PalindromeChecker()

if checker.is_palindrome(text_input):
    print("Palindrome")
else:
    print("Not a palindrome")
