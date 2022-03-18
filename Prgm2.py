# WAP to sort a list in ascending and descending order
list = [5, 4, 3, 2, 1]
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['c', 'a', 'z', 'k']
items = [1, 4, 3, 7, 2]

# method
list.sort()
list1.reverse()
list2.sort(reverse=True)

# builtin function
sorted(items)

print("Ascending:", list)
print("Descending", list1)
print("Descending", list2)
print("ascending", items)