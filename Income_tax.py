# import sys
salary = 1600000
# salary = int(sys.argv[1])
# salary = eval(input("Enter the salary: "))
tax = 0
default_slab = 300000
if salary > 0:
    salary = salary - default_slab
    # salary slab from 3 to 6 lakhs
    if salary > 0:
        if salary >= default_slab:
            tax = ((default_slab / 100) * 5) + tax
        else:
            tax = ((salary / 100) * 5) + tax
        salary = salary - default_slab
    # salary slab from 6 to 9 lakhs
    if salary > 0:
        if salary >= default_slab:
            tax = ((default_slab / 100) * 10) + tax
        else:
            tax = ((salary / 100) * 10) + tax
        salary = salary - default_slab
    # salary slab from 9 to 12 lakhs
    if salary > 0:
        if salary >= default_slab:
            tax = ((default_slab / 100) * 15) + tax
        else:
            tax = ((salary / 100) * 15) + tax
        salary = salary - default_slab
    # salary slab from 12 to 15 lakhs
    if salary > 0:
        if salary >= default_slab:
            tax = ((default_slab / 100) * 20) + tax
        else:
            tax = ((salary / 100) * 20) + tax
        salary = salary - default_slab
    # salary slab >15 lakhs
    if salary > 0:
        tax = ((salary / 100) * 30) + tax
print(tax)