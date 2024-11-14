def calculate_paye(taxable_income):
    if taxable_income <= 235000:
        return 0
    elif taxable_income <= 335000:
        return (taxable_income - 235000) * 0.10
    elif taxable_income <= 410000:
        return (taxable_income - 335000) * 0.20 + 10000
    elif taxable_income <= 10000000:
        return (taxable_income - 410000) * 0.30 + 25000
    else:
        return ((taxable_income - 410000) * 0.30 + 25000) + ((taxable_income - 10000000) * 0.10)

# Example usage
taxable_income = float(input("Enter your taxable income (UGX): "))
paye = calculate_paye(taxable_income)
print(f"The PAYE for a taxable income of {taxable_income} UGX is {paye} UGX")