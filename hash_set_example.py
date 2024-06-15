def remove_duplicates(data):
    seen = set()
    result = []
    for item in data:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage
data = [1, 2, 2, 3, 4, 4, 5]
unique_data = remove_duplicates(data)
print(unique_data)  # Output: [1, 2, 3, 4, 5]

