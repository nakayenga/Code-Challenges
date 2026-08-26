if __name__ == '__main__':
    students = []
    
    # Read number of students
    n = int(input())
    
    # Populate the nested list
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Find the second lowest grade using set to remove duplicates
    scores = sorted(list(set(student[1] for student in students)))
    second_lowest_score = scores[1]
    
    # Extract names of students with the second lowest grade
    names = [student[0] for student in students if student[1] == second_lowest_score]
    
    # Sort names alphabetically and print each on a new line
    names.sort()
    for name in names:
        print(name)
