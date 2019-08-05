def my_abs(sum=10, *args, **kw):
    print(kw)
    for n in args:
        sum += n
    return sum

res = my_abs()
print(res)
