# Python Programming Assignment 01

**<span style="color: green; font-weight: bold;">Instructions:</span> Implement Python programs to accomplish the following tasks**

1. **Age Assignments Based on the Riddle**

   - **Problem Statement:** Write a program to solve this age-related riddle!
     Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
     - Anton is 21 years old.
     - Beth is 6 years older than Anton.
     - Chen is 20 years older than Beth.
     - Drew is as old as Chen's age plus Anton's age.
     - Ethan is the same age as Chen.
   - Your code should store each person's age to a variable and print their names and ages at the end.
     ```python
     Anton is 3
     Beth is 4
     Chen is 5
     Drew is 6
     Ethan is 7
     ```

2. **Formatted String Interpolation**

   - **Task:** Given the variables `name`, `age`, and `city`, use f-strings to construct a sentence that describes a person using these variables.
     ```python
     name:str = "Alice"
     age:int = 30
     city:str = "New York"
     ```
   - **Instructions:** Use an f-string to create a sentence in the format: `"Alice is 30 years old and lives in New York."`
   - **Expected Output:**
     ```
     Alice is 30 years old and lives in New York.
     ```

3. **String Manipulation**

   - **Task:** Given the string `s`, use string methods to:
     - **Capitalize the first letter:** make the first character uppercase and the rest of the string lowercase.
     - **Convert to uppercase:** change all characters in the string to uppercase.
     - **Convert to lowercase:** change all characters in the string to lowercase.
     ```python
     s:str = "hElLo WoRlD"
     ```
   - **Expected Output:**
     ```
     Hello world
     HELLO WORLD
     hello world
     ```

4. **Substring Search**

   - **Task:** Given the string `s`, use string methods to:
     - **Find the index of "fox":** get the starting index of the substring "fox". If "fox" is not found, it should return -1.
     - **Count occurrences of "the":** Use the string's built-in method to count how many times the substring "the" appears in the string.
     ```python
     s:str ="the quick brown fox jumps over the lazy dog"
     ```
   - **Expected Output:**
     ```
     index of 'fox' is 16
     'the' appears 2 times
     ```

5. **String Replacement**

   - **Task:** Given the string `s`, use string methods to:
     - **Replace "Python" with "Java":** substitute "Python" with "Java".
     ```python
     s:str ="I love programming in Python"
     ```
   - **Expected Output:**
     ```
     I love programming in Java
     ```

6. **String Splitting and Joining**

   - **Task:** Given the string `s`, use string methods to:
     - **Split into a list:** break the string into a list of substrings based on the delimiter `,`.
     - **Join with spaces:** combine the list of substrings back into a single string, with each element separated by a space.
     ```python
     s:str ="apple,banana,cherry,dates"
     ```
   - **Expected Output:**
     ```
     ["apple", "banana", "cherry", "dates"]
     apple banana cherry dates
     ```

7. **String Stripping and Justifying**

   - **Task:** Given the string `s`, use string methods to:
     - **Remove leading/trailing spaces:** remove all leading and trailing whitespace characters from the string.
     - **Left justify with '\*':** left justify the string within a field of width 20, using `*` as the fill character.
     - **Right justify with '\*':** right justify the string within a field of width 20, using `*` as the fill character.
     ```python
     s:str ="   Python is fun!   "
     ```
   - **Expected Output:**
     ```
     Python is fun!
     Python is fun!*****
     *****Python is fun!
     ```

8. **Convert an integer to its binary representation**

   - **Task:** Given an integer `num`
     - Obtain the binary representation of `num`
     ```python
     num:int = 45
     ```
   - **Expected Output:**
     ```
     Binary representation : 0b101101
     ```

9. **Calculate Powers of Numbers.**

   - **Task:** Given two integers `base` and `exponent`
     - Compute `base` raised to the power of `exponent`.
     ```python
     base:int = 3
     exponent:int = 4
     ```
   - **Expected Output:**
     ```
     Power result: 81
     ```

10. **Round floating-point numbers**

    - **Task:** Given a floating-point number `value`
      - Round `value` to the nearest integer.
      - Round `value` to two decimal places.
      ```python
      value:float = 12.34567
      ```
    - **Expected Output:**
      ```
      Rounded to nearest integer: 12
      Rounded to two decimal places: 12.35
      ```
