input = "Zebra-493?"
rotationFactor = 3
output = "Cheud-726?"

# encrypt = chr((ord("Z") + rotationFactor-65) % 26 + 65)
encrypt = (ord('Z') + rotationFactor - 65)
print(encrypt)


