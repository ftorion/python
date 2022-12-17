class person:
    age = 20
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hi(self):
        print(f"привет {self.name} тебе {self.age}")

class enemi(person):
    def __init__(self, name, age, comm):
        super().__init__(name, age)
        self.comm = comm
    def Hello(self):
        print(f"{self.name} {self.age} {self.comm}")
