
#a
RowCount= 1 

while RowCount <=4 :
    ColumnCounter = 1
    while ColumnCounter <=2 : 
        print("*",end="")
        ColumnCounter += 1 
    print()
    RowCount += 1  

print()

#b
RowCount= 0

while RowCount <=3 :
    ColumnCounter1 = 1
    ColumnCounter2 = 1
    while ColumnCounter1 <=2-RowCount : 
        print("*",end="")
        ColumnCounter1 += 1 
    while RowCount>=2 and ColumnCounter2<=RowCount-1:
        print("*",end="")
        ColumnCounter2 += 1 
    print()
    RowCount += 1        

print()

#c
RowCount= 1 

while RowCount <=4 :
    ColumnCounter = 1
    while ColumnCounter <=RowCount : 
        print(RowCount,end="")
        ColumnCounter += 1 
    print()
    RowCount += 1  


print()
#d
RowCount= 1 

while RowCount <=4 :
    ColumnCounter = 1
    Counter = 1
    while ColumnCounter <=RowCount : 
        print(Counter,end="")
        Counter+=2
        ColumnCounter += 1 
    print()
    RowCount += 1
