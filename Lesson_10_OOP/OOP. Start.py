"""
Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.
"""
from dataclasses import dataclass
import json


class AnimalFactory:
	def get_animal(self, animal_type, *args, **kwargs):
		if animal_type == "Cat":
			return Cat(*args, **kwargs)
		elif animal_type == "Dog":
			return Dog(*args, **kwargs)
		else:
			raise ValueError(f"Invalid animal type: {animal_type}")


@dataclass
class Cat:
	name: str
	age: int

	def meow(self):
		print(f"{self.name} meows")

	def serialize(self):
		return json.dumps({"name": self.name, "age": self.age})


@dataclass
class Dog:
	name: str
	breed: str

	def bark(self):
		print(f"{self.name} barks")

	def serialize(self):
		return json.dumps({"name": self.name, "breed": self.breed})


factory = AnimalFactory()

cat = factory.get_animal("Cat", "Murka", 5)
cat.meow()
print(cat.serialize())

dog = factory.get_animal("Dog", "Sharik", breed="Husky")
dog.bark()
print(dog.serialize())







