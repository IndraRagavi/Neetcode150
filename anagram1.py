from collections import defaultdict
strs = ["act","pots","tops","cat","stop","zat"]
print(strs)
lis = []
dic=defaultdict(list)
for i in range(0,len(strs)):
    #print(i,strs[i])
    sorte=(''.join(sorted(strs[i])))
    dic[sorte].append(strs[i])


print(list(dic.values()))

