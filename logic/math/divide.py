def divide_numbers(nums: list[int]) -> int:
   """Ділить всі числа у списку"""
   result = nums[0]
   for n in nums[1:]:
        if n == 0:
            return "Ділення на нуль неможливе"
        result /= n
   return result
