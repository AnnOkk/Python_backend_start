from students.student import Student
from students.college import College
from unittest import TestCase,main

student1=Student(2,"John",85)
student2=Student(1,"Jane",90)
student3=Student(4,"Bob",95)
student4=Student(3,"Alice",80)

students=[student1,student2,student3,student4]
class TestCollege(TestCase):
    def setUp(self):
        self.__college = College()
        for student in students:
            self.__college.add_student(student)

    def test_add_existing_student(self):
        with self.assertRaises(ValueError):
            self.__college.add_student(student1)

    def test_add_new_student(self):
        student5=Student(5,"Charlie",92)
        self.__college.add_student(student5)
        self.assertIn(student5,self.__college.get_students_sorted_by_id())
        self.assertIn(student5,self.__college.get_students_sorted_by_score())
    def test_remove_existing_student(self):
        self.__college.remove_student(student1)
        self.assertNotIn(student1,self.__college.get_students_sorted_by_id())
        self.assertNotIn(student1,self.__college.get_students_sorted_by_score())
    def test_get_students_sorted_by_id(self ):
        students_sorted_by_id=self.__college.get_students_sorted_by_id()
        self.assertListEqual([student2,student1,student4,student3] ,students_sorted_by_id)
    def test_get_students_sorted_by_score(self):
        students_sorted_by_score=self.__college.get_students_sorted_by_score()
        self.assertListEqual([student4,student1,student2,student3,] ,students_sorted_by_score)

if __name__ == '__main__':
    main()
