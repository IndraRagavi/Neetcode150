from collections import Counter
nums = [1,2,2,3,3,3]
k = 2

def kfrq(nums,k):
    frq_no=[key for key,count in Counter(nums).most_common(k)]
    return frq_no

kfrqncy = kfrq(nums,k)
print(kfrqncy)