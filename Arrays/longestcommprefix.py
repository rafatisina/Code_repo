class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        res=strs[0]
        for k in range(1,len(strs)):
            s1=list(res)
            s2=list(strs[k])
            i=0
            n=min(len(s1),len(s2))
            while i<= (n-1):
                if s1[i] != s2[i]:
                        break
                i+=1
            res=''.join(s1[:i])
        return res

       
