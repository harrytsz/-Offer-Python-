#Edition 2
# Array Sort

def duplicate(numbers, length, duplication):
    if numbers == None or length <= 0:
        return False
    for item in numbers:
        if item < 0 or item > length - 1:
            return False

    numbers.sort()

    for i in range(length-1):
        if numbers[i] == numbers[i+1]:
            duplication.append(numbers[i])
    return duplication


if __name__=="__main__":
    numbers = [2, 3, 1, 0, 2, 5, 3]
    length = 7
    duplication = []

    result = duplicate(numbers, length, duplication)

    if result != None:
        print("Duplicate Elements are: ",duplication)
    else:
        print("NO duplicate Element!!!")
