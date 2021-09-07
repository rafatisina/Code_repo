class Solution:
    def reverseWords(self, s: str) -> str:
        d,word=deque(),[]
        left=0
        right=len(s)-1
        while left <= right:
            if s[left]==' 'and word:
                d.append(''.join(word[::-1]))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left+=1

        d.append(''.join(word[::-1]))

        return ' '.join(d)


        
