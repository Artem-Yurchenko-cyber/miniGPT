def subtract_numbers(nums: list[int]) -> int:
    """Віднімає всі числа у списку"""
    result = nums[0]
    for n in nums[1:]:
        result -= n
    return result