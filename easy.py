  def is_even(n): return "Even" if n % 2 == 0 else "Odd"

print("The number is", is_even(4))   # Expected: Even
print("The number is", is_even(7))   # Expected: Odd


def number_status(n): return "Positive" if n > 0 else "Negative" if n < 0 else "Zero"

print("The number is", number_status(10))   # Expected: Positive
print("The number is", number_status(-5))   # Expected: Negative
print("The number is", number_status(0))    # Expected: Zero
