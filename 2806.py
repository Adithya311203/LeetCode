def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        x=purchaseAmount//10
        y=math.ceil(purchaseAmount/10)
        print(x*10,y*10)
        a=0
        if abs(x*10-purchaseAmount)<abs(y*10-purchaseAmount):
            a=x*10
        else:
            a=y*10
        return 100-a
    