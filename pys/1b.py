num = input("Enter the number: ")
rev_num = num[::-1]  # Reverse the number
if num == rev_num:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
