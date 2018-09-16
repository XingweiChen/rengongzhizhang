from collections import deque
def BFS(name, data_dict, value):
    search_queue = deque()
    search_queue += data_dict[name]
    searched = []
    while len(search_queue) != 0:
        current = search_queue.popleft()
        if current not in searched:
            if current == value:
                return True
            else:
                search_queue += data_dict[current]
                search_queue.append(current)
    return False

def DFS(name, data_dict, value):
    search_queue = deque()
    search_queue += data_dict[name]
    searched = []
    while len(search_queue) != 0:
        current = search_queue.pop()
        if current not in searched:
            if current == value:
                return True
            else:
                search_queue += data_dict[current]
                search_queue.append(current)
    return False

def Binary_Search(start, end, value, array):
    if value >= array[-1]:
        return len(array)-1
    elif value <= array[0]:
        return 0
    while True:
        mid = (end + start)//2
        if array[mid] == value:
            return mid
        elif end - start == 1:
            return start
        elif array[mid] > value:
            end = mid
        elif array[mid] < value:
            start = mid

def MergeSort(array):
    if len(array) == 1 or len(array) == 0:
        return array
    else:
        mid = len(array)//2
        left = MergeSort(array[0:mid])
        right = MergeSort(array[mid:])
        new_array = []
        while len(left) and len(right):
            if left[0] <= right[0]:
                new_array.append(left[0])
                left = left[1:]
            elif left[0] > right[0]:
                new_array.append(right[0])
                right = right[1:]
        new_array.extend(left); new_array.extend(right)
        return new_array
