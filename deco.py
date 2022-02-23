def sub_mod(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        func(a,b)
    return inner
@sub_mod
def sub(a,b):
    print(a-b)
a,b=(int(i) for i in input().split())
sub(a,b)