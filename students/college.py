import bisect
from bisect import bisect_left, bisect_right
from unittest import result

from sortedcontainers import SortedSet, SortedKeyList


class College:
    def __init__(self):
        self.__students = SortedSet()
        self.__sorted_score_students = SortedKeyList(key=lambda s: (s.score,s.id))
    def add_student(self, student):
        if student in self.__students:
            raise ValueError(f'Student with {student.id} already exists')

        self.__students.add(student)
        self.__sorted_score_students.add(student)

    def remove_student(self, student):
        if student not in self.__students:
            raise ValueError(f'Student with {student.id} does not exist')
        self.__students.remove(student)
        self.__sorted_score_students.remove(student)

    def get_students_sorted_by_id(self):
        return list(self.__students)

    def get_students_sorted_by_score(self):
        return list(self.__sorted_score_students)


#Hw+test,include max+min
    # def get_students_by_scores_between(self,min_score,max_score):
    #     res = []
    #     for students in self.__sorted_score_students:
    #         if min_score <= students.score <= max_score:
    #             res.append(students)
    #     return res

    def get_students_by_scores_between(self,min_score,max_score):
        left = self.__sorted_score_students.bisect_key_left((min_score,0))
        right = self.__sorted_score_students.bisect_key_right((max_score, float('inf')))
        return self.__sorted_score_students[left:right]








