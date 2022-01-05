def findSmallest(x):
    """
    Find the smallest value in a list/array and return it's index location
    """
    smallest=x[0]
    smallest_index=0
    for i in range(1,len(x)):
        if x[i] < smallest:
            smallest=x[i]
            smallest_index=i
    return smallest_index

def selectionSort(x):
    """
    For a given list/array, find the smallest value in the list, add it to a new array and remove it from the original list
    """
    newArr=[]
    for i in range(len(x)):
        smallest = findSmallest(x)
        newArr.append(x.pop(smallest))
    return newArr