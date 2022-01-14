Content Hints:
- Use a loop to iterate through the Roman numeral to figure out their value. 
- Use a dictionary to store the string characters and their respective values, compare the characters from the input to this list.
- Use a while loop so you can manually control the indices.

Given Roman numerals as a string, return their value as an integer. You may assume the Roman numerals are in the "standard" form, i.e. any digits involving 4 and 9 will always appear in the subtractive form.

    For example:
    >>> roman("II")
    2
    >>> roman("IV")
    4
    >>> roman("IX")
    9
    >>> roman("XIX")
    19
    >>> roman("XX")
    20
    >>> roman("MDCCLXXVI")
    1776
    >>> roman("MMXIX")
    2019
