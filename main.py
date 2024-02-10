#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    word = word.replace(" ", "")
    if not word:
        return False 
    if word == word[::-1]:
        return True

if __name__ == '__main__': 
    #REMOVE PASS AND YOUR CODE GOES HERE
    word = input()
    print(palindrome)
