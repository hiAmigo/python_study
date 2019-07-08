class Student(object):
    pass

s0 = Student()
s0.name = 'Lee'
print(s0.name)

def set_age(self, age):
    self.age = age

from types import MethodType

s0.set_age = MethodType(set_age, s0)
s0.set_age(23)
print(s0.age)

s1 = Student()
# s1.set_age(21)

def set_score(self, score):
    self.score = score

Student.set_score = set_score
s0.set_score(88)
s1.set_score(79)
print(s0.score)
print(s1.score)

class Student1(object):
    __slots__ = ('name', 'age')

s2 = Student1()
s2.name = 'Lee'
s2.age = 34
# s2.score = 90