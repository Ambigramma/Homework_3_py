lst = []
for i in range(int(input())):
    lst.append(int(input()))

def number_near(n):
    lst.append(n)
    lst.sort()
    return lst.pop(lst.index(n) - 1)

print(number_near(int(input())))