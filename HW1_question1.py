# sarit malayev 311397582
# question 1
def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    count=0
    for i in range(len(word)-1):
        if word[i]==word[i+1]:
            count=count+1
    if count==3:
        return True
    else:
        return False

print(trifeca('abbcc')) 
print(trifeca('aabbcc'))