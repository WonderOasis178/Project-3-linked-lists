from Project3.slist import SList
from Project3.course import Course
import random


def calculate_gpa(courseList):
  sumGrades = 0
  credits = 0
  for course in courseList:
      sumGrades += course.grade() * course.credit_hr()
      credits += course.credit_hr()
  if credits == 0:
    return 0
  return sumGrades / credits


def is_sorted(lyst):
  for i in range(0, len(lyst) - 1):
    if lyst[i] > lyst[i + 1]:
      return False
  return True


def main():
  random.seed(0)
  cl = SList()
  for _ in range(37):
      cl.insert(Course(random.randrange(1000, 7000), "test", 1.0, 2.0))

  #PRINT LISTS
  #cl.printList()
  print(cl.__str__())
  # Function call
  print("Count of nodes is :", cl.size())


if __name__ == "__main__":
    main()
