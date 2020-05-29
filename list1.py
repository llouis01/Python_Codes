# practicing slicing and dicing

lou_grades = ["A", "A+", "A", "B+", "C"]

lou_GPA = [3.5, 3.3, 3.2, 3.1, 3.2]

tom_grades = lou_grades[:] # copying the elements from lou's to tom's

tom_GPA = lou_GPA[:] # same effct as above

lou_grades[3] = "C-"

print(lou_grades)

tom_GPA[1] = "WU"

print(tom_GPA)

class_gpa = lou_GPA + tom_GPA

print(class_gpa)

print(lou_GPA[:4]) # print out up to 3

school_stats = [[lou_grades],
    [lou_GPA], [tom_grades],
    [tom_GPA], [class_gpa]]

print(f"Lou's grades are {lou_grades}, his gpa is {max(lou_GPA)}")
print(f"Tom's grades are {tom_grades}, his gpa is {(tom_GPA[3])}")