class Student(object):

    count = 0

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        Student.count += 1

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def print_score(self):
        print('%s score is %s' % (self.__name, self.__score))
        
# bart = Student('Bart Simpion', 46)
# bart.__name = 'New Name'
# print(bart.__name)
# print(bart.get_name())

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart', 10)
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart', 20)
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

