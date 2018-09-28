# 面试题4 替换空格
#

def replaceBlank(string):
    if string == None :
        return False

    newString = string.replace(" ", "%20")

    return newString

if __name__=="__main__":

    string = "We are happy."
    result = replaceBlank(string)
    print(result)
