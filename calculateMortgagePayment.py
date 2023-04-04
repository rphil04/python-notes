def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def calculate_down_payment(sales_price, down_payment_percentage):
    return sales_price * down_payment_percentage


def calculate_loan_amount(sales_price, down_payment):
    return sales_price - down_payment


def calculate_origination_fee(loan_amount):
    # Calculate origination fee as 1% of the loan amount
    return loan_amount * 0.01


def calculate_title_insurance(sales_price):
    # Calculate title insurance as 0.5% of the sales price
    return sales_price * 0.005


def calculate_escrow(loan_amount):
    # Calculate escrow as 1% of the loan amount
    return loan_amount * 0.01


def calculate_recording_fees():
    # Fixed recording fees of $250
    return 250


def calculate_discounts(discount_points, discount_dollars, loan_amount):
    # Calculate total discount amount
    discount_amount = discount_dollars + (discount_points * loan_amount / 100)
    return discount_amount


def calculate_total_closing_costs(loan_amount, sales_price, discount_points, discount_dollars):
    # Calculate all closing costs
    origination_fee = calculate_origination_fee(loan_amount)
    title_insurance = calculate_title_insurance(sales_price)
    escrow = calculate_escrow(loan_amount)
    recording_fees = calculate_recording_fees()
    discounts = calculate_discounts(discount_points, discount_dollars, loan_amount)
    return origination_fee + title_insurance + escrow + recording_fees - discounts


def calculate_monthly_payment(loan_amount, interest_rate, loan_term):
    # Calculate monthly mortgage payment using the formula for a fixed rate mortgage
    if loan_amount <= 0:
        return 0
    monthly_interest_rate = interest_rate / 12
    num_payments = loan_term * 12
    return (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)


def format_currency(value):
    # Format a number as a currency string
    return f"${value:,.2f}"


# Prompt the user for input
sales_price = get_float_input("Enter the sales price of the house: ")
down_payment_percentage = get_float_input("Enter the down payment percentage as a decimal (e.g. 0.2 for 20%): ")
interest_rate = get_float_input("Enter the interest rate as a decimal (e.g. 0.06 for 6%): ")
loan_term = get_int_input("Enter the loan term in years (e.g. 30): ")
discount_dollars = get_float_input("Enter any additional discount in dollars, or 0 for no additional discount: ")
discount_points = get_float_input("Enter the discount points as a decimal (e.g. 0.5 for half a point), or 0 for no discount: ")

# Calculate various values based on input
down_payment = calculate_down_payment(sales_price, down_payment_percentage)
loan_amount = calculate_loan_amount(sales_price, down_payment)
total_discounts = calculate_discounts(discount_points, discount_dollars, loan_amount)
closing_costs = calculate_total_closing_costs(loan_amount, sales_price, discount_points, discount_dollars)
monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_term)

# Output the results
print("\nMORTGAGE DETAILS")
print(f"Sales price: {format_currency(sales_price)}")
print(f"Down payment ({down_payment_percentage * 100}%): {format_currency(down_payment)}")
print(f"Loan amount: {format_currency(loan_amount)}")
print(f"Interest rate: {interest_rate * 100:.2f}%")
print(f"Loan term: {loan_term} years")
print(f"Discount points: {discount_points:.2f}")
print(f"Discount dollars: {format_currency(discount_dollars)}")
print(f"Total discounts: {format_currency(total_discounts)}")

print("\nCLOSING COSTS")
print(f"Origination fee: {format_currency(calculate_origination_fee(loan_amount))}")
print(f"Title insurance: {format_currency(calculate_title_insurance(sales_price))}")
print(f"Escrow: {format_currency(calculate_escrow(loan_amount))}")
print(f"Recording fees: {format_currency(calculate_recording_fees())}")
print(f"Discounts: -{format_currency(total_discounts)}")
print(f"Total closing costs: {format_currency(closing_costs)}")

print("\nMONTHLY PAYMENT")
print(f"Monthly payment: {format_currency(monthly_payment)}")
