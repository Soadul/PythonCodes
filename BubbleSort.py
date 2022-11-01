#!/usr/bin/env python
# coding: utf-8

# In[34]:


# Bubble sort in Python

def bubSort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                temp = array[j]
                array[j]=array[j+1]
                array[j+1]=temp
                     
array=[4546,45,878,34,3435,33,32,2];
'''
print("Enter Array Size")
size = int(input())

for x in range(0,size):
    print("Enter", x ,"th Value in Array" )
    l=input();
    array.append(l)
'''
print("Array:")
print(array)
print("Sorting Started: ")
bubSort(array)

print('Sorted Array in Ascending Order:')
print(array)
for x in range(0,len(array)):
    print(x,"th element is: ",array[x])
bubSort(array)


# In[ ]:




