class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} 坐下了")
    def roll_over(self):
        print(f"{self.name}打滚")

my_dog=Dog('小黑',12)
my_dog.sit()
my_dog.roll_over()