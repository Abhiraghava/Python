print("welcome to the tip calculator")
bill=float(input("what was the total bill? ₹"))
tip=int(input("how much tip u would like to give?10,12 or 13? :"))
people=int(input("how many people do you want to split the bill?"))
bill_with_tip=tip/100*bill+bill
bill_per_person=bill_with_tip/people
final_amount=round(bill_per_person,2)
print("each person have to pay:",final_amount)