def FlipBit(x, position):
    mask = 1 << position
    return mask ^ position

print(FlipBit(15, 2)
