def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-2):
        ls = []
        ls = ls + [string[i], string[i+1], string[i+2]]
        if sub_string == ''.join(ls):
            count+=1
        else:
            continue
            
    return count

print(count_substring('ABCDCDC', 'CDC')) # Output: 2


# accounts for all test cases
def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)
    
    for i in range(len(string) - sub_len + 1):
        if string[i : i + sub_len] == sub_string:
            count += 1
            
    return count

print(count_substring('ABCDCDC', 'CDC')) # Output: 2
