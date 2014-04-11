import unittest
import hashcalendar


class calendarCase(unittest.TestCase):

    def testMakeMonth(self):
        testMonth = hashcalendar.make_month(2014, 4)
        self.assertEqual(testMonth(10), 'Th')
        self.assertRaises(KeyError, testMonth, 0)
        self.assertRaises(KeyError, testMonth, 75)

        testMonth = hashcalendar.make_month(1988, 7)
        self.assertEqual(testMonth(7), 'Th')
        self.assertRaises(KeyError, testMonth, 32)

        testMonth = hashcalendar.make_month(1988, 2)
        self.assertEqual(testMonth(29), 'Mo')
        self.assertRaises(KeyError, testMonth, 30)

        testMonth = hashcalendar.make_month(1989, 2)
        self.assertEqual(testMonth(28), 'Tu')
        self.assertRaises(KeyError, testMonth, 29)

if __name__ == "__main__":
    unittest.main()
