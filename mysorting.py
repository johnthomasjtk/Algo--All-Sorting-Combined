#Algorithms Sorting Code - Padmamala Mam.

import random
import time			        #Header Files

#Bubble Sort

def bubbleSort(aList):					#Defining Bubble Sort
    exchanges=True                      		#Bubble Sort is the simplest sorting algorithm that works by repeatedly 							swapping the adjacent elements if they are in wrong order.
    passnum=len(aList)-1
    while passnum > 0 and exchanges:
        exchanges=False					#Best Case Time Complexity: O(n). Best case occurs when array is already 								sorted.
        for i in range(passnum):
            if aList[i] > aList[i + 1]:		
                exchanges=True
                temp = aList[i]
                aList[i] = aList[i + 1]
                aList[i + 1] = temp
                
#Selection Sort

def selectionSort(aList):				#Defining Selection Sort
    for fillslot in range(len(aList) - 1, 0, -1):	#The selection sort algorithm sorts an array by repeatedly finding the 								minimum element (considering ascending order) from unsorted part and 								putting it at the beginning. The algorithm maintains two subarrays in 								given array.
        positionOfMax = 0
        for location in range(1, fillslot + 1):	
            if aList[location] > aList[positionOfMax]:	#In every iteration of selection sort, the minimum element (considering 							ascending order) from the unsorted subarray is picked and moved to the 								sorted subarray. 
                positionOfMax = location
        temp = aList[fillslot]				#Time Complexity: O(n2) as there are two nested loops.
        aList[fillslot] = aList[positionOfMax]
        aList[positionOfMax] = temp

#Insertion Sort

def insertionSort(aList):				#Defining Insertion Sort
    for index in range(1, len(aList)):			#Time Complexity: O(n*2) 
        currentValue = aList[index]
        position = index
        while position > 0 and aList[position - 1] > currentValue:
            aList[position] = aList[position - 1]
            position = position - 1
        aList[position] = currentValue

#Heap Sort	
			
def heapSort(a):  					#Defining Heap Sort
 def sift(start, count):  				#Time Complexity: Time complexity of heapify is O(Logn). Time complexity 								of createAndBuildHeap() is O(n) and overall time complexity of Heap Sort 								is O(nLogn).
   	root = start  
      
        while root * 2 + 1 < count:  
             child = root * 2 + 1  
             if child < count - 1 and a[child] < a[child + 1]:  
                child += 1  
             if a[root] < a[child]:  
                a[root], a[child] = a[child], a[root]  
                root = child  
             else:  
       		  return 

 
 
 count = len(a)  
 start = count / 2 - 1    #Moving to Next position in the list
 end = count - 1  
      

 while start >= 0:  
            sift(start, count)  
            start -= 1  
      
 while end > 0:  
            a[end], a[0] = a[0], a[end]  
            sift(0, end)  
            end -= 1  


def createList(size): #Creates a list of random numbers
    lyst = []
    temp = []
    while len(lyst) < size: #For how many numbers in list
        num = random.randint(1, 1000)# Random Numbers between 1 and 1000 
        lyst.append(num)
    return lyst

def printList(lyst):		#Function for Printing List
    count = 0
    for num in lyst:
        print("%6d" % num, end == "")
        count += 1
        if count == 10:
            count = 0
            print()

def main():
    print("Creating List....") # Creating a list of Hundred Numbers
    lyst = createList(100)
    lyst_A=list(lyst)
    lyst_B=list(lyst)


 

                      #--------------------------Sorting---------------------------------->
                      
                      

    print("----------Different Sorting Methods -----------") #Printing all sorting With time taken for sorting.

    print("\n----------Bubble Sorting----------")
    StartTime=time.time()
    print("\n100 List Bubble Sorting......>")
    bubbleSort(lyst)
    print("Bubble Sorting DONE!")
    endTime=(time.time()-StartTime)
    print("End Time: ",endTime)

    print("\n----------Selection Sorting---------------->")
    StartTime=time.time()
    print("\n 100 List Selection Sorting......>")
    selectionSort(lyst_A)
    print("Selection Sorting DONE!")
    endTime=(time.time()-StartTime)
    print("End Time: ",endTime)

    print("\n----------Insertion Sorting---------------->")
    StartTime=time.time()
    print("\n 100 List Insertion Sorting......>")
    insertionSort(lyst_B)
    print("Insertion Sorting DONE!")
    endTime=(time.time()-StartTime)
    print("End Time: ",endTime)
  
    print("\n----------Heap Sorting---------------->")
    StartTime=time.time()
    print("\n 100 List Heap Sorting......>")
    heapSort(lyst_B)
    print("Heap Sorting DONE!")
    endTime=(time.time()-StartTime)
    print("End Time: ",endTime)

     
main()


