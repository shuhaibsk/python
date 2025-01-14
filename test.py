def duplicate_count(input_list):
    # Check if the input is a list
    if not isinstance(input_list, list):
        return "Invalid"
    
    # If the list is empty, return an empty dictionary
    if not input_list:
        return {}
    
    # Initialize an empty dictionary to store counts
    counts = {}
    
    # Iterate over each element in the list
    for item in input_list:
        if item not in counts:  # Check if the item is not in the dictionary
            counts[item] = 1  # Add it with a count of 1
        else:
            counts[item] += 1  # Increment the count
    
    return counts

# Example usage
result = duplicate_count([1, 2, 1, "a", "b", "b", "b", "1"])
print(result)
