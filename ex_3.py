age=input("what is your age :")
age_int=int(age)
years_remaining=90-age_int
days_remaining=years_remaining*365
months_remaining=years_remaining*12
weeks_remaining=years_remaining*52
txt=f"you have {years_remaining}years,{days_remaining}days,{months_remaining}months,{weeks_remaining}weeks left in your life if you are alive until 90years"
print(txt)