manai_adi = [6, 8, 10, 11, 16, 17, 20, 21, 22, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 39, 41, 42, 50, 52, 54, 56,
             59, 60, 64, 66, 68, 72, 73, 74, 75, 77, 80, 84, 85, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
value = eval(input("Enter the house length: "))
count = 0
# value = 41
file = open(r'C:\Studies\Coding\veedu_manai_output.txt', 'a+')
file.write(f'Given input house length is {value} feet\n')
for each_adi in manai_adi:
    # print(each_adi)
    count_adi = value + each_adi
    if (count_adi < max(manai_adi)) and (count_adi in manai_adi):
        count = count + 1
        if count == 4:
            break
        print(f"{value} + {each_adi} = {count_adi}")
        file.write(f'{value} + {each_adi} = {count_adi}\n')
file.write(f'\n\t ---------- \t----------\n\n')
file.close()


# Using with statement
manai_adi = [6, 8, 10, 11, 16, 17, 20, 21, 22, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 39, 41, 42, 50, 52, 54, 56,
             59, 60, 64, 66, 68, 72, 73, 74, 75, 77, 80, 84, 85, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
value = eval(input("Enter the house length: "))
count = 0
# value = 41
with open(r'C:\Studies\Coding\veedu_manai_output.txt', 'a+') as file:
    file.write(f'Given input house length is {value} feet\n')
    for each_adi in manai_adi:
        # print(each_adi)
        count_adi = value + each_adi
        if (count_adi < max(manai_adi)) and (count_adi in manai_adi):
            count = count + 1
            if count == 4:
                break
            print(f"{value} + {each_adi} = {count_adi}")
            file.write(f'{value} + {each_adi} = {count_adi}\n')
    file.write(f'\n\t ---------- \t----------\n\n')







