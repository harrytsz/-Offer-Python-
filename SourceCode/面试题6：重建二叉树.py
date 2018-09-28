# 面试题6：重建二叉树
class Node(object):
    def __init__(self, left, right, value):
        self.left = left
        self.right = right  # columns 取值范围：(1 - 2^i)
        self.value = value

    def __init__(self,value):
        self.value = value

def ConstructBinaryTree( prearr, midarr):
    if prearr == None or midarr == None:
        return None

    pymap = {}

    for i in range(len(midarr)):
        pymap.update({midarr[i]:i})
        # name = midarr[i]
        # value = i
        # temp = {name:value}
        # pymap.update(temp)

    return PreMid(prearr, 0, len(prearr)-1, midarr, 0, len(midarr)-1, pymap)

def PreMid(prearr, prei, prej, midarr, midi, midj, pymap):
    if prei > prej:
        return None
    head = Node(prearr[prei])
    index = pymap.get(prearr[prei])
    head.left = PreMid(prearr, prei + 1, prei + index - midi, midarr, midi, index - 1, pymap)
    head.right = PreMid(prearr, prei + index - midi + 1, prej, midarr, index + 1, midj, pymap)
    return head

def PrintFromTopToBottom(root):
    queue = []
    result = []
    if root == None:
        return result

    queue.append(root)
    while queue:
        newNode = queue.pop(0)
        result.append(newNode.value)
        if newNode.left != None:
            queue.append(newNode.left)
        if newNode.right != None:
            queue.append(newNode.right)
    return result


if __name__=="__main__":
    prearr = [1,2,4,7,3,5,6,8]
    midarr = [4,7,2,1,5,3,8,6]
    result = ConstructBinaryTree(prearr, midarr)
    re = PrintFromTopToBottom(result)
    print(re)