# using dictionary

# # word = input("Enter the word:")
# keypad = {1: ["&", "("], 2: ["A", "B", "C"], 3: ["D", "E", "F"], 4: ["G", "H", "I"], 5: ["J", "K", "L"],
#               6: ["M", "N", "O"], 7: ["P",  "Q", "R", "S"], 8: ["T", "U", "V"], 9: ["W", "X", "Y"]}
# for letter in "Maisod#":
#     # print(letter)
#     # print("---")
#     flag = True
#     for numbers, alphabets in keypad.items():
#         # print(numbers, alphabets)
#         if str(letter).upper() in alphabets:
#             try:
#                 print(f"Letter {letter} - {numbers} Number {int(alphabets.index(str(letter).upper()))+1} position")
#                 flag = False
#                 break
#             except Exception as error:
#                 print(error)
#     if flag:
#         print(letter, "not in keypad")


# using list


word = input("Enter the word:")
keypad = [["&", "("], ["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"], ["M", "N", "O"],
          ["P",  "Q", "R", "S"], ["T", "U", "V"], ["W", "X", "Y"]]
for letter in word:
    # print(letter)
    # print("---")
    flag = True
    for numbers in keypad:
        # print(numbers, alphabets)
        for alphabets in numbers:
            each_letter = str(letter).upper()
            if each_letter in alphabets:
                try:
                    print(f"Letter {letter} - {numbers} Number {int(alphabets.index(each_letter))+1} position")
                    flag = False
                    break
                except Exception as error:
                    print(error)
    if flag:
        print(letter, "not in keypad")