

class Counter:
    def __init__(self):
        self._value = 0
    
    def add(self):
        self._value += 1
    
    def remove(self):
        if self._value <= 0:
            self.clear()
        else:
            self._value -= 1
    
    def clear(self):
        self._value = 0
    
    def get_value(self):
        return self._value



















