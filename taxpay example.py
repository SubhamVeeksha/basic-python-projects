def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    # Pre-tax pay
    pay_pretax = num_hours * hourly_wage
    # After-tax pay
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax
aftertax=get_pay_with_more_inputs(40,15,0.12)

print(aftertax)
aftertax1=get_pay_with_more_inputs(40,24,0.22)
print(aftertax1)