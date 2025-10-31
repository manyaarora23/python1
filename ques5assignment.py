""" 
Avasthi is having some amount of money and he is having only some denominations of 100,50,20,10,5,2,1.
 He needs to know how many notes are required for the amount present with him. (Do it using Switch case)
"""
def notes_count(amount):
    denomination = [100 , 50 , 20 , 10 , 5 , 2 , 1]
    print("No. of notes for each denominations : ")
    for notes in denomination:
        count = amount // notes
        amount = amount % notes
        if count > 0:
            match notes:
                case 100:
                    print("100 :", count)
                case 50:
                    print("50 :", count)
                case 20:
                    print("20 :", count)
                case 10:
                    print("10 :", count)
                case 5:
                    print("5 :", count)
                case 2:
                    print("2 :", count)
                case 1:
                    print("1 :", count)
amount = int(input("Amount of money present : "))
notes_count(amount)
