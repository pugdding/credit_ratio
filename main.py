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