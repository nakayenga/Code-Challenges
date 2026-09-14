# merge two lists and return the head

list1 = [1,2,4]
list2 = [1,3,4]

def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append any remaining elements from list1 or list2
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list[0]

print(merge_sorted_lists(list1, list2))

def merge_sorted_lists_2(list1, list2):
    list3 = list1 + list2
    list3.sort()
    return list3[0]

print(merge_sorted_lists_2(list1, list2))
