from student import Student


class SuperStudent(Student):
    def hello(self):
        msg = f"Hi! Im super student with name - {self.name}!"
        print(msg)
