import random

def binary_search_float(data, search_for):
    left, right = 0, len(data) - 1
    iterations = 0
    upper = None
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        if data[mid] == search_for:
            return (iterations, data[mid])
        
        elif data[mid] < search_for:
            left = mid + 1
        
        else:
            upper = data[mid]
            right = mid - 1
    
    if upper is None and left < len(data):
        upper = data[left]
    
    return (iterations, upper)

data = [0.156, 0.289, 0.475, 0.638, 0.721, 1.112, 1.378, 1.682, 1.845, 2.239, 2.561, 3.145, 3.859, 4.276, 4.912, 5.637, 6.125, 7.458, 8.237, 9.824]
print("data: ")
print(data)

search_for = 1.9
result = binary_search_float(data, search_for)
print(result) #  2.239

search_for = 3.85
result = binary_search_float(data, search_for)
print(result) # 3.859

search_for = 10
result = binary_search_float(data, search_for)
print(result) # 10



def generate_random_floats(size, lower_bound, upper_bound, precision=3):
    unique_floats = set()
    
    while len(unique_floats) < size:
        number = round(random.uniform(lower_bound, upper_bound), precision)
        unique_floats.add(number)
    
    random_floats = sorted(unique_floats)
    return random_floats

data = generate_random_floats(100, 0, 10)

print("data: ")
print(data)

print("search")
search_for = 5.9
result = binary_search_float(data, search_for)
print(result)


print("big array 100000")

data = generate_random_floats(100000, 0, 10, precision=6)

print("data: ")
print(data[:10])

print("search")
search_for = 5.9
result = binary_search_float(data, search_for)
print(result)

input()