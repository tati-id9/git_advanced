class Calculator(object):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
 
    def __add__(self):
        return self.arg1 + self.arg2
 
    def __sub__(self):
        return self.arg1 - self.arg2
 
    def __mul__(self):
        return self.arg1 * self.arg2
 
    def __div__(self):
        return self.arg1 // self.arg2