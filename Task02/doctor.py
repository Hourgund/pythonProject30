from human import Human


class Doctor(Human):
    def hello(self):
        super().hello()
        print(" Im a good doctor!")
