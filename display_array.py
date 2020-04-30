
#Craeting a prompt to intake a array of mark


import student_mark
mark1 = int(input("Enter 1st mark: \n"))
mark2 = int(input("Enter 2nd mark: \n"))
mark3 = int(input("Enter 3rd mark: \n"))
mark4 = int(input("Enter 4th mark: \n"))
mark5 = int(input("Enter 5th mark: \n"))
mark6 = int(input("Enter 6th mark: \n"))
mark7 = int(input("Enter 7th mark: \n"))
mark8 = int(input("Enter 8th mark: \n"))
mark9 = int(input("Enter 9th mark: \n"))
mark10 = int(input("Enter 10th mark: \n"))

int_average = student_mark.mark_array(mark1, mark2, mark3, mark4, mark5, mark6, mark7, mark8, mark9, mark10)
print("The average mark is:", int_average, "%")

final_average = student_mark.average_mark(int_average)
print("The Student has:", final_average)

