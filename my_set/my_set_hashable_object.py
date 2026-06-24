from dataclasses import dataclass, field

from my_set import MySet

@dataclass(unsafe_hash=True)
class Person:
    id:int
    name:str = field(compare=False)

    def __init__(self,id, name):
        self.id = id
        self.name = name

    # def __hash__(self):
    #    return hash(self.id)
    #
    # def __eq__(self, other):
    #     if not isinstance(other, Person):
    #         return False
    #     return self.id == other.id


p1=Person(1,'John')
p2=Person(2,'Jane')
my_set_persons = MySet()
my_set_persons.add(p1)
my_set_persons.add(p2)


for person in my_set_persons:
    print(hash(person))