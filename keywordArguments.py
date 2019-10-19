def myFunc(arg1, arg2, arg3, *args, **kwargs):
    print(str(arg1))
    print(str(arg2))
    print(str(arg3))
    print(str(args))
    print(str(kwargs))

myFunc(1,2,3,12,14,age=21)