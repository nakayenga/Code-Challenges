# IBM Python Interview Question

def count_rearranged_valleys(data: list) -> int:
    """
    Rearranges an input list by alternating small and large numbers, 
    places the top two largest numbers at the ends, and counts 'valleys'
    (elements strictly smaller than both neighbors).
    """
    # 1. Sort the incoming list in place
    data.sort()

    # 2. Create a copy to manipulate
    list_copy = data.copy()

    # 3. Identify and isolate the largest and second-largest numbers
    largest = sorted(list_copy)[-1]
    second_largest = sorted(list_copy)[-2]

    # 4. Remove them from the working copy
    list_copy.remove(largest)
    list_copy.remove(second_largest)

    # 5. Build the alternating list (min, max, min, max...)
    new_list = []
    while list_copy:
        current_min = min(list_copy)
        new_list.append(current_min)
        list_copy.remove(current_min)
        
        if list_copy:
            current_max = max(list_copy)
            new_list.append(current_max)
            list_copy.remove(current_max)

    # 6. Place the two largest numbers at the absolute start and end
    new_list.insert(0, second_largest)
    new_list.append(largest)

    # 7. Count elements that are smaller than both neighbors
    count = 0
    for i in range(1, len(new_list) - 1):
        if new_list[i] < new_list[i - 1] and new_list[i] < new_list[i + 1]:
            count += 1

    return count

initial_numbers = [5, 9, 3, 7, 2, 1, 8, 4, 6, 0]
result = count_rearranged_valleys(initial_numbers)
print(f"Total valleys found: {result}")
