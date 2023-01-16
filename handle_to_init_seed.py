#!/usr/bin/env python3
import pyperclip

handle = "nft_finley"
list_text = "["
i = 0
print("\n[", end="")
for char in handle:
    if char.isnumeric():
        list_text = list_text + str(int(char) + 26)
        print(int(char) + 26, end="")
    elif char == "_":
        list_text = list_text + "0"
        print(0, end="")
    else:
        list_text = list_text + str(ord(char.lower()) - 96)
        print(ord(char.lower()) - 96, end="")
    i = i + 1
    if i != len(handle):
        list_text = list_text + ","
        print(",", end="")
list_text = list_text + "]"
print("]\n\n", end="")

final_text = f"""(1) Get handle: `{handle}`

(2) Turn letters into their alphabetic number: `{list_text}` (Underscores are mapped to 0 and literal numbers are added up by 26)

(3) Multiply each number by 4.20 continuously and create a list of 1000 numbers

(4) Take integer parts to create a list of 1000 integers

(5) Use this list as seed (+ code/math) to create a unique snowflake-shaped handleflake"""
pyperclip.copy(final_text)
