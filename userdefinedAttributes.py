class Edureka():
    def __init__(self):
        self.__pri = "I am private."
        self._pro = "I am protected."
        self.pub = "I am public."

ob = Edureka()
print(ob.pub)
print(ob._pro)
#print(ob.__pri)