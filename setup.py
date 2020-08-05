# from models import Person
# p1 = Person("Alibek", "passkey")
# print(p1.getFullName())

from setuptools import setup 

setup(
    name="NewProj1",#ЛЮБОЕ НАИМЕНОВАНИЕ
    url = "https://github.com/alibekch/lesson35.setuplibs",
    author = "alibek",
    packages = ["models"], #ЭТО ПАПКА КОТОРАЯ БУДЕТ ПРЕОБРАЗОВЫВАТЬСЯ
    installrequires=[],
    license="MIT",
    description = "my own lib"
)