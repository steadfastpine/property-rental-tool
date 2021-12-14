
# Program Name:		Property Rental Tool
# Program Author:	Scott Forsberg
# Creation Date:	2019-01-15
# Python Version:	3.7.1



# gather user input
numRenters = int(input("How many renters? "))
creditScore = int(input("What is the your lowest credit score? "))
monthlyIncome = int(input("What is your total monthly income? "))
isFelon = input("Are you a convicted felon? ")
hasPet = input("Do you have a cat or dog? ")
lowBaseRent = int(input("What is the low-end rent? "))
highBaseRent = int(input("What is the high-end rent? "))

'''
# test values
numRenters = int(2)
creditScore = int(800)
monthlyIncome = int(3600)
isFelon = "n"
hasPet = "yes"
lowBaseRent = int(950)
highBaseRent = int(1100)
'''


# Calculate total monthly rent according to these rules:
# apply a 10% discount on base rent if credit score is at least 740
# if renter has a pet, add $100 to total monthly rent
def monthlyRentCheck(baseRentVar,hasPetVar,creditScoreVar):

    # reduce rent by 10% if credit score over 740
    if creditScoreVar >= 740:
        baseRentVar = baseRentVar - (baseRentVar * .1)
        
    # add $100 to rent if pet
    if hasPetVar == "yes":
        baseRentVar = baseRentVar + 100

    return(baseRentVar)



# Determine whether renter is eligible according to these rules:
# is not a felon
# lowest credit score > 579
# has monthly income at least 3x total month
def eligibleCheck(isFelonVar,creditScoreVar,monthlyIncomeVar,monthlyRentVar):

    #check if felon, if so then ineligible
    if isFelonVar == "no" or isFelonVar == "n" or isFelonVar == "not":

        #check if credit score less than 580, if so then ineligible
        if creditScoreVar > 579:

            #check if 3 times monthly income is less than total monthly rent, if so then ineligible
            if monthlyIncomeVar > monthlyRentVar * 3:
                
                return("yes")



# Calculate down-payment based on these rules:
# first & last month's rent
# $250 refundable damage depos
def downPaymentCheck(monthlyRentVar):

    # first and last months rent plus $250
    downPaymentVar = (monthlyRentVar * 2) + 250
    return(downPaymentVar)



# Calculate monthly rent per person
def monthlyRentPerPersonCheck(monthlyRentVar,numRentersVar):

    # divide monthly rent by number of people renting
    return(monthlyRentVar / numRentersVar)
    


# Calculate down payment per person
def downPaymentPerPersonCheck(downPaymentVar,numRentersVar):

    # divide down payment by number of people renting
    downPaymentPerPersonVar = (downPaymentVar / numRentersVar)
    return(downPaymentPerPersonVar)



# check low base rent
monthlyRent = monthlyRentCheck(lowBaseRent,hasPet,creditScore)
monthlyRentPerPerson = monthlyRentPerPersonCheck(monthlyRent,numRenters)
eligible = eligibleCheck(isFelon,creditScore,monthlyIncome,monthlyRent)
downPayment = downPaymentCheck(monthlyRent)
downPaymentPerPerson = downPaymentPerPersonCheck(downPayment,numRenters)



# eligibility feedback
print("\n##  Low end rent check\n")

if eligible == "yes":

    # For eligible renters, print the following information for both low-rent & high-rent scenarios:
    #
    # total monthly rent
    # rent per person
    # total down-payment
    # payment per person
    print("Monthly rent total:\t","{:.2f}".format(monthlyRent).rjust(10))
    print("Monthly rent per person:","{:.2f}".format(monthlyRentPerPerson).rjust(10))
    print("Down-payment total:\t","{:.2f}".format(downPayment).rjust(10))
    print("Down-payment per person:","{:.2f}".format(downPaymentPerPerson).rjust(10))
    
else:
    print("Sorry, you aren't eligible.")

  

# check high base rent
monthlyRent = monthlyRentCheck(highBaseRent,hasPet,creditScore)
monthlyRentPerPerson = monthlyRentPerPersonCheck(monthlyRent,numRenters)
eligible = eligibleCheck(isFelon,creditScore,monthlyIncome,monthlyRent)
downPayment = downPaymentCheck(monthlyRent)
downPaymentPerPerson = downPaymentPerPersonCheck(downPayment,numRenters)



# eligibility feedback
print("\n\n##  High end rent check\n")

if eligible == "yes":

    # For eligible renters, print the following information for both low-rent & high-rent scenarios:
    #
    # total monthly rent
    # rent per person
    # total down-payment
    # payment per person
    print("Monthly rent total:\t","{:.2f}".format(monthlyRent).rjust(10))
    print("Monthly rent per person:","{:.2f}".format(monthlyRentPerPerson).rjust(10))
    print("Down-payment total:\t","{:.2f}".format(downPayment).rjust(10))
    print("Down-payment per person:","{:.2f}".format(downPaymentPerPerson).rjust(10))
    
else:
    print("Sorry, you aren't eligible.")
    
import sys
sys.exit()

'''
'''
