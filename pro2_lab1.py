#Develope a class called calculator with a following
#functions(add,sub,divide). then define an object from this class
#in the main part

class Calculator():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        super().__init__(num1,num2)
    
    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def divide(self):
        return self.num1 / self.num2
    
    def __str__(self):
        return 'the add = {} , the sub = {} , the divide = {}'.format(self.add,self.sub,self.divide)

if __name__ == "__main__":
    x = Calculator(2,2)
    print("the result ",x.add,x.sub,x.divide)

    