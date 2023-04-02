lst = input().split()
last = lst.pop()
lst.insert(0, last)
print(" ".join(lst))