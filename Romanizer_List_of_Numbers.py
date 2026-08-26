def romanizer(numbers):
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    result_list = []
    for n in numbers:
        roman = []
        for i in range(len(num)):
            while n >= num[i]:
                roman.append(sym[i])
                n -= num[i]
        result_list.append("".join(roman))
        
    return result_list

print(romanizer([1994, 2021, 58]))
