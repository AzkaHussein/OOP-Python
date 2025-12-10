class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Invalid withdrawal amount or insufficient funds"


# Test
account = BankAccount("Name")
print(account.deposit(1000))     # Expected
print(account.withdraw(500))     # Expected
print(account.withdraw(600))     # Expected



class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        return f"Grade {grade} added."

    def get_average(self):
        return sum(self.grades) / len(self.grades)


# Test
student = Student("Alice")
print(student.add_grade(90))   # Expected
print(student.add_grade(80))   # Expected
print(student.add_grade(70))   # Expected
print("Average grade:", student.get_average())   # Expected 80.0
