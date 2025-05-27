class Payment:
    def process(self):
        return "Processing generic payment"

class PayPal(Payment):
    def process(self):  
        return "Processing PayPal payment"

print(Payment().process())  
print(PayPal().process())   
