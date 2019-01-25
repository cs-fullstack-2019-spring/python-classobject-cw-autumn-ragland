# Create a class Dog. Make sure it has the attributes name, breed, color, gender.
class Dog:
    def __init__(self,name="",breed="",color="",gender=""):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender
    # Create a function that will print all attributes of the class.
    def printAll(self):
        print(f'{self.name} is a {self.color} {self.gender} {self.breed}')

# create a class of people with name weight height
class BMI:
    def __init__(self,name="",weight=0,height=0):
        self.name = name
        self.weight = weight
        self.height = height
    # caculate BMI
    def caculation(self):
        return ((self.weight / (self.height * self.height))*703)
    # change the weight and height
    def changeIt(self,weight,height):
        self.weight = weight
        self.height = height
    # print name weight height and BMI
    def printAll(self):
        print(f'{self.name} weighs {self.weight} pounds and is {self.height} inches tall.\nTheir BMI is {self.caculation()}')

# Create a class Product that represents a product sold online. A product has a name, price, and quantity.
class Product:
    def __init__(self, name="", price=0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def changeProduct(self,xname="",xprice=0,xquantity=0):
        self.name = xname
        self.price = xprice
        self.quantity = xquantity
    def printAll(self):
        print(f'The {self.name} cost ${self.price} and we have {self.quantity}')

def main():
    # prob1()
    # prob2()
    prob3()
    # prob4()

def prob1():
    # Create an object of Dog
    dog1 = Dog("Sally","lab","gray","female",)
    # print all attributes
    dog1.printAll()

# Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.
def prob2():
    userInput = input("Enter a word\n")
    while userInput != "=":
        userInput = input("Okay! Enter another word\n")

# create objects in class BMI
def prob3():
    person1 = BMI("Autumn", 140, 62)
    person1.printAll()
    person1.changeIt(130, 63)
    person1.printAll()

    person2 = BMI("Adam", 160, 68)
    person2.printAll()
    person2.changeIt(150, 70)
    person2.printAll()

    person3 = BMI("Amy", 150, 49)
    person3.printAll()
    person3.changeIt(155, 51)
    person3.printAll()




# create an object in class Product
def prob4():
    newProdcut1 = Product("fidget spinners", 1, 500)
    newProdcut2 = Product("fidget spinners", 1)
    newProduct3 = Product("fidget spinners")

    newProdcut1.printAll()
    newProdcut2.printAll()
    newProduct3.printAll()

    newProdcut1.changeProduct("fidget spinner", 2)
    newProdcut2.changeProduct("mind nummer")
    newProduct3.changeProduct("fidget spinner", 1, 700)

    newProdcut1.printAll()
    newProdcut2.printAll()
    newProduct3.printAll()

if __name__ == '__main__':
    main()