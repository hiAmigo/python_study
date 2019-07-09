import logging

try:
    num = 10/0
    print('result is %d' % num)
except ZeroDivisionError as e:
    # logging.exception(e )
    print('except---', e)
except ValueError as e:
    print('valueException')
finally:
    print('finally')
print('END')


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

main()
