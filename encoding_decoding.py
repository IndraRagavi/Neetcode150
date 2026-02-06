from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        strn = []
        for i in strs:
            strn.append(str(len(i))+'%'+i)
        return ''.join(strn)

    def decode(self, s: str) -> List[str]:
        res_dec = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '%':
                j+=1
            leng = int(s[i:j])
            j+=1
            res_dec.append(s[j:j+leng])
            i=j+leng
        return res_dec


arr =['Hello,jan', '', 'World']
sol = Solution()
encod = sol.encode(arr)
decod = sol.decode(encod)
print(encod,decod,sep='\n')
print(encod)
print(decod)