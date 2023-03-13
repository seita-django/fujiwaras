
class stringCalculator:

    # Task 1 and 2
    def Calculate1(self, num1):
        if not num1:
            return 0
        return int(num1)


    # Task 3
    def Calculate3(self, nums):
        num1, num2 = map(int, nums.split(','))
        return num1 + num2

    # Task 4
    def Calculate4(self, nums):

        num1, num2 = nums.split('\n')
        return int(num1) + int(num2)

    # Task 5
    def Ccalculate5(self, numbers):
        if '\n' in numbers:
            # Split the input string into three separate strings
            num1, num2, num3 = map(int, numbers.split('\n'))

        else:
            # Split the input string into three separate strings
            num1, num2, num3 = map(int, numbers.split(','))

        return num1 + num2 + num3

    # Task 6


    # Task 7
    def Ccalculate7(self, numbers):
        if '\n' in numbers:
            # Split the input string into three separate strings
            num1, num2, num3 = map(int, numbers.split('\n'))

        else:
            # Split the input string into three separate strings
            num1, num2, num3 = map(int, numbers.split(','))

        if num1 > 1000:
            num1 = 0
        if num2 > 1000:
            num2 = 0
        if num3 > 1000:
            num3 = 0

        return num1 + num2 + num3