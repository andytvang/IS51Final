"""Structured-English
start

create a program that displays the grades of the students on their final
by listing the number of grades, the class average, and percentage of grades
above the average.

Number of grades = 24.
Average grade = 83.25
Percentage of grades above class average = 54.17%

Use open method to bring the list of grades in a dictionary
Then, grades will be listed as integers
We then calculate grades

end
"""
"""Pseudo-Code

def main():

    infile = open(txt)
    display the number of grades
    print("The amount of grades is")

    display the average grade
    print("Average grade is")

def calculate_percent_above_average():
    print("Percentage of grades above class average")
    
"""
def main():
    infile = open("Final.txt" , 'r')
    testGrades = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(testGrades)):
        testGrades[i] = int(testGrades[i])
    len(testGrades)
    print("The amount of grades is: " , len(testGrades))

    classgradeaverage = sum(testGrades) / len(testGrades)
    print("Average grade is: " , classgradeaverage)
    dict = testGrades
    avg = classgradeaverage
    calculate_percent_above_average(dict, avg)

def calculate_percent_above_average(dict, avg):
    num = 0
    for grade in dict:
        if grade > avg:
            num += 1
    print("Percentage of grades above class average: {0:.2f}%".format(100 * num / len(dict)))

main()



