list = [1, 1, 2, 2, 3, 3, 3, 4]
def remove_duplicates(list):
    result = []
    for i in list:
        if i not in list:
            result.append(i)
        return result
print(remove_duplicates(list))