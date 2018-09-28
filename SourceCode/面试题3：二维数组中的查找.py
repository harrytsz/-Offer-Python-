#二维数组中的查找

def findNumber(array, number):
    for rows in array:
        for item in rows:
            if number == item:
                return True
    return False


if __name__=="__main__":

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]

    # number = 7 # This Array Contain This Number!!
    number = 5 # There Is No This Number!!

    result = findNumber(array, number)

    if result == True:
        print("This Array Contain This Number!!")
    else:
        print("There Is No This Number!!")
