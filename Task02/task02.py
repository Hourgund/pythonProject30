from doctor import Doctor
from super_student import SuperStudent, Student
from laborexchange import LaborExchange


def main():
    st1 = Student("Alex")
    st2 = Student("Alice")
    st3 = Student("Harry")
    st4 = SuperStudent("Peter Parker")
    doc1 = Doctor("Dr.Strange")
    doc2 = Doctor("Dr.House")
    doc3 = Doctor("Dr.Watson")

    unemployed = (st1, st2, st3, st4, doc1, doc2, doc3)
    LaborExchange.execute(unemployed)


if __name__ == "__main__":
    main()
