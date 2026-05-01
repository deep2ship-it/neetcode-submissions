from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        annagrams = defaultdict(list)

        

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c)-ord('a')] += 1

            annagrams[tuple(count)].append(word)

        
        return list(annagrams.values())



        