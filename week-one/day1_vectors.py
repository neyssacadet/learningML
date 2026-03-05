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

# cosine similarity
v1 = np.array([1, 0])
v2 = np.array([0, 1])
v3 = np.array([1, 1])


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print("v1 vs v2:", cosine_similarity(v1, v2))
print("v1 vs v3:", cosine_similarity(v1, v3))

king = [0.8, 0.2, 0.6]
queen = [0.82, 0.18, 0.61]
banana = [0.1, 0.9, 0.3]

king = np.array([0.8, 0.2, 0.6])
queen = np.array([0.82, 0.18, 0.61])
banana = np.array([0.1, 0.9, 0.3])

print("king vs queen:", cosine_similarity(king, queen))
print("king vs banana:", cosine_similarity(king, banana))