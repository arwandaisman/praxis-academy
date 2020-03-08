class Dog:

    kind = 'canine'         # class variable 

    def __init__(self, name):
        self.name = name    # instance variable 
        self.tricks = []
        
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.kind                  
e.kind                  
d.name                  
e.name                  
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks        