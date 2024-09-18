class Animal:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def make_sound(self):
        pass

    def eat(self):
        pass
    
    
class Bird(Animal):
    # сократим кол-во писанины за счет **kwargs
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def make_sound(self):
        print(f"{self.name.title()} издает причудливые звуки: 'Чык-чырык!'")


class Mammal(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def make_sound(self):
        print(f"{self.name.title()} издает леденящий кровь рык!")
        

class Reptile(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def make_sound(self):
        print(f"{self.name.title()} издает неприятное шипение.")


def animal_sounds(animal):
        animal.make_sound()


animals = [Bird(name="воробышек", kind='grey'),
           Mammal(name="лев", kind='ferocious'),
           Reptile(name="игуана", kind="skinny")]

for animal in animals:
    animal_sounds(animal)
