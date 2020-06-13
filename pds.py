# pandas

import pandas as pd

students = {
    'Names': ['Lou', 'Vance', 'Paul'],
    'GPA': [3.3, 3.5, 3.0],
    'Major': ["Economics", 'Economics and Finance', 'Accounting']
}

# manually build a dataframe
print(students)
new_students = pd.DataFrame(students)
print()
print(new_students)
print()

row_labels = ['LL', 'VR', 'PS']
new_students.index = row_labels # changing the index from generic to custom 'LL'...
print(new_students)
print()

# transform a csv file into a dataframe with pandas.DataFrame(imported_dataset)
htwt = pd.read_csv("C:\\Users\\Loube\\Desktop\\htwt.csv", index_col = 0) # index_col = 0..1.. column used as row label
print(htwt)