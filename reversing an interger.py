def reverse_integer_string(n: int) -> int:
    # Handle negative numbers by separating the sign
    if n < 0:
        return -int(str(abs(n))[::-1])
    
    return int(str(n)[::-1])

# Examples
print(reverse_integer_string(12345))  # Output: 54321
print(reverse_integer_string(-987))   # Output: -789
