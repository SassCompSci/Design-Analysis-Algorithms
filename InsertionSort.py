# Python program for implementation of Insertion Sort

# Function to do insertion sort
count = 0
def insertionSort(arr):
        
    # Traverse through 1 to len(arr)
    global count
    for i in range(1, len(arr)):

        key = arr[i]
        
        # Move elements of arr[0..i-1], that are
	# greater than key, to one position ahead
	# of their current position
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
            count = count + 1
        arr[j+1] = key
    return count


# Driver code to test above
with open("10_Random.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
insertionSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("10_Reverse.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
insertionSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("10_Sorted.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
insertionSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("100_Random.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
insertionSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("100_Reverse.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
insertionSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("100_Sorted.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
insertionSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("1000_Random.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
insertionSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("1000_Reverse.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
insertionSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("1000_Sorted.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
insertionSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)
