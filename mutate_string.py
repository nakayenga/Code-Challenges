def mutate_string(string, position, character):
    
    ls = list(string)
    ls[position] = character
    s = ''.join(ls)
    
    return s

print(mutate_string('abracadabra', 5, 'k')
