def duplicate(numbers, length, duplication):
    if numbers == None or length <= 0:
        return False
    for item in numbers:
        if item < 0 or item > length - 1:
            return False
    for i in range(length):
        while numbers[i] != i:
            if numbers[i] == numbers[numbers[i]]:
                duplication.append(i)
                break
            else:
               temp = numbers[i]
               numbers[i] = numbers[temp]
               numbers[temp] = temp
    return duplication

if __name__=="__main__":
    numbers = [2, 3, 1, 0, 4, 5, 2]
    length = 7
    duplication = []
    duplication = duplicate( numbers, length, duplication)

    if len(duplication) != 0:
        print(duplication)
    else:
        print("No duplication elements!")
