student_dic = {"Marry": 9.5, "Rafs": 6.5, "Masud": 8, "Anna": 5};
print(student_dic.values());
print(student_dic.keys());
marksMarry = list(student_dic);
print(marksMarry[0])
print(marksMarry[1])
print(marksMarry[2])
print(marksMarry[3])
# print(marksMarry[4])
totalMarksOfAllStudents = sum(student_dic.values());
length = len(student_dic);
mean = totalMarksOfAllStudents / length;
print('Avg:',mean);