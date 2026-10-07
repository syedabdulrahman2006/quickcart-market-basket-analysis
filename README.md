# QuickCart Market Basket Analysis

A market basket analysis project using Apriori Association Rule Mining to discover products that are frequently purchased together in QuickCart orders.

## Project Overview

The goal of this project is to identify product combinations and association rules that can help QuickCart with:

- Product bundling
- Cross-selling recommendations
- Shelf placement
- Understanding customer purchasing patterns

The dataset contains 5,000 orders, 60 unique SKUs, and 26,878 transaction line items.

## Technologies Used

- Python
- Pandas
- MLxtend
- Apriori
- Association Rule Mining

## Analysis

Frequent itemsets were analyzed using a minimum support of 2%.

Results:

- 256 frequent itemsets
- 980 association rules
- Strong rules filtered using:
  - Support > 5%
  - Lift > 2

## Key Metrics

### Support

Measures how frequently products appear together in the transactions.

### Confidence

Measures how often the consequent product is purchased when the antecedent product is purchased.

### Lift

Measures how much more frequently products occur together compared with random chance.

A lift greater than 1 indicates a positive association.

## Key Association Rules

| Product Association | Support | Confidence | Lift |
|---|---:|---:|---:|
| Ghee 500ml → Poha 500g | 14.68% | 86.05% | 5.07 |
| Hand Sanitizer 200ml → Face Wash 100ml | 13.18% | 79.30% | 5.05 |
| Instant Coffee 100g → Choco Cookies 150g | 15.20% | 85.88% | 4.84 |
| Potato Chips 90g → Cola 750ml | 19.74% | 90.38% | 4.18 |

## Business Applications

The discovered associations can be used for:

- Bundle Deals
- Cross-Selling
- Shelf Placement
- Product Recommendations

## Project Structure

```text
quickcart-market-basket/
│
├── quickcart_market_basket.py
├── frequent_itemsets.csv
├── quickcart_strong_rules.csv
├── QuickCart_MarketBasket_Project_Spec.pdf
└── README.md

## Connect With Me

- **GitHub:** https://github.com/syedabdulrahman2006/quickcart-market-basket-analysis.git
- **LinkedIn:** https://lnkd.in/p/d-7pzdkz

---

**Made by Syed Abdul Rahman**
