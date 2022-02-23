def sub(a,b):
    print(a-b)
def sub_mod(fun):
        def inner(a,b):
            if a<b:
                a,b=b,a
            fun(a,b)
        return inner
a,b=(int(i) for i in input().split())
su=sub_mod(sub)
sub(a,b)

