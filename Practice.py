class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

    def __str__(self):
        return self.data

class LinkedLists:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(str(node) for node in nodes)

def mergeLinkedLists(arr1, arr2):
    arr1_list = []
    for i in arr1:
        arr1_list.append(i)

    arr2_list = []
    for j in arr2:
        arr2_list.append(j)

    arr3_list = []
    i = 0
    j = 0
    while i < len(arr1_list) and j < len(arr2_list):
        if int(arr1_list[i]) < int(arr2_list[j]):
            arr3_list.append(arr1_list[i])
            i += 1
        else:
            arr3_list.append(arr2_list[j])
            j += 1

    while i < len(arr1_list):
        arr3_list.append(arr1_list[i])
        i += 1

    while j < len(arr2_list):
        arr3_list.append(arr2_list[j])
        j += 1

    new_linkedlist = LinkedLists(arr3_list)
    return new_linkedlist

# llst = LinkedLists(["1", "2", "5", "10"])
# llst2 = LinkedLists(["1", "3", "7", "9"])

llst = LinkedLists([1, 2, 5, 10])
llst2 = LinkedLists([1, 3, 7, 9])

print(llst)
print(llst2)
print(mergeLinkedLists(llst, llst2))

