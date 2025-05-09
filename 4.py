def LongestWordLength(s):
    n = len(s)
    res = 0
    curr_len = 0
    longest = ""
    for i in range(0, n):
        if s[i] != ' ':
            longest += s[i]
            curr_len += 1
        else:
            res = max(res, curr_len)
            curr_len = 0
            longest = ""
    res = max(res, curr_len)
    if curr_len > 0:
        longest = longest.strip()
    return res, longest

def countOccurance(s, char):
    count = 0
    for i in s:
        if i == char:
            count += 1
    return char, count

def isPalindrome(s):
    for i in range(0, int(len(s) / 2)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

def subStr(mainstr, sub):
    res = []
    for i in range(len(mainstr)):
        if mainstr[i:i+len(sub)] == sub:
            res.append(i)
    return res

def freq(s):
    words = s.split()
    unique_words = []
    for i in words:
        if i not in unique_words:
            unique_words.append(i)
    print("Frequency of each word in the string is:")
    for word in unique_words:
        print(f'Frequency of "{word}" is: {words.count(word)}')

flag = 1
while flag == 1:
    print("/MENU*/")
    print("1. To display word with the longest length")
    print("2. To determine the frequency of occurrence of a particular character")
    print("3. To check whether a given string is palindrome or not")
    print("4. To display index of first appearance of the substring")
    print("5. To count the occurrences of each word in a given string")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        s = "I am working in the department of computer engineering"
        l, longest_word = LongestWordLength(s)
        print("Longest word is '{1}' of length {0}".format(l, longest_word))
        
    elif choice == 2:
        s = "I am working in the department of computer engineering"
        c = input("Enter the character to count: ")
        c, cnt = countOccurance(s, c)
        print("Character '{0}' occurred {1} times in string: '{2}'".format(c, cnt, s))
        
    elif choice == 3:
        s = input("Enter the string to check palindrome: ")
        if isPalindrome(s):
            print("Yes, the string '{0}' is a palindrome.".format(s))
        else:
            print("No, the string '{0}' is not a palindrome.".format(s))
            
    elif choice == 4:
        s = "I am working in the department of computer engineering"
        s1 = input("Enter the substring to find: ")
        indices = subStr(s, s1)
        print("Starting indices of substring '{1}' in string '{0}' are: {2}".format(s, s1, indices))
        
    elif choice == 5:
        s = "apple mango apple orange orange apple guava mango mango"
        freq(s)
        
    elif choice == 6:
        print("Closed")
        flag = 0
        
    else:
        print("Wrong choice, please try again.")