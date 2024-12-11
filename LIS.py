#Q44. Write a Python program to find the longest increasing subsequence in a list of numbers.

#check if the list is empty
def longest_increasing_subsequence(nums):
    if not nums:
        return []

    # List to store all subsequences
    subsequences = []

    for num in nums:
        # Find the longest subsequence that can be extended
        longest_subsequence = []
        for subsequence in subsequences:
            if subsequence[-1] < num and len(subsequence) > len(longest_subsequence):
                longest_subsequence = subsequence

        # Add the new subsequence
        subsequences.append(longest_subsequence + [num])

    # Return the longest subsequence
    return max(subsequences, key=len, default=[])

# Example usage:
nums = [24, 6, 5, 33, 6, 26, 10, 18]
lis = longest_increasing_subsequence(nums)
print("Longest Increasing Subsequence:", lis)
