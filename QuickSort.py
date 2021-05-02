# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot

count = 0

def partition(arr,low,high):
    global count
    i = ( low-1 )		 # index of smaller element
    pivot = arr[high]	 # pivot

    for j in range(low , high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
		
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            count = count + 1

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
    return count

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def quickSort(arr,low,high):
	if low < high:

		# pi is partitioning index, arr[p] is now
		# at right place
		pi = partition(arr,low,high)

		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

# Driver code to test above
with open("10_Random.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
n = len(content)
quickSort(content,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("10_Reverse.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
n = len(content)
quickSort(content,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("10_Sorted.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
n = len(content)
quickSort(content,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("100_Random.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
n = len(content)
quickSort(content,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("100_Reverse.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
n = len(content)
quickSort(content,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("100_Sorted.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
n = len(content)
quickSort(content,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("1000_Random.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
n = len(content)
quickSort(content,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("1000_Reverse.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
n = len(content)
quickSort(content,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("1000_Sorted.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
n = len(content)
quickSort(content,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)
