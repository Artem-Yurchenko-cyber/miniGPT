def multiply_numbers(nums: list[int]) -> int:
   """Множить всі числа у списку"""
   result = 1
   for n in nums:
       result *= n
   return result
