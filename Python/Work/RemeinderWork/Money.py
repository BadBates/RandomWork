#Amount of pennies the customer brought in.
pennies = int(input("How many pennies do you have man:"))

#How much a penny cost in comparison to bills .
penny = .01

#Bills in their original amount.
onehundred = 100
fifty = 50
twenty = 20
ten = 10
five = 5
one = 1

#Calculations for pennies into Bills
onehundreds = onehundred / penny
print ("Amount of 100 dollar bills:", pennies / onehundreds)
pennies2 = pennies % onehundreds
print ("Pennies left", pennies2)

fifties = fifty / penny
print ("Amount of fifties:", pennies2 / fifties)
pennies3 = pennies2 % fifties
print ("Pennies left:",pennies3)

twenties = twenty / penny
print ("Amount of twenties:", pennies3 / twenties)
pennies4 = pennies3 % twenties
print ("Pennies left:",pennies4)

tens = ten / penny
print ("Amount of tens:", pennies4 / tens)
pennies5 = pennies4 % tens
print ("Pennies left:",pennies5)

fives =  five / penny
print ("Amount of fives:", pennies5 / fives)
pennies6 = pennies5 % fives
print ("Pennies left:",pennies6)

ones = one / penny
print ("Amount of ones:", pennies6 / ones)
pennies7 = pennies6 % ones
print ("Pennies left:",pennies7)