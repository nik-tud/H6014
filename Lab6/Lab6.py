from collections import Counter
from pathlib import Path

import numpy as np
from PIL import Image

data = Path("aes.bmp.enc").read_bytes()

# the encrypted image is 640 * 480 * 3 bytes per pixel
# because typical bmp images of size 901K are 640 * 480 in resolution
width, height = 640, 480
payload = data[:width * height * 3]

# AES has a 16-byte block size.
blocks = [
    payload[i:i + 16]
    for i in range(0, len(payload), 16)
]

frequencies = Counter(blocks)

print("File size:", len(data))
print("Number of blocks:", len(blocks))
print("Distinct blocks:", len(frequencies))
print("Most common blocks:")
for block, count in frequencies.most_common(5):
    print(block.hex(), count)

# Find the most commonly repeated ciphertext blocks
most_common = frequencies.most_common()
rank = {block: i for i, (block, _) in enumerate(most_common)}

# 120 blocks per row for a 640-pixel-wide,
# 24-bit image: 640 * 3 / 16 = 120.
blocks_per_row = width * 3 // 16
grid = np.zeros((height, blocks_per_row), dtype=np.uint8)

# Go through each block and if it is most common make it white
# if it is 2nd most common make it black
# otherwise make everything else gray
for i, block in enumerate(blocks):
    y, x = divmod(i, blocks_per_row)

    if rank[block] == 0:
        grid[y, x] = 255
    elif rank[block] == 1:
        grid[y, x] = 0
    else:
        grid[y, x] = 100

# Enlarge each block column to make the pattern visible.
result = Image.fromarray(grid, mode="L")
result = result.resize(
    (width, height),
    Image.Resampling.NEAREST
)
result.save("aes.png")

print("Saved aes.png")