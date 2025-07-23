# 16. Check if two strings are isomorphic
def are_isomorphic(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

# 17. Check if a string contains only digits
def is_only_digits(s):
    return s.isdigit()

# 18. Find all substrings of a string
def all_substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

# 19. Find the most frequent character in a string
from collections import Counter
def most_frequent_char(s):
    count = Counter(s)
    return max(count, key=count.get)

# 20. Check if one string is a rotation of another
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in s1 + s1

# 21. Find the longest substring without repeating characters
def longest_unique_substring(s):
    start = max_len = 0
    used = {}
    for i, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        used[char] = i
        max_len = max(max_len, i - start + 1)
    return max_len

# 22. Basic string compression ("aabcc" → "a2b1c2")
def compress_string(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return ''.join(result)

# 23. Longest common prefix among list of strings
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# 24. Count all palindromic substrings in a string
def count_palindromic_substrings(s):
    def expand(l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
    return sum(expand(i, i) + expand(i, i+1) for i in range(len(s)))

# 25. Wildcard pattern matching with * and ?
def is_match(s, p):
    from fnmatch import fnmatch
    return fnmatch(s, p)

# 26. Minimum window substring that contains all characters of another string
from collections import Counter
def min_window(s, t):
    if not s or not t:
        return ""
    t_count = Counter(t)
    window = {}
    have = need = 0
    res = [0, float('inf')]
    l = 0
    for r, c in enumerate(s):
        window[c] = window.get(c, 0) + 1
        if c in t_count and window[c] == t_count[c]:
            have += 1
        while have == len(t_count):
            if (r - l) < (res[1] - res[0]):
                res = [l, r]
            window[s[l]] -= 1
            if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l:r+1] if res[1] != float('inf') else ""

# 27. Valid palindrome after removing at most one character
def valid_palindrome(s):
    def is_palin(x): return x == x[::-1]
    for i in range(len(s) // 2):
        if s[i] != s[-1 - i]:
            return is_palin(s[i+1:len(s)-i]) or is_palin(s[i:len(s)-1-i])
    return True

# 28. Implement strstr (first occurrence of substring in another)
def strstr(haystack, needle):
    return haystack.find(needle)

# 29. Decode a run-length encoded string (e.g., "a2b1c2" → "aabcc")
def decode_rle(s):
    result = ""
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        num = ""
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        result += char * int(num)
    return result

# 30. All permutations of a string
from itertools import permutations
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]