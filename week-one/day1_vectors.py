import numpy as np

x = np.array([2000, 3, 2])

print("Vector:", x)
print("Shape:", x.shape)

x2 = np.array([1500, 2, 1])
print("Second Vector:", x2)

x3 = np.array([
    [2000, 3, 2], 
    [1500, 2, 1], 
    [1800, 3, 2]
])
print("Dataset:", x3)
print("Dataset shape:", x3.shape)

#Dot Product
x = np.array([2000, 3, 2])

w = np.array([150, 10000, 8000])

prediction = np.dot(x, w) 

print("Prediction (no bias):", prediction)

manual = x[0]*w[0] + x[1]*w[1] + x[2]*w[2]

print("Manual:", manual)
print("NumPy:", np.dot(x, w))