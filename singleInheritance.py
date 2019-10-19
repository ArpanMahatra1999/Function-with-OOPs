class base1:
    def fun(self):
        print("In class base1.")

class sub(base1):
    pass

ob = sub()
ob.fun()