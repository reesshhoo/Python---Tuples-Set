alpha = ['x','y','z']
nlst=[2,3,4]
nlst2 = [2,3,4,5]
lst1 = []
lst2 = []
lst3 = []
lst4 = []
lst5 = []


#First list
for i in alpha:
    for j in range(1,5):
        lst2.append(i*j)
print(lst1)


#Second List
for i in range(1,5):
    for j in alpha:
        lst2.append(j*i)
print(lst2)


#Third List
while nlst[2]<7:
    for i in range(len(nlst)):
        lst3.append([nlst[i]])
        nlst[i] = nlst[i] + 1
print(lst3)


#Fourth List
while nlst2[3]<9:
    lst4.append(nlst2[::])
    for j in range(len(nlst2)):
        nlst2[j] = nlst2[j] + 1
    
print(lst4)



#Fifth List
for i in range(1,4):
    for j in range(1,4):
        lst5.append((j,i))
print(lst5)