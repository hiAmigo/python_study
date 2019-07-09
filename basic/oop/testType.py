def hello(self, name='world'):
    print('Hello, %s' % name)

Hello = type('Hello', (object,), dict(hello=hello))

h = Hello()
h.hello()
print(type(Hello))
print(type(h))

# mateclass是类的模板，必须从type派生
class ListMateclass(type):

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value : self.apend(value)
        return type.__new__(cls, name, bases, attrs)
