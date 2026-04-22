class creditCard: 
    def __init__(self, current_balance, max_credit): 
        self.current_balance=current_balance
        self.max_credit=max_credit 
    
class Purchase: 
    def __init__(self,name,desc,cost): 
        self.name=name 
        self.desc=desc
        self.cost=cost 

account={
    "name": "pudding", 
    "num_of_credit_card":1, 
    "total_balance":0,
    "total_credit":500,
    "credit_utilization":0,
}

#store purchases 
purchase_history=[
    Purchase("matcha","_____", "7.65"),
]

#define helper functions 
def calculate_total_spending(): 
    total_cost=0
    #loop through purchase array
    for x in purchase_history: 
        total_cost=x.cost
    
    #update information on the account
    account["total_balance"]= total_cost

    #return total cost 
    return total_cost 

def calculate_utilization_ratio(): 
    return (account["total_balance"] / account["total_credit"]) * 100
