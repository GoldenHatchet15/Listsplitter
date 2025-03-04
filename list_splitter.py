def split_array(arr):
    """
    Splits a given array into two equal halves.
    If the array length is odd, the extra element goes to the first half.
    
    :param arr: List of elements to be split
    :return: Tuple containing two lists
    """
    mid = (len(arr) + 1) // 2  # Ensures the first half gets the extra element if odd
    first_half = arr[:mid]
    second_half = arr[mid:]
    
    return first_half, second_half

# Example usage:
if __name__ == "__main__":
    big_array = [1, 2, 3, 4, 5, 6, 7]
    list1, list2 = split_array(big_array)
    print("First half:", list1)
    print("Second half:", list2)
