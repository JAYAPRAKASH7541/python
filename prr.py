class Person:
    def __init__(self, name, age):
        # TODO: Fill code here
        self.name=name
        self.age=age


def get_person_details(person):
    return "{} is {} years old".format(person.name, person.age)


if __name__ == "__main__":
    name = input()
    age = int(input())

    person = Person(name=name, age=age)
    print(get_person_details(person))
