def int_to_binary(n):
    if n == 0:
        return "0"
    
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    
    return "".join(reversed(binary))

print(int_to_binary(161))  
