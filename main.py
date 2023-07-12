n = int(input())
arr = list(map(int, input().split())) #Convert space-separated input values to a list of integers
nlist = []
for x in arr:
    if x not in nlist: #use to find duplicate
        nlist.append(x)

nlist.sort(reverse=True) #sort in descending order
print(nlist[1]) #print the runnerup score




