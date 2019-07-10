import pickle, json

d = dict(name='李敦', age=20, score=90)
# print(pickle.dumps(d))
# with open('C:/Users/Lee/StudySpace/python_study/basic/io/test.txt', 'rb') as f:
#     # pickle.dump(d, f)
#     print(pickle.load(f))

# bb = b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x03\x00\x00\x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04KZu.'
# print(pickle.loads(bb))

# 如果ensure_ascii为True(默认值)，则输出保证将所有输入的非ASCII字符转义。如果确保ensure_ascii为False，这些字符将原样输出。
print(json.dumps(d, ensure_ascii=False))
# print(json.loads('{"name": "Bob", "age": 20, "score": 90}'))

class Student:
    
    def __init__(self, name, age, score):
        self._name = name
        self._age = age
        self._score = score

def student2dict(stu):
    return {'name': stu._name, 'age': stu._age, 'score': stu._score}

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

# s = Student('Lee', 28, 98)
# print(json.dumps(s, default=student2dict))
# print(json.dumps(s, default=lambda obj: obj.__dict__))
# dd = '{"name": "Lee", "age": 28, "score": 98}'
# print(json.loads(dd, object_hook=dict2student))



