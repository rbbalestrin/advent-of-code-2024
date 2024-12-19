rightList = []
leftList = []

def inputList(list1, list2):
    with open('input.txt', 'r') as file:
        for line in file:
            numbers = line.split()
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))
    print("Right List (Unsorted):", list2)
    print("Left List (Unsorted):", list1)

def sortList(lst):
    lst.sort()
    return lst

def findDif(list1, list2):
    total_distance = 0
    for i in range(len(list1)):
        distance = abs(list1[i] - list2[i])
        total_distance += distance
        print(f"Pair {i + 1}: {list1[i]} and {list2[i]}, Distance: {distance}")
    print(f"Total Distance: {total_distance}")
    return total_distance

inputList(rightList, leftList)

rightList = sortList(rightList)
leftList = sortList(leftList)

findDif(leftList, rightList)
