import re

reg = r'^\d{3}\-\d{3,8}$'
s0 = '020-334123'
if re.match(reg, s0):
    print(True)
else:
    print('False')

# 分割字符串
s1 = 'a b  s a  s     s'
print(re.split(r'\s+', s1))
# print(s1.split(' '))

s2 = 'a,b  s,a , s     s'
print(re.split(r'[\s\,]+', s2))

s3 = 'a,b  s,a , s;;;     s'
print(re.split(r'[\s\,\;]+', s3))

# 分组
m0 = re.match(r'^(\d{3})-(\d{3,8})$', s0)
print(m0.groups())
# print('g1 is %s, g2 is %s, g3 is %s' % (m0.group(0), m0.group(1), m0.group(2)))

s4 = '123120000'
m1 = re.match(r'^(\d+)(0*)$', s4)
print(m1.groups())

m2 = re.match(r'^(\d+?)(0*)$', s4)
print(m2.groups())

re_phone = re.compile(r'^(\d{3})-(\d{3,7})$')
print(re_phone.match('020-334123').groups())

