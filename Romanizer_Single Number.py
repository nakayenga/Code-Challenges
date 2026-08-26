def romanizer(number):
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    result = []
    for i in range(len(num)):
        while number >= num[i]:
            result.append(sym[i])
            number -= num[i]
            
    return "".join(result)

print(romanizer(1994))
