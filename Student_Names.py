s = open('studentnames.txt', 'r')
num = 0
# read = s.readline().rstrip('\n')
for student in s:
    name = student.rstrip('\n')
    print(name)
    num+=1
# i-=1
print("There were", num, "students in the file.")
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
s.close()
