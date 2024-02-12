#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    word = word.replace(" ", "")
    if not word:
        return False 
    return word == word[::-1]
    

if __name__ == '__main__': 
    #REMOVE PASS AND YOUR CODE GOES HERE
    word = input()
    print(palindrome(word))
