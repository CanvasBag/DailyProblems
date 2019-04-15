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

# region Ex 2 - Array - Produto dos números duma lista excepto dele próprio
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

# region Ex 4 - Array - lowest positive integer

# --------------------------------------------------------------
# This problem was asked by Stripe.
#
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other
# words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and
# negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.
# --------------------------------------------------------------

def first_missing_positive(nums):
    if not nums:
        return 1
    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            if nums[i] == nums[v - 1]:
                break
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1

def first_missing_positive_set(nums):
    s = set(nums)
    i = 1
    while i in s:
        i += 1
    return i

#print(first_missing_positive([1, 3, 5, 2, 8]))
#print(first_missing_positive([3,4,-1,1]))

# endregion

# region - How To Solve a Hard Programming Interview Question

# endregion

# region Ex 5 - Lambda - Implement Cons Class

# --------------------------------------------------------------
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
#
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
#
# Implement car and cdr.
#
# --------------------------------------------------------------


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    return pair(lambda a, b: a)


def cdr(pair):
    return pair(lambda a, b: b)

#print(car(cons(3, 4)))
#print(cdr(cons(3, 4)))

# endregion

#region Ex 6 - XOR Linked List

# --------------------------------------------------------------
# An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields,
# it holds a field named both, which is an XOR of the next node and the previous node.
#
# Implement an XOR linked list;
# it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
#
# If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and
# dereference_pointer functions that converts between nodes and memory addresses.
#
# --------------------------------------------------------------

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        return

    def has_value(self, value):
        if self.value == value:
            return True
        else:
            return False

class LinkedXorList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        if not isinstance(item, Node):
            item = Node(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

    def get(self, idx):
