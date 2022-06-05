

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA | setB)
print(setA.union(setB)) # A birleşim B
print(setB.union(setA))


print(setA & setB)
print(setA.intersection(setB)) # A kesişim B
print(setB.intersection(setA))

print(setA - setB)
print(setA.difference(setB)) # A fark B
print(setB.difference(setA))

print(setA ^ setB)
print(setA.symmetric_difference(setB)) # A birleşim B - A kesişim B
print(setB.symmetric_difference(setA))
