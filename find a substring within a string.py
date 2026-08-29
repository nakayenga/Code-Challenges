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
