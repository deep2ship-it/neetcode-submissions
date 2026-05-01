class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s))+  '#' + s )

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        decode = []

        i =0
        while i < len(s):
            j= i
            while s[j] != '#':
                j += 1
            le = int(s[i:j])
            i = j+1
                
            decode.append(s[i:i+le])
            i = i+le
        return decode




    
