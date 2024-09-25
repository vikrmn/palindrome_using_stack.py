def ispalindrome(string):
    stack = []
    for char in string:
        stack.append(char)
        if(char != stack.pop()):
            return False
    return True    

if __name__ == "__main__":
    string = input("enter the string : ").lower()

    result = ispalindrome(string)
    if(result):
        print("The given string is palindrome")
    else:
        print("The given string is not palindrome")    
