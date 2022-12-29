'''
Set 2
2.1	Sorting
Write a Python program to sort a list of dictionaries using function. 
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
'''
from operator import itemgetter

dic_list= [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

#Method 1
def sortDicList1(DL):
    print(sorted(DL,key=itemgetter("model"),reverse=True))

#Method 2
def sortDicList2(D_L):
    l=[]
    finalList=[]
    for i in range(len(D_L)):
        l.append(D_L[i].get("model")) 
        l.sort(reverse=True) 

    for i in range(len(D_L)):
        for j in range(len(D_L)):
            if l[i]==D_L[j].get("model"):
                finalList.append(D_L[j])
    print(finalList)

# sortDicList1(dic_list)
sortDicList2(dic_list)