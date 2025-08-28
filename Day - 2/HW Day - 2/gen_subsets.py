def generate_subsets(nums, index=0, current=None):
    if current is None:
        current = []
    if index == len(nums):
        print(current)
        return
    
    # Case 1: Exclude nums[index]
    generate_subsets(nums, index + 1, current)
    
    # Case 2: Include nums[index]
    current.append(nums[index])
    generate_subsets(nums, index + 1, current)
    
    # Backtrack (remove the last added element)
    current.pop()

nums = [1, 2, 3]
generate_subsets(nums)
