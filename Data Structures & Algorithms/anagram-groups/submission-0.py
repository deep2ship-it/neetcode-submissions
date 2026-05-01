from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            arr[key].append(word)

        return list(arr.values()) 

                    
        