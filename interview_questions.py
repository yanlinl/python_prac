'''
    Question 1
    Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.
'''
def question1(s, t):
    new_dict = {}
    # Create an dictionaly this takes O(N)
    # I could use a list, but it will make the search takes longer
    for char in s:
        if char not in new_dict:
            new_dict[char] = 0

    # check each char see if it is in the dictionary
    for char in t:
        if char not in new_dict:
            return False
    return True


'''
    Question 2
    Given a string a, find the longest palindromic substring contained in a.
    Your function definition should look like question2(a), and return a 
    string.
'''
def getPalidrom(a, pre, post):
    size = len(a)

    # do not step out of array size. Do it until the left size and the right
    # side no longer equal to each other.
    while pre > 0 and post < size and a[pre] == a[post]:
        pre = pre - 1
        post = post + 1
    return a[pre:post]

def question2(a):
    # get the size of string
    size = len(a)
    # variable that stores longest palidrom
    curLongest = ""
    curLongestSize = 0
    for i in range(0, size-1):
        # odd size palidrom
        palindrom = getPalidrom(a, i, i)
        # even size palidrom
        if a[i] == a[i+1]:
            palindrom2 = getPalidrom(a, i, i+1)
            # id even size palidrom is larger than odd palidrom
            if len(palindrom2) > len(palindrom):
                palindrom = palindrom2

        # update longest palidrom if it is larger
        if len(palindrom) > curLongestSize:
            curLongestSize = len(palindrom)
            curLongest = palindrom
    return curLongest


'''
    Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:

        {'A': [('B', 2)],
         'B': [('A', 2), ('C', 5)], 
         'C': [('B', 5)]}
        {
        'A':[('F', 2),('B',4)],
        'F':[('A',2), ('B',5),('C',1),('E',4)],
        'E':[('F',4), ('D',2) ],
        'D':[('E',2),('C',3)],
        'C':[('D',3),('F',1),('B',6)],
        'B':[('A',4),('F',5),('C',6)]
         }
    Vertices are represented as unique strings. The function definition should be question3(G)
'''
def question3(G):
    # This function uses Kruskal's algorithm to find MST for the graph
    mst = {}
    vertaxSet = []
    edges = getEdges(G)

    for i in range(0, len(edges)):
        first = [edges[i][0]]
        firstIndex = -1
        second = [edges[i][1]]
        secondIndex = -1
        new = []
        for k in range(0, len(vertaxSet)):
            if edges[i][0] in vertaxSet[k]:
                first = vertaxSet[k]
                firstIndex = k
            if edges[i][1] in vertaxSet[k]:
                second = vertaxSet[k]
                secondIndex = k

        if firstIndex == -1 and secondIndex == -1:
            # if both vertax is not in the set
            new = first + second
            vertaxSet.append(new)
            addEdge(mst, edges[i])
        elif firstIndex != secondIndex:
            # if two vertaices are in different set
            new = first + second
            if first in vertaxSet:
                vertaxSet.remove(first)
            if second in vertaxSet:
                vertaxSet.remove(second)
            vertaxSet.append(new)
            addEdge(mst, edges[i])
        else:
            # do nothing if they are in the same set
            pass
    print mst

def getEdges(graph):
    data =[]
    for vertax in graph:
        for edge in graph[vertax]:
            # add unique edges
            if (vertax, edge[0], edge[1]) not in data and (edge[0], vertax, edge[1]) not in data:
                data.append((vertax, edge[0], edge[1]))
    # sort edges by weight
    data.sort(key=lambda x:x[2])
    return data

def addEdge(mst, edge):
    if edge[0] not in mst:
        # initialize list if it is not created
        mst[edge[0]] = [(edge[1], edge[2])]
    else:
        # append to the list
        mst[edge[0]].append((edge[1], edge[2]))

    if edge[1] not in mst:
        # initialize list if it is not created
        mst[edge[1]] = [(edge[0], edge[2])]
    else:
        # append to the list
        mst[edge[1]].append((edge[0], edge[2]))

'''
    Find the least common ancestor between two nodes on a binary search tree.
    The least common ancestor is the farthest node from the root that is an
    ancestor of both nodes. For example, the root is a common ancestor of all
    nodes on the tree, but if both nodes are descendents of the root's left
    child, then that left child might be the lowest common ancestor. You can
    assume that both nodes are in the tree, and the tree itself adheres to all
    BST properties. The function definition should look like question4(T, r,
    n1, n2), where T is the tree represented as a matrix, where the index of
    the list is equal to the integer stored in that node and a 1 represents a
    child node, r is a non-negative integer representing the root, and n1 and
    n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be

    question4([[0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [1, 0, 0, 0, 1],
               [0, 0, 0, 0, 0]],
              3,
              1,
              4)
    and the answer would be 3.
'''

'''
    I do not under stand the input of this questions. A binary search tree 
    have 2 childern. But the each list have 5 elements. For instance first item in the list have one child node. Does it say if it is left child or
    right? child? Why there are 5 elemets in the list?
'''

'''
    Question 5 Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def getLlSize(ll):
    # if ll is none
    if ll == None:
        return 0

    size = 1
    curNode = ll
    while curNode.next != None:
        # increment the size
        size = size + 1
    return size

def getMth(ll, m):
    temp = m
    curNode = ll
    while m > 0:
        m = m - 1
        curNode = ll.next
    return curNode

def question5(ll, m):
    llSize = getLlSize(ll)
    if llSize < m:
        raise ValueError("Linked list size is smaller than m. llSize=", llSize, " and m = ", m)
    fromHead = llSize - m + 1
    return getMth( ll, fromHead )









