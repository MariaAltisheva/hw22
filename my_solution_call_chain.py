class Person:
    def __init__(self, room_number=42, population=100500):
        self.room_number = room_number
        self.population = population

    def get_person_room(self):
        return self.room_number

    def get_city_population(self):
        return self.population


person = Person()
print(person.get_person_room())
print(person.get_city_population())