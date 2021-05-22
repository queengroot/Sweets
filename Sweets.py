#Kate Blunt
#September 19, 2019
#Sweets Practice

def main():

    #declare variables

    sweetNum = 0
    bagCost = 0
    people = 0
    sweetsEach = 0
    sweetsRemaining = 0
    costPerPerson = 0

    print("Hello, this is the sweets practice program.\n")
    print()
    
#Get the number of sweets 
    sweetNum = int(input("Enter the number of sweets: "))
    print()
    
#The cost of the bag of sweets. I used a float because money is usually decimals
    bagCost = float(input("Enter the cost of the bag of sweets: " + "$"))
    print()
    
#Get the amount of people
    people = int(input("Enter the amount of people that are sharing: "))
    print()
    
#The sweets each is the number os sweets divided by people
#Integer division because I do not want the fracition
    sweetsEach = sweetNum//people
    
#print results
    print("The amount of sweets each person will get is: " + str(sweetsEach))
    print()
    
#Sweets remaining would be the remainder after divided, so the modulus
    sweetsRemaining = sweetNum%people

#print results
    print("The amount of sweets left over is: " + str(sweetsRemaining))
    print()
    
#Cost per person is the cost of the bag divided by the amount of people
    costPerPerson = bagCost/people

#Print the results
    print("The cost to each person is: " + "$" + str(costPerPerson))
    print()
    print("Bye! Thank you for using this program.")


main()
