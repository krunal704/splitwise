def simplifyDebt(transactions):
    # Simplify Debt Function to simplify Transcation
    paidTo = {}     # Persons with amount paid
    paidFrom = {}   # Persons with amount received

    # Iterate each transaction to assign total paid amount
    # and total received amount of each person
    for transaction in transactions:
        sum = 0
        for person in transaction["paidFor"]:
            sum += transaction["paidFor"][person]
            if person in paidTo:
                paidTo[person] += transaction["paidFor"][person]
            else:
                paidTo[person] = transaction["paidFor"][person]
        if transaction["paidBy"] in paidFrom:
            paidFrom[transaction["paidBy"]] += sum
        else:
            paidFrom[transaction["paidBy"]] = sum

    # normalize paid and received amount of same person
    for person in paidTo:
        if person in paidFrom:
            if paidFrom[person] <= paidTo[person]:
                paidTo[person] -= paidFrom[person]
                # Remove person from list if amount value is 0
                del paidFrom[person]
            else:
                paidFrom[person] -= paidTo[person]
                paidTo[person] = 0

    # normalize received amount and paid amount
    for person in paidFrom:
        if person in paidTo:
            if paidTo[person] <= paidFrom[person]:
                paidFrom[person] -= paidTo[person]
                # Remove person from list amount value is 0
                del paidTo[person] #= 0
            else:
                paidTo[person] -= paidFrom[person]
                paidFrom[person] = 0
    # Return paidFrom and paidTo person's list with remaining amount
    return paidFrom, paidTo



# test case 1
transactions1 = [{ 	"paidBy": "A", 	"paidFor": { "B": 200 } 	},
{ 	"paidBy": "B", 	"paidFor": { "C": 100 } 	},
{ 	"paidBy": "C", 	"paidFor": { "A": 100 } 	}]

# test case 2
transactions2 = [{ 	"paidBy": "A", 	"paidFor": { "B": 100, "C": 50 } 	},
{ 	"paidBy": "A", 	"paidFor": { "C": 500 } 	},
{ 	"paidBy": "B", 	"paidFor": { "A": 150, "C": 200 } 	},
{ 	"paidBy": "C", 	"paidFor": { "A": 250, "B": 200 } 	}]

# Test Case Example
# If A is paying amount to B and C then one transcation would be 
# {"paidBy":"A", "paidFor":{"B":val1, "C":val2}}

# Call the function with passing array of transcation
paidFrom, paidTo = simplifyDebt(transactions2)

# print the personfrom and personTo with amount
for person1 in paidTo:
    for person2 in paidFrom:
        if paidTo[person1] >= paidFrom[person2]:
            # Print person name with its owes to person with amount
            print person1, "owes", person2, paidFrom[person2]
            paidTo[person1] -= paidFrom[person2]
            paidFrom[person2] = 0


