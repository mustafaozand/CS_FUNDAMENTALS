class Stack:
    pointer =  -1
    stack = []

    # def __init__(self, size):
    #     self.pointer =  -1
     
    #     self.stack = []

    def is_full(self):
        return self.pointer > -1
    
    def push(self, element):
        self.pointer += 1
        self.stack.append(element) 
        print("Element: ",self.stack[self.pointer], "pointer: ", self.pointer,  "has been added to the stack.")

    def pop(self):
        if self.pointer != -1:
            popped_element = self.stack
            self.pointer -= 1
            return popped_element
        
        return None
    
    def is_Empty(self):
        return self.pointer == -1
    
