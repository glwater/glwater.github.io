# ----- Copy into bonds.py and run as `python bonds.py`
# For bond amount $xM, at r% for N years, 
# Calculate by year: Annual Payment, Interest Paid, Principal Paid, 
#                    Cumulative Interest Paid, and Remaining Balance.

import pandas as pd
import matplotlib.pyplot as plt

P = 27930000    # Principal amount
r = 4.5         # Annual interest rate in %
N = 25          # Amortization period in years
r = r / 100

def generate_bond_schedule(P, r, N):
    Myr = P * (r * (1 + r)**N) / ((1 + r)**N - 1)
    Bal = P
    I = 0
    schedule_data = []
    
    for year in range(1, N + 1):
        Iyr = Bal * r
        M = Myr - Iyr
        I += Iyr
        Bal -= M
        
        if Bal < 0:
            Bal = 0
            
        schedule_data.append({
            "Year": year,
            "Annual Payment": Myr,
            "Interest Paid": Iyr,
            "Principal Paid": M,
            "Cumulative Interest Paid": I,
            "Remaining Balance": Bal
        })

    df = pd.DataFrame(schedule_data)
    return df

df = generate_bond_schedule(P, r, N)
print("--- BOND AMORTIZATION SCHEDULE ---")
print(df.to_string(index=False, formatters={
    'Annual Payment': '{:,.0f}'.format,
    'Interest Paid': '{:,.0f}'.format,
    'Principal Paid': '{:,.0f}'.format,
    'Cumulative Interest Paid': '{:,.0f}'.format,
    'Remaining Balance': '{:,.0f}'.format
}))
