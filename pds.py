# pandas

import pandas as pd

students = {
    'Names': ['Lou', 'Vance', 'Paul'],
    'GPA': [3.3, 3.5, 3.0],
    'Major': ["Economics", 'Economics and Finance', 'Accounting']
    }

print(students)
pd.DataFrame(students)
print()
print(students)
print()

htwt = pd.read_csv("C:\\Users\\Loube\\Desktop\\htwt.csv")
print(htwt)
pd.DataFrame(htwt)
print(htwt)