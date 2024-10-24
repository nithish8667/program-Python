rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
row_sums = []
for i in range(rows):
    row_sums2=[]
    for j in range(columns):
        row_sums2.append(int(input()))
    row_sums.append(row_sums2)
print(row_sums)
sol=[]
for i in row_sums:
    add=0
    for j in i:
        add+=j
    sol.append(add)
print(*sol)