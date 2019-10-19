class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def dmy(cls, day, month, year):
        cls.year = year
        cls.month = month
        cls.day = day
        return cls(cls.year, cls.month, cls.day)

a = Date(2019,10,19)
print(a.year)

b = Date.dmy(19,10,2019)
print(b.year)