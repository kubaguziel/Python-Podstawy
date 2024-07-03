class Dog():
    """Prosta próba modelowania psa"""
    def __init__(self, name, age):
        """Inicjalizacja atrybutów name i age"""
        self.name = name
        self.age = age

    def sit(self):
        """Symulacja, że pies siada po otrzymaniu polecenia"""
        print(f"\n{self.name.title()} teraz siedzi. ")

    def roll_over(self):
        """Symulacja, że pies się turla."""
        print(f"\n{self.name.title()} teraz się turla. ")

my_dog = Dog('Dafik',7)

my_dog.sit()
my_dog.roll_over()