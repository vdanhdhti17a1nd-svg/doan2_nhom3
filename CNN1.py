import numpy as np
image = np.array([
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,1,1,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
], dtype=float)

print("Input Image")
print(image)

kernel = np.array([
    [-1,-1,-1],
    [ 0, 0, 0],
    [ 1, 1, 1]
], dtype=float)

print("\nKernel")
print(kernel)

H, W = image.shape
k = kernel.shape[0]

output_size = H - k + 1

feature = np.zeros((output_size, output_size))

for i in range(output_size):

    for j in range(output_size):

        region = image[i:i+k, j:j+k]

        value = np.sum(region * kernel)

        feature[i,j] = value

print("\nFeature Map")
print(feature)
