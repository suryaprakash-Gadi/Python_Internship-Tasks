print("Palindrome checker")
print("-------------------")

def palindrome_checker(input_string):
    input_string=input_string.replace(" ","")
    if input_string[0:]==input_string[::-1]:
        print("Given string is a palindrome")
    else:
        print("Given string is Not a palindrome")

input_string=input("Enter a string:").lower()
palindrome_checker(input_string)
