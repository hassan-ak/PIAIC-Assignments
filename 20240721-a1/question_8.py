def calculate_power(base: int, exponent: int) -> int:
  """
  Calculate the power of a number.
  """
  result = 1
  for _ in range(exponent):
    result *= base
  return result

# Example usage
base = 3
exponent = 4
power_result = calculate_power(base, exponent)
print(f"Power result: {power_result}")
