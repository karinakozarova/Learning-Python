class Car:

    def __init__(self,color,model):
        self.color = color
        self.model = model

    def print(self):
        return self.color + " " + self.model

    
car1 = Car("green","Toyota")
print(car1.print())