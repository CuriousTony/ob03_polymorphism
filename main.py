class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass
    
    
class Bird(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def make_sound(self):
        print(f"{self.name.title()} издает причудливые звуки: 'Чык-чырык!.")


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
