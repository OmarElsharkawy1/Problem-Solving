def mergeTwoLists(list1, list2):
    sortedList = []
    if list1 and list2 == []:
        sortedList = []
        return sortedList
    elif list1 == []:
        sortedList = list2
        return sortedList
    elif list2 == []:
        sortedList = list1
        return sortedList
    
    
    for i in list1:
        for n in list2:
            if i > n:
                sortedList.append(n)
                sortedList.append(i)
                list2.remove(list2[0])
                break
            elif i == n:
                sortedList.append(i)
                sortedList.append(n)  
                list2.remove(list2[0])
                break  
            else:
                sortedList.append(i) 
                sortedList.append(n)
                list2.remove(list2[0])
                break
    
        return sortedList

list1 = [1]
list2 = [1]
print ("-----------------")
print (mergeTwoLists(list1= list1, list2=list2))