import datetime

today=datetime.datetime.now()
date1=today.date()
time1=today.time()
fdate=date1.strftime("%d-%m-%y")
ftime=time1.strftime("%H:%M  %p")
qty=float(input("Enter the quantity of item sold: "))
val=float(input("Enter the value of item: "))
discount=float(input("Enter the discount percentage: "))
tax=float(input("Enter the tax: "))
amt=qty*val
discount_amt=(amt*discount)/100
sub_total=amt-discount_amt
tax_amt=(sub_total*tax)/100
total_amt=sub_total+tax_amt

print("****************BILL****************")
print(fdate,end="              ")
print(ftime)
print()
print(" Quality sold :    \t  ",qty)
print(" Price per item :   \t ",val)
print("\n\t \t    -----------------")
print(" Amount : \t        ",amt)
print(" Discount Total : \t ",discount_amt)
print("   \t  \t     ----------------")
print(" Discounted Total : \t",sub_total)
print(" Tax :\t     \t       +",tax_amt)
print("    \t  \t     -----------------")
print("Total amout to be paid  ",total_amt,"\n")