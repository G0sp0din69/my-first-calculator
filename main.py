import biblia

print(""" 
Hi!
I am calculator, created by Mark Tvern.
Write integer and symbols to get a result.
""")
x = int(input("""
Write integer. 
1. Calculate the loan or mortgage. 
2. Go to solutions of equations.
Answer: """))
if x == 1:
    biblia.loanOrMortage()
if x == 2:
    biblia.equa()