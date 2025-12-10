def is_anagram(s1, s2): return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))   # Expected: True
print(is_anagram("hello", "world"))     # Expected: False

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))   # Expected: 120
print(factorial(0))   # Expected: 1
