"""
QUESTION:
Create a function `SwapNN` that takes a list of integers `mem` representing memory and two addresses `addr1` and `addr2` as input. The function should swap the two 4-byte integers at the given addresses in the memory without using a temporary variable or a `CopyFrom` method. The function should return the modified memory if the addresses are valid, and an error message "Invalid address" otherwise. The addresses are valid if they are non-negative and do not exceed the length of the memory list minus 4.
"""

def SwapNN(mem, addr1, addr2):
    if (addr1 < 0 or addr1+4 > len(mem) or addr2 < 0 or addr2+4 > len(mem)):
        return "Invalid address"

    num1_addr = addr1
    num2_addr = addr2

    num1 = 0
    num2 = 0
    for i in range(4):
        num1 += (mem[num1_addr+i] << (8*i))
        num2 += (mem[num2_addr+i] << (8*i))

    for i in range(4):
        mem[num2_addr+i] = (num1 >> (8*i)) & 0xFF

    for i in range(4):
        mem[num1_addr+i] = (num2 >> (8*i)) & 0xFF

    return mem