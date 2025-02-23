class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in anagrams_dict:
                anagrams_dict[sorted_string] = [string]
            elif sorted_string in anagrams_dict:
                anagrams_dict[sorted_string].append(string)
        return list(anagrams_dict.values())

    # TC = O(m * nlogn) (m = no. of strings in strs list, n = length of longest string in strs list)
    # SC = O(m*n) (Dictionary storage; m = no. of strings, n = no. of characters in a string, each letter in a string takes space)
    
    
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            count = [0]*26
            for char in string:
                count[ord(char)-ord('a')] += 1
            res[tuple(count)].append(string)
            
        return list(res.values())
    
# URL - https://neetcode.io/problems/anagram-groups
        
            
