count = 0

def mergeSort(nlist):
    global count
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
                count = count + 1
            else:
                nlist[k]=righthalf[j]
                j=j+1
                count = count + 1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1
            count = count + 1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
            count = count + 1
    return count

# Driver code to test above
with open("10_Random.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
mergeSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("10_Reverse.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
mergeSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("10_Sorted.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
mergeSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("100_Random.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
mergeSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("100_Reverse.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
mergeSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("100_Sorted.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
mergeSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("1000_Random.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
mergeSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("1000_Reverse.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
mergeSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)

with open("1000_Sorted.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
mergeSort(content)
print ("Sorted array is:")
for i in range(len(content)):
    print ("%s" %content[i])
print ("Total number of comparisons: ", count)
