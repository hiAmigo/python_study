from io import StringIO
from io import BytesIO
filepath = 'c:/Users/Lee/StudySpace/python_study/basic/io/test.txt'

# with open(filepath, 'rb') as f:
#    print(f.read())
#    print(f.read(1))
#    for line in f.readlines():
#        print(line.strip())

# with open(filepath, 'a') as f:
#     f.write('\n Append something') 

f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World')
print(f.getvalue())

f1 = StringIO('Hello world bye')
while True:
    s = f1.readline()
    if s == '':
        break
    # print(s.strip())

f2 = BytesIO('李敦'.encode('utf-8'))
print(f2.getvalue())

f3 = BytesIO(b'\xe6\x9d\x8e\xe6\x95\xa6')
print(f3.read())