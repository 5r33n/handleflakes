#!/usr/bin/env python3
from os import path
import time

# CONSTANTS #
WEED = 4.20
LIST_LEN = 1000

with open("handles/handles_list.txt", "r") as handles_file:
    handles = handles_file.read().splitlines()

seed_index = 1

for handle in handles:
    if path.exists(f"seeds/{handle}.txt"):
        print(f"[WARN] {handle}.txt exists in seeds/, passing")
        continue
    array = []
    for char in handle:
        if char == "\n":
            continue
        elif char.isnumeric():
            array.append(int(char) + 26)
            # print(int(char) + 26)
        elif char == "_":
            array.append(0)
            # print(0)
        else:
            array.append(ord(char.lower()) - 96)
            # print(ord(char) - 96)
    with open(f"seeds/{handle}.txt", "a") as seeds_file:
        index = 0
        while True:
            for num in array:
                seeds_file.write(f"{num}\n")
                array[index % len(array)] = int((num * WEED) // 1) % LIST_LEN
                index = index + 1
                if index == LIST_LEN:
                    break
            if index == LIST_LEN:
                break
    print(f"[{time.time()}][OK] seed #{seed_index} created for: {handle}")
    seed_index = seed_index + 1
