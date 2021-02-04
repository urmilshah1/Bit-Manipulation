def ClearBit(x, position):
    mask = 1 << position
    return x & ~(mask)


print(int(0b111), 0b111)
print(ClearBit(0b111, 3))

