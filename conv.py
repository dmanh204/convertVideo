import numpy as np
data = np.fromfile('big_buck_bunny_720p_2mb.mp4', dtype=np.dtype('B'))
# with open('big_buck_bunny_720p_2mb.mp4', 'rb') as f:
#     data = f.read()
output = ''.join(format(byte, '08b') for byte in data)
with open('bin.txt', 'w') as file:
    file.write(output)