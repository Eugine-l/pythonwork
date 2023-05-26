Amount = int(input('Enter purchase amount: '))
if Amount>=1000:
    discount=0.05*Amount
    Payable_amount=Amount-discount
    print("discount", discount)
    print("Payable_amount",Payable_amount)
else:
 print("Amount",Amount)