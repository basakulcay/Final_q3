commission=0.09
total=0
counter=0
number=int(input('What is the number of employees? '))

for i in range(number):
    sales=int(input('What is the worth of sales of person:'))
    salary=200+sales*commission
    counter+=1
    total+=salary

    print(salary)

print('Total of salaries paid:',total)
print('The average salary paid:',total/counter)
