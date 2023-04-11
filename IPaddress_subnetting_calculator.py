# Name:                     Final Project – IP address subnetting calculator
# Author:                   Yunfeng Lin (Ylin8832)
# Date Created:             April 06, 2023
# Date Last Modified:       April 10, 2023

'''
1. This program is written for a scenario of performing network CIDR IP subnetting technic that is used to create number of subnets 
   from a given base network address.
2. User will be given an IPv4 network address, the program will then prompt the user to enter the 32 bits IPv4 address from the first 
   octet to the fourth octet one by one (e.g., 192.168.10.0/24).
3. Based on the user input, the base IP address (before subnetting) will be displayed to the console.
4. Then the program will again prompt the user to input the network bits, host bits, number of subnets that are required to be created, 
   and number of host bits to borrow from the host bits for calculating the block size and each new subnets.

'''
import os

IPsubnettingFile = "ipsubneting.txt"

print("\n{:-^50s}".format("IP address subnetting calculator".upper()))
print("\nPlease enter a base IP address you would like to subnet.")
# since this is an IP address, the input must be all numbers without spaces and dots.
while True:
    firstOct = input("First octet: ").strip().replace(".","")
    if firstOct.isdecimal() == False:            # check if the input data is a decimal number. If it is proved False,
        print("Invalid input, try again.")       # then inform the user that the input is invalid and try again.
    else:
        break
while True:
    secondOct = input("Second octet: ").strip().replace(".","")
    if secondOct.isdecimal() == False:
        print("Invalid input, try again.")
    else:
        break
while True:
    thirdOct = input("Third octet: ").strip().replace(".","")
    if thirdOct.isdecimal() == False:
        print("Invalid input, try again.")
    else:
        break
while True:
    fourthOct = input("Fourth octet: ").strip().replace(".","")
    if fourthOct.isdecimal() == False:
        print("Invalid input, try again.")
    else:
        break
while True:
    preFix = input("CIDR value: ").strip().replace(".","")
    if preFix.isdecimal() == False:
        print("Invalid input, try again.")
    else:
        break  

print("\n{}Your base address is{}".format("-----","-----"))
print("\n\t{}.{}.{}.{}/{}".format(firstOct,secondOct,thirdOct,fourthOct,preFix))
print("\nContinue to enter necessary values for subnetting your address.\n----")

def blocksizeCal():
    baseNetworkbits = int(input("Enter the number of base network bits: "))
    hostBits = int(input("Enter the host bits: "))
    subnetsRequred = int(input("Enter the number of subnets that have to be created: "))
    # The variable "exponent" refers to the number of host bits to borrow, i.e., 2 raise to the power of which input value from the user.
    if subnetsRequred > 2 and subnetsRequred <= 4:
        exponent = 2
    elif subnetsRequred > 4 and subnetsRequred <= 8:
        exponent = 3
    elif subnetsRequred > 8 and subnetsRequred <= 16:
        exponent = 4
    elif subnetsRequred > 16 and subnetsRequred <= 32:
        exponent = 5
    elif subnetsRequred > 32 and subnetsRequred <= 64:
        exponent = 6
    elif subnetsRequred > 64 and subnetsRequred <= 128:
        exponent = 7
    elif subnetsRequred > 128 and subnetsRequred <= 256:
        exponent = 8
    elif subnetsRequred > 256 and subnetsRequred <= 512:
        exponent = 9
    elif subnetsRequred > 512 and subnetsRequred <= 1024:
        exponent = 10
    elif subnetsRequred > 1024 and subnetsRequred <= 2048:
        exponent = 11

    bitsToborrow = exponent
    print("{}\nTo create {} new subnets, {} bits need to be borrowed from the current host bits.\n{}".format("----",subnetsRequred, bitsToborrow,"----"))

    newCIDRval = baseNetworkbits + exponent
    newHostbits = hostBits - bitsToborrow

    if newHostbits >= 8 and newHostbits <= 16: # if new host bits are more than 8 bits and less than 16 bits, block size will be calculated on 3rd octet. 
        blockSize = 2 ** (newHostbits - 8)
    elif newHostbits >= 16 and newHostbits <= 24: # if new host bits are more than 16 bits and less than 24 bits, block size will be calculated on 2nd octet. 
        blockSize = 2 ** (newHostbits - 16)
    else:
        blockSize = 2 ** newHostbits

    print("Bits to borrow:",bitsToborrow)
    print("New CIDR value:",newCIDRval)
    print("New host bits:",newHostbits)
    print("Block size:",blockSize)

    return(blockSize)
block = blocksizeCal()

print("The following subnetting result has also been saved here:\n\n\t{}\n".format(os.path.join(os.getcwd(), IPsubnettingFile)))
output = ""
output += "Network  Broadcast  First Valid  Last Valid\t"
output += "\nAddress  Address    Address      Address"

i = block

output += ("\n{0:>4}\t{1:>8}\t{2:>3}\t{3:>5}".format(i-block, i-1, 1, i-2))

while i < 256:
    i += block
    output += ("\n{0:>4}\t{1:>8}\t{2:>3}\t{3:>5}".format(i-block, i-1, i-block+1, i-2))

with open(IPsubnettingFile, "w") as outputFile:
    outputFile.write(output)
print(output)

