from collections import Counter

# Define the dataset
dataset = [
    ("Small", "Green", "Irregular", "No"),
    ("Large", "Red", "Irregular", "Yes"),
    ("Large", "Red", "Circle", "Yes"),
    ("Large", "Green", "Circle", "No"),
    ("Large", "Green", "Irregular", "No"),
    ("Small", "Red", "Circle", "Yes"),
    ("Large", "Green", "Irregular", "No"),
    ("Small", "Red", "Irregular", "No"),
    ("Small", "Green", "Circle", "No"),
    ("Large", "Red", "Circle", "Yes")
]

# Define the test instance
test_instance = ("Small", "Red", "Circle")

def hamming_distance(instance1, instance2):
    return sum(el1 != el2 for el1, el2 in zip(instance1, instance2))

def knn(dataset, test_instance, k):
    distances = [(data, hamming_distance(test_instance, data[:-1])) for data in dataset]
    distances.sort(key=lambda x: x[1])  # Sort by distance
    nearest_neighbors = [data[0] for data in distances[:k]]
    counts = Counter(nn[-1] for nn in nearest_neighbors)
    majority_class = counts.most_common(1)[0][0]
    return majority_class

k = 5
predicted_label = knn(dataset, test_instance, k)
print(f"Predicted label for test instance {test_instance}: {predicted_label}")
