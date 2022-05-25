# student name: Mitchell Kok
# student number: 44572246

import threading

def sortingWorker(firstHalf: bool) -> None:
    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """
    
    # initialize working array to appropriate half of the testcase list
    if firstHalf == True:
        working_arr = testcase[:(len(testcase)//2)]
    else:
        working_arr = testcase[(len(testcase)//2):]

    # bubble sort algorithm for working array
    for i in range(len(working_arr) - 1):
        for j in range(len(working_arr) - i - 1):
            if working_arr[j] > working_arr[j + 1]:
                tmp = working_arr[j]
                working_arr[j] = working_arr[j+1]
                working_arr[j+1] = tmp

    # store working array to corresponding list
    if firstHalf == True:
        global sortedFirstHalf
        sortedFirstHalf = working_arr
    else:
        global sortedSecondHalf
        sortedSecondHalf = working_arr



def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """
    first_cnt = second_cnt = 0  # counters to keep track of position in half lists
    while first_cnt < len(sortedFirstHalf) and second_cnt < len(sortedSecondHalf):
        # Put the smaller number into the full list first
        if sortedFirstHalf[first_cnt] < sortedSecondHalf[second_cnt]:
            SortedFullList.append(sortedFirstHalf[first_cnt])
            first_cnt += 1
        else:
            SortedFullList.append(sortedSecondHalf[second_cnt])
            second_cnt += 1

    # place any remaining items in first list
    while first_cnt < len(sortedFirstHalf):
        SortedFullList.append(sortedFirstHalf[first_cnt])
        first_cnt += 1

    # place any remaining items in second list
    while second_cnt < len(sortedSecondHalf):
        SortedFullList.append(sortedSecondHalf[second_cnt])
        second_cnt += 1  


if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,3,2]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #to implement the rest of the code below, as specified 

    # create threads
    sorting_thread1 = threading.Thread(target=sortingWorker, args=(True, ))
    sorting_thread2 = threading.Thread(target=sortingWorker, args=(False, ))
    merging_thread = threading.Thread(target=mergingWorker)

    # start sorting threads
    sorting_thread1.start()
    sorting_thread2.start()
    
    # join sorting threads
    sorting_thread1.join()
    sorting_thread2.join()

    # start merging thread
    merging_thread.start()
    merging_thread.join()

    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)