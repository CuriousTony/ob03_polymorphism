class Animal:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
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


animals_dict = {
    'bird': Bird(name="воробышек", kind='grey'),
    'mammal': Mammal(name="лев", kind='ferocious'),
    'reptile': Reptile(name="игуана", kind="skinny")
}

for animal in animals_dict.values():
    animal_sounds(animal)


class Employee:
    def __init__(self, name):
        self.name = name


class Zookeeper(Employee):
    def __init__(self, spec, **kwargs):
        super().__init__(**kwargs)
        self.spec = spec

    def feed_animals(self):
        print(f"{self.name.title()} is feeding animals.")


class Veterinarian(Employee):
    def __init__(self, spec, **kwargs):
        super().__init__(**kwargs)
        self.spec = spec

    def treat_animals(self):
        print(f"{self.name.title()} is treating animals.")


class Zoo:
    def __init__(self):
        self.employees = []
        self.pets = []

    # агрегация
    def add_pet(self, pet_type):
        if pet_type.lower() in animals_dict:
            self.pets.append(animals_dict[pet_type.lower()])
            print(f"{pet_type.title()} successfully transferred to the Zoo!")

    # композиция
    def add_employee(self, role):
        if role == 'vet':
            employee = Veterinarian(name='Mark', spec='veterinarian')
            self.employees.append(employee)
        elif role == 'keeper':
            employee = Zookeeper(name='Tom', spec='zookeeper')
            self.employees.append(employee)

    def show_list(self, choice):
        if choice == 'employee':
            for guy in self.employees:
                print(f"{guy.name.title()} the {guy.spec}")
        elif choice == 'pets':
            for pet in self.pets:
                print(f"{pet.name} the {pet.kind}")


leningradsky_zoopark = Zoo()
leningradsky_zoopark.add_pet('bird')
leningradsky_zoopark.add_pet('mammal')
leningradsky_zoopark.add_pet('reptile')
leningradsky_zoopark.show_list('pets')
leningradsky_zoopark.add_employee('keeper')
leningradsky_zoopark.add_employee('vet')
leningradsky_zoopark.show_list('employee')
