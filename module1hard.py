DICT = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
result_list = []
for i in grades:
    result = sum(i) / len(i)
    result_list.append(result)
for r in range(len(result_list)):
    DICT[students_list[r]] = result_list[r]
print(DICT)
