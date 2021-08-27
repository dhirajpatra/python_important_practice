"""
Sets are lists with no duplicate entries
"""
print(set("my name is Eric and Eric is my name".split()))
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(a)
print(a.intersection(b))
print(a.symmetric_difference(b))
print(a.difference(b))
print(a.union(b))
print(b.difference(a))
