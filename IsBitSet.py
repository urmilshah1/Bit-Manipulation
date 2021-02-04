def IsBitSet(x, position):
    shifted = x >> position
    return shifted & 1

print(bin(100))
print(IsBitSet(100, 10))