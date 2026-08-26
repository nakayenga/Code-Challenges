# Version 1 (Optimal Solution):
def minimalOperations(words):
    results = []
    
    for word in words:
        replacements = 0
        i = 0
        n = len(word)
        
        while i < n:
            run_length = 1
            # Count the length of identical adjacent characters
            while i + 1 < n and word[i] == word[i + 1]:
                run_length += 1
                i += 1
            
            # Add floor(run_length / 2) replacements for this block
            replacements += run_length // 2
            i += 1
            
        results.append(replacements)
        
    return results

# Example Usage:
words = ["ab", "aab", "abbba", "aaaaaaaa"]
print(minimalOperations(words))  # Output: [0, 1, 1, 4]

# Version 2 (Single-Pass Greedy Solution):
def minimalOperations(words):
    results = []
    
    for word in words:
        replacements = 0
        i = 1
        
        while i < len(word):
            # If current character matches the previous one
            if word[i] == word[i - 1]:
                replacements += 1
                # Greedy choice: "Replace" word[i] with a unique wildcard.
                # Moving forward by 2 skips the replaced character entirely.
                i += 2
            else:
                i += 1
                
        results.append(replacements)
        
    return results

# Example Usage
words = ["ab", "aab", "abbba", "aaaaaaaa"]
print(minimalOperations(words))  # Output: [0, 1, 1, 4]

#Version 3 (Dynamic Programming)
def minimalOperations(words):
    results = []
    
    for word in words:
        # prev_same: cost if we do NOT change word[i]
        # prev_diff: cost if we DO change word[i]
        prev_same = 0
        prev_diff = 1
        
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                # If current matches previous:
                # - To KEEP word[i], the previous character MUST have been changed.
                # - To CHANGE word[i], previous could be unchanged or changed (take min).
                curr_same = prev_diff
                curr_diff = min(prev_same, prev_diff) + 1
            else:
                # If current differs from previous:
                # - To KEEP word[i], previous could be unchanged or changed.
                # - To CHANGE word[i], previous could be unchanged or changed.
                curr_same = min(prev_same, prev_diff)
                curr_diff = min(prev_same, prev_diff) + 1
                
            prev_same, prev_diff = curr_same, curr_diff
            
        results.append(min(prev_same, prev_diff))
        
    return results

# Example Usage
words = ["ab", "aab", "abbba", "aaaaaaaa"]
print(minimalOperations(words))  # Output: [0, 1, 1, 4]
