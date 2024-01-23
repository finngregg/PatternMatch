def match(pattern, word):
    if len(pattern) == 0 or len(word) == 0: 
        return False
    if pattern[0]==word[0] or pattern[0]=="?": 
        return True 
    if len(pattern) != len(word): 
        return False        
    if pattern[0] != "?":
        if pattern[0] != word[0]:
            return match(pattern[1:], word[1:])