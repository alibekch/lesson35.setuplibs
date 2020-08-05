from models import Grade, Person
p1 = Person("Linda", "passkeylinda")
p2 = Person("Lennon", "Yorika")

persons = [p1, p2]

g1=Grade("11b", persons)
g1.print_persons()