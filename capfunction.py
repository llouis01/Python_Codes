# program to make proper capitalization
# useful when working with lots of strings that are improperly capitalized

text_to_correct = input("Enter text to correct: ")

def CorrectCap(text_to_correct):
    proper_cap = text_to_correct.title() # to capitalize 1st letter of words
    print (proper_cap)

CorrectCap(text_to_correct)
