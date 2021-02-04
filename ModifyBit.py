def ModifyBit(x, position, state):
    mask = 1 << position
    return (x & ~mask) | (-state & mask)

print(ModifyBit(10, 5, 1))
