import numpy as np
with open('bin.txt', 'r') as file:
    stringData = file.read()
binary_data = bytes(int(stringData[i:i+8], 2) for i in range(0, len(stringData), 8))
with open('reconstructVideo.mp4', 'wb') as file:
    file.write(binary_data)