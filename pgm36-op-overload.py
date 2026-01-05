class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    def __add__(self, other):
        h = self.__hour + other.__hour
        m = self.__minute + other.__minute
        s = self.__second + other.__second
        if s >= 60:
            s -= 60
            m += 1
        if m >= 60:
            m -= 60
            h += 1
        return Time(h, m, s)
    def display(self):
        print(f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")
t1 = Time(2, 45, 50)
t2 = Time(1, 30, 20)
t3 = t1 + t2
print("Time 1:")
t1.display()
print("Time 2:")
t2.display()
print("Sum")
t3.display()