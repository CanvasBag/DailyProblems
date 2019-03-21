# region Ex 1 - Retornar True se a soma de 2 numeros da lista dê o valor X

# --------------------------------------------------------------
# 1
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?
#
# --------------------------------------------------------------

def checkSum1(numbCheckSum, list):
    for idx, num1 in enumerate(list):
        for num2 in list[idx + 1:]:
            if int(num1) + int(num2) == numbCheckSum:
                return True
    return False

def checkSum2(numbCheckSum, list):
    resto = set()
    for num in list:
        if int(num) in resto:
            return True
        else:
            resto.add(numbCheckSum - int(num))



# numbString =input("Digite uma lista de números? ").split(', ')
# numbCheckSum = int(input("Digite o número a verificar? "))
# print(checkSum1(numbCheckSum, numbString))
# print(checkSum2(numbCheckSum, numbString))

# endregion

# region Ex 2 - Produto dos números duma lista excepto dele próprio
# --------------------------------------------------------------
# 2
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of
# all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
# [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?
#
# --------------------------------------------------------------

def product(inputList):
    productList = [1]*len(inputList)
    for targetIdx, num in enumerate(inputList):
        for productIdx, num2 in enumerate(productList):
            if targetIdx != productIdx:
                productList[productIdx] = num * num2
    return productList


def product2(inputList):
    # Generate prefix products
    prefix_products = []
    for num in inputList:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(inputList):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(inputList)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(inputList) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result

#inputList = [5, 4, 3, 2, 1]
#productList = product2(inputList)
#print(productList)

# endregion

# region Ex 3 - Binary Tree - (de)serialize

# --------------------------------------------------------------
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class Node:
#    def __init__(self, val, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'
# --------------------------------------------------------------


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self):
        stringNode = ""
        if self is None:
            return str(-1) + " "
        else:
            stringNode += self.val + " "
            stringNode += Node.serialize(self.left)
            stringNode += Node.serialize(self.right)
        return stringNode

    def deserialize(stringNode, idx=[0]):
        nodeTmp = None
        value = stringNode.split(' ')[idx[0]]
        if value == '-1':
            idx[0] = idx[0] + 1
            return
        else:
            idx[0] = idx[0] + 1
            nodeTmp = Node(value, Node.deserialize(stringNode, idx), Node.deserialize(stringNode, idx))
        return nodeTmp


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert Node.deserialize(Node.serialize(node)).left.left.val == 'left.left'

# endregion
