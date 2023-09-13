import unittest
import number_of_students_unable_to_eat_lunch


class TestNumberOfStudents(unittest.TestCase):
    def test(self):
        self.assertEqual(
            number_of_students_unable_to_eat_lunch.countStudents(students = [1,1,1,0,0,1],sandwiches = [1,0,0,0,1,1],),3)
        self.assertEqual(
            number_of_students_unable_to_eat_lunch.countStudents(students = [1,1,0,0],sandwiches = [0,1,0,1],),0)        

if __name__ == '__main__':
    unittest.main()
