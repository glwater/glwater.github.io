---
layout: page
title: "Grand Lakes: A Community Asking Who Is Accountable for Its Water Districts<br>
        Part 11: Grand Lakes MUD No. 2 and the $46.6 million bond episode"
tags: [Grand Lakes, Katy, Texas, board, consultant, bonds]
categories: [Governance, Finances]
preview: "Grand Lakes residents raise serious questions about the operation of the four water districts (MUD4, MUD1, MUD2, and WCID) and the conduct of the different consultants (attorney, operator, engineer, bookkeeper, auditor, financial advisor, tax collector, etc.) serving our districts. This article documents how the MUD2 residents / taxpayers managed to defeat a questionable bond scheme that would have made the consultants serving the district in control of the district and its residents for another 40 years."
prvimg: "/assets/imgs/money.jpg" 
date: 2026-10-25
katex: true
---

### Why It Matters
The Grand Lakes community has already seen how consequential the questions of transparency, fiduciary duties, lawful governance, and compliance with the law can become.

We, the residents / taxpayers of Grand Lakes MUD No. 2, managed to defeat a 2026 bond election involving proposed authorization for a total out-of-pocket cost of \$46.6 million (\$27.93 million at 4.5% for 25 years). On April 20, 2026, just 12 days before election day, the MUD attorney amended the the bond-election order, changing a \$5.25 million figure to \$15.25 million. 

Whether every aspect of the bond proposal was lawful and justified is a matter for appropriate legal and governmental review. But the broader lesson is clear: **Residents must scrutinize proposed debt before it is approved—not after it becomes a 20-, 30-, or 40-year obligation.** The community cannot afford to treat tens of millions of dollars of proposed debt as merely another agenda item. This message must be appreciated, and complied with, by the boards and consultants alike.

### 💰 ✏️ 📊 Defeating the \$46.6M Illusion: Why Grand Lakes Said "No" on May 2, 2026
On **May 2, 2026**, our community made history by soundly defeating a massive **\$46.6 Million MUD bond proposal**. Private service firms and proponents tried to market this debt as a seamless investment into our future. What they hid in the fine print was the true structural anatomy of a municipal bond.

To understand why this was a bad deal for taxpayers, we analyzed the actual 25-year amortization numbers from **MUD2's existing \$27.93M bond layout at 4.5% interest**. The trajectory is staggering.

### The 15-Year Inflection Trap
When a MUD board passes a multi-million dollar bond, they lock residents into a generation of debt. As shown in the payment breakdown above, it takes **10 years** of writing annual **\$1.86 Million checks** before our community's tax payments finally shift to counting as 50% toward the principal balance. Prior to then, we are effectively just paying off corporate bank interest. 

By the time we hit that 15-year cross-over point, we will still require another **10 full years** of tax assessments to clear a remaining balance of **\$15 Million**. This is why our watchdog coalition stood firm on May 2, 2026. If we do not provide independent oversight over how these infrastructure funds are requested and handled, private entities exploit our water districts to lock us into cycles of high-interest structural debt.

<div align="left">
  <img src="/assets/docs/gl2bonds.png" alt="MUD Bond Repayment" width="95%">
  <p><i>Figure 1: Notice how the red interest payments drain our tax dollars for a decade before a single dollar effectively impacts the core principal.</i></p>
  <p><i>Figure 2: The Intersect of Debt. At Year 15, we have spent $14.99M on pure interest—yet we still owe $14.98M on the actual original balance to pay over 10 more years.</i></p>
</div>

### 💡 Glossary of Bond Terms
> 📌 **Bonds**
> Bonds are debt instruments issued for the purpose of acquiring investor funds for a certain period of time. In return, the bondholders earn periodic interest as payments.
>
> 📌 **Bondholders** 
> Bondholders are the lenders or investors.
>
> 📌 **Bond issuers**
> Bond issuers are the borrowers. In our case, this is the MUD.
>
> 📌 **Principal Balance**
> The actual, base amount of money that the MUD borrows to fund infrastructure projects. For example, in MUD2's current bond, the original principal balance was **\$27.93 Million**. Our payments only reduce our overall debt when they are applied directly to this balance.
>
> 📌 **Amortization Schedule**
> A complete chronological table showing exactly how each monthly or annual tax payment is split between paying off the bank's interest versus lowering the remaining principal debt over the life of the bond (25, 30, or 40 years).
>
> 📌 **Inflection Point**
> The specific calendar year in a bond's lifetime where our annual tax money finally shifts from mostly enrichment for financial lenders (interest) to mostly paying down the community's structural debt balance (principal). In our example, this would have been year 15.
>
> 📌 **Maturity**
> Maturity (or maturity date) is the date by which the bond (principal and interest) must be fully paid off.

### <img src="/assets/imgs/circig.svg"> 📝 📊 Interested in the Code and Data?
<div class ="block" style="margin-bottom: 16px;">
• <a href="{{ '/assets/docs/bonds.py' | relative_url }}"> Python code (.py).</a>  <br>
• <a href="{{ '/assets/docs/gl2bonds.pdf' | relative_url }}"> Bond Amortization Data (.pdf).</a>
</div>

### Accuracy Check
<blockquote markdown="1">
A simple and rough accuracy check shows that the interest amount fits the amortization model.  

P = \$27,930,000; r = 4.5% / 12 = 0.00375; n = 25 years x 12 = 300 months.  

For monthly payments due at the end of the period:  
• M = \$155,244 per month.  
• Out\-of\-pocket Cost = M x n = \$46,573,200.  
• Total Interest Paid = (M x n) - P = \$18,643,200.

```math 
  M = \frac{P \cdot r \cdot (1+r)^n}{(1+r)^n-1} 
```

For monthly payments due at the beginning of the period:  
• M = \$154,664 per month.  
• Out\-of\-pocket Cost = M x n = \$46,399,206.  
• Total Interest Paid = (M x n) - P = \$18,469,206.

```math 
  M = \frac{P \cdot r \cdot (1+r)^{n-1}}{(1+r)^n-1} 
```

</blockquote>
