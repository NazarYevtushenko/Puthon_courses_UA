

# __call__
class Counter:
    def __init__(self):
        self.counter = 0

    def __call__(self, *args, **kwargs):
        print("__call__")
        self.counter += 1
        return self.counter

# __repr__


class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self): #Для отображения в режиме отладки(Для разработчика или если метод __str__ не предопределен - тогда для вывода в print)
        return f'{self.__class__}: {self.name}'


    def __str__(self):
        return f'{self.name}'



class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

# реализовать любым способом патерн одиночка (singleton)

class DataBase:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        if not hasattr(self, 'user'):
            self.user = user
            self.psw = psw
            self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")

#Нужно создать класс, который должен формировать только первые пять объектов.
# Остальные (шестой, седьмой и т.д.) должны быть ссылкой на последний (пятый) созданный объект.
class SingletonFive:
    __instance = None
    __count = 0

    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__instance = super().__new__(cls)
            cls.__count += 1
        return cls.__instance

    def __init__(self, name):
        if not hasattr(self, "name"):
            self.name = name



def main():
    #call check
    print("Call check")
    c = Counter()
    c()
    c()
    c()
    res = c.counter
    print(res, '\n')


    #Property check
    p = Person("Vasya", 44)
    print(p.old)
    p.old = 23
    p.__dict__['old'] = 100
    print(p.__dict__)
    print(p.old)
    del p.old
    print(p.__dict__,'\n')

    #Singelton check
    db = DataBase('root', "123", 80)
    db2 = DataBase('root2', "5678", 45)
    print(id(db), id(db2))
    print(db.connect())
    print(db2.connect())

    #Singeltone five check
    objs = [SingletonFive(str(n)) for n in range(10)]

if __name__ == '__main__':
    main()
