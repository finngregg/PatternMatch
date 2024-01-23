def match(pattern, word):
    if len(pattern) == 0 or len(word) == 0: 
        return False
    if "?" in pattern:
        if len(pattern) != len(word): 
            return False    
        if pattern[0]==word[0] or pattern[0]=="?": 
            return True        
        if pattern[0] != "?":
            if pattern[0] != word[0]:
                return match(pattern[1:], word[1:])        
    else:
        if "*" in pattern:
            if pattern == "*" and word == "" or word == word[::]:
                return True
            if len(pattern) != len(word):
                pat = pattern.split("*")
                if all(pat) in word:
                    return True
            else:
                if pattern[0]==word[0] or pattern[0]=="*":
                    return True 
                if pattern[0] != "*":
                    if pattern[0] != word[0]:
                        return match(pattern[1:], word[1:])                
                
