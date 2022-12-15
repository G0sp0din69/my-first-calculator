def loanOrMortage():
    credit_min = float('inf')
    while True:
        print()
        money=int(input("Loan amount(Enter 0 to exit): "))
        if not money:
            break
        x=int(input("Loan rate: "))
        x=x/100

        years=float(input("For how many years: "))
        mounthpay =   (money * x * (1 + x) ** years) / (12 * ((1 + x) ** years- 1))
        print(f"Monthly payment: {mounthpay};")
        t_sum = mounthpay * years * 12
        credit_sum = (t_sum / money) * 100
        credit_sum_str = '%.f%%' % credit_sum
        print ('Amount for the entire period: %.f' % t_sum)
        print ('This will amount to', credit_sum_str, 'from the initial amount')
        if credit_sum < credit_min:
            credit_min = credit_sum
            money_result = money
            percent_result = x*100
            years_result = years
            month_pay_result = mounthpay
            t_sum_result = t_sum

        if credit_min < float('inf'):
            print ('\n' + 'The most profitable loan repayment percentage will be: ' + str(credit_min),
            '\n\n' + 'It was a loan on the following terms:',
            '\n' + 'Loan amount:', str(money_result),
            '\n' + 'Loan rate:', '%.f%%' % percent_result,
            '\n' + 'For how many years:', years_result,
            '\n' + 'Monthly payment: ', '%.f' % month_pay_result,
            '\n' + 'Amount for the entire period:', '%.f' % t_sum_result)
def equa():
    print("""
    What kind of equation do you want to solve?
    1. Quadratic equation.
    2. Linear equation.
    3. Matrix equation
    """)
    x = int(input("Enter a number: "))
    if x == 1:
        print("пошел нахуй")
    elif x == 2:
        print("пошел нахуй")
    elif x== 3:
        print("пошел нахуй")
    else:
        print("пошел нахуй это не число кретин дурак мудак козел блин")
