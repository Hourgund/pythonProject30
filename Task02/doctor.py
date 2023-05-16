from human import Human


class Doctor(Human):
    def hello(self):
        super().hello()
        print(" Im a good doctor!")

    def work(self):
        print("I can cure.")