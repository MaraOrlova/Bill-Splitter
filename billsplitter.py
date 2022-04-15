import random
# write your code here
number_of_friends = int(
    input("Enter the number of friends joining (including you):\n")
)

if number_of_friends <= 0:
    print("No one is joining for the party")
else:
    names = []

    print()

    print("Enter the name of every friend (including you),"
          " each on a new line:")

    for _ in range(number_of_friends):
        names.append(input())

    print()

    total_bill = int(input("Enter the total bill value: \n"))

    amount_per_person = round(total_bill / number_of_friends, 2)

    payment_dict = dict.fromkeys(names, amount_per_person)

    print()

    #print(payment_dict)
    
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    
    lucky = input()
    
    if lucky == "Yes":
        
        lucky_name = random.choice(names)
        
        print("{} is the lucky one!".format(lucky_name))
        
        amount_per_person = round(total_bill / (number_of_friends - 1), 2)
        
        payment_dict = dict.fromkeys(names, amount_per_person)
        
        payment_dict[lucky_name] = 0
    
        print(payment_dict)
        
    else:
        
        print("\nNo one is going to be lucky")
        
        print(payment_dict)
        


