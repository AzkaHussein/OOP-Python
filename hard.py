def is_palindrome(s): return s == s[::-1]

print(is_palindrome("racecar"))   # Expected: True
print(is_palindrome("python"))    # Expected: False
print(is_palindrome("habibah"))   # Expected: True


def is_armstrong(n):
    digits = str(n)
    return n == sum(int(d)**len(digits) for d in digits)

print(is_armstrong(153))   # Expected: True
print(is_armstrong(370))   # Expected: True
print(is_armstrong(123))   # Expected: False
