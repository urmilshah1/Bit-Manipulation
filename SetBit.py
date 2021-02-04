def SetBit(x, position):
    mask = 1 << position
    return x | mask
print(int(0b00000001))
print(SetBit(0b00000001, 0b00000001))


