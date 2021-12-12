height = input("How tall is the tree?: ")
height = int(height)
spaces = height -1
hashes = 1
stumpSpaces = height
while height != 0:
    for i in range(spaces):
        print(' ', end = "")
    for i in range(hashes):
        print('#', end="")
    print()
    spaces -= 1
    hashes += 2
    height -= 1
for i in range(1):
    print(' ', end = "")
    print("   #")

