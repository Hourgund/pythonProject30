class Human:
    def __init__(self, name="no name"):
        self.name = name

    # @property
    # def name(self):
    # return self.__name

    # @name.setter
    # def name(self, name):
    # self.__name = name

    def __str__(self):
        return self.name

    def hello(self):
        print(f"Hello! Im {self.name}.", end='')

    def work(self):
        pass
