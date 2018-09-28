#数组中重复的数字 Edition3
# in []

def duplicate(numbers, length, duplication):
    if numbers == None or length <= 0:
        return False

    for item in numbers:
        if item < 0 or item > length - 1:
            return False

    container = []
    for i in range(length):
        if numbers[i] in container:
            duplication.append(numbers[i])
        else:
            container.append(numbers[i])

    return duplication

if __name__=="__main__":
    numbers = [2, 3, 1, 0, 2, 5, 3]
    length = 7
    duplication = []

    result = duplicate(numbers, length, duplication)

    if result != None:
        print(duplication)
    else:
        print("No Duplicate Elements!!!")

