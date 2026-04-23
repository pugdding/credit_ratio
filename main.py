#import module
from data import Purchase
from data import account

#store purchases 
purchase_history=[
    Purchase("matcha","_____", 7.65)
]

#define helper functions 
def calculate_total_spending(): 
    total_cost=0
    #loop through purchase array
    for x in purchase_history: 
        total_cost+=x.cost

    
    #update information on the account
    account["total_balance"]+=total_cost

    #display 
    display_purchases()
    display_information()
    recommendation()



def calculate_utilization_ratio(): 
    return round(account["total_balance"] / account["total_credit"] * 100, 2)


#adding new purchase 
def add_new_purchase(purchase_obj):
    purchase_history.append(purchase_obj)
    #call to update total_balance 
    calculate_total_spending()




#display functions
def display_purchases(): 
    print(f"=== PURCHASE INFO =========================================================")
    for x in purchase_history: 
        print(f"{x.name} | ${x.cost}")

def display_information(): 
    print(f"=== SUMMARY =========================================================")
    print(f"Total Balance: ${account["total_balance"]}")
    print(f"Avaliable Balance: ${account["total_credit"] - account["total_balance"]}")
    print(f"Credit Ratio: {calculate_utilization_ratio()}%")
    print(f"Target Ratio: {account["target_utilization_ratio"]}%")

def recommendation(): 
    ratio_difference=account["target_utilization_ratio"] - calculate_utilization_ratio()
    print("=== RECOMMENDATIONS =========================================================")
    print(f"Ratio Difference: {ratio_difference}%")

    money_difference=round((ratio_difference/100) * account["total_credit"],2)

    if (ratio_difference > 0): 
        print(f"Spend ${money_difference} more", end="")
    elif (ratio_difference < 0): 
        print("Pay off x", end="")

    print(f" before the closing date to reach the target of {account["target_utilization_ratio"]}%!")

#sample run 
calculate_total_spending()

add_new_purchase(Purchase("chocolate cake", "a", 5.44))
