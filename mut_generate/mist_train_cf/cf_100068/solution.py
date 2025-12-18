"""
QUESTION:
Write a function named `SwapNN` that takes a list of bytes representing memory and two addresses as input, and swaps the 4-byte numbers at these addresses. The function should not use any external methods to copy or move data, instead directly manipulating the memory. The function should also validate the addresses and return an error message if either address is invalid (i.e., less than 0 or would access memory outside the list).
"""

def SwapNN(mem, addr1, addr2):
    # Check if the given addresses are valid or not
    if (addr1 < 0 or addr1+4 > len(mem) or addr2 < 0 or addr2+4 > len(mem)):
        return "Invalid address"

    # Identify the memory addresses of the two numbers to be swapped
    num1_addr = addr1
    num2_addr = addr2

    # Load the values from the memory addresses of both the numbers
    num1 = 0
    num2 = 0
    for i in range(4):
        num1 += (mem[num1_addr+i] << (8*i))
        num2 += (mem[num2_addr+i] << (8*i))

    # Write the value from the memory address of the first number to the memory address of the second number
    for i in range(4):
        mem[num2_addr+i] = (num1 >> (8*i)) & 0xFF

    # Write the value from the memory address of the second number to the memory address of the first number
    for i in range(4):
        mem[num1_addr+i] = (num2 >> (8*i)) & 0xFF

    return mem