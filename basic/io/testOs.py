import os
import shutil

# print(os.name)
# print(os.environ)
# print(os.environ.get('path'))
# print(os.path.abspath('.'))
# print(os.path.join('C:/Users/Lee/StudySpace/python_study', 'testDir'))
# print(os.mkdir('C:/Users/Lee/StudySpace/python_study/testDir'))
# os.rmdir('C:/Users/Lee/StudySpace/python_study/testDir')
# print(os.path.split('C:/Users/Lee/StudySpace/python_study/testDir'))
# print(os.path.splitext('C:/Users/Lee/StudySpace/python_study/basic/io/testIO.py'))
# os.rename('C:/Users/Lee/StudySpace/python_study/basic/io/test.txt', 'rename.txt')
# os.remove('rename.txt')
# shutil.copyfile()
# for x in os.listdir('.'):
#     if os.path.isfile(x) and os.path.splitext(x)[1] == '.py':
#         print(x)



def searchFile(name):
    for root, dirs, files in os.walk('.'):
        for i in files:
            if name in i:
                print(os.path.join(root, i))

searchFile('testIO.py')