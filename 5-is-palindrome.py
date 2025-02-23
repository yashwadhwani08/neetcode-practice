class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        str_alphanumeric = ""

        for char in s_lower:
            if char.isalnum():
                str_alphanumeric += char
            else:
                continue

        i, j = 0, len(str_alphanumeric) - 1

        while i < j:
            if str_alphanumeric[i] == str_alphanumeric[j]:
                i += 1
                j -= 1
                continue
            return False
        else:
            return True

    # TC - O(n)
    # SC - O(n) - storing alphanumeric characters in a string
    """
    To further reduce the space complexity, increment left pointer only when at left, 
    non-aplhanumeric charcater found, decrement right pointer only when at right, non-alphanumeric
    charcter found. Compare directly with lower() method (s[i].lower() == s[j].lower()) in
    while instead of creating another string with all lower case characters
    """


# URL - https://neetcode.io/problems/is-palindrome
