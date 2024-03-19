marks1 = int(input("Enter IA1 marks: "))
marks2 = int(input("Enter IA2 marks: "))
marks3 = int(input("Enter IA3 marks: "))
minimum = min(marks1, marks2, marks3)
sumof2 = marks1 + marks2 + marks3 - minimum
avgof2 = sumof2 / 2
print("Average of best 2 = ", avgof2)
