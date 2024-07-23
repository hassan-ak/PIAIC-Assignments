s: str = "the quick brown fox jumps over the lazy dog"


fox_index = s.index("fox")


if fox_index != -1:
    print(f"index of 'fox' is {fox_index}")
else:
    print("'fox' is not found in the string")


the_count = s.count("the")
print(f"'the' appears {the_count} times")
