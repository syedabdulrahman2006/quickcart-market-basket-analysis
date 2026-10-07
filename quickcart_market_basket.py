import pandas as pd
from mlxtend.frequent_patterns import association_rules

data = pd.read_csv("frequent_itemsets.csv")

data["itemsets"] = data["itemsets"].apply(eval)

print(data.head())
print("Rows:", len(data))

rules = association_rules(
    data,
    metric="lift",
    min_threshold=1.0
)

print(rules.head())
print("Total rules:", len(rules))

strong_rules = rules[
    (rules["support"] > 0.05) &
    (rules["lift"] > 2)
]

strong_rules = strong_rules.sort_values("lift", ascending=False)

print("\nStrong Rules:")
print(strong_rules[[
    "antecedents",
    "consequents",
    "support",
    "confidence",
    "lift"
]].head(10))

strong_rules.to_csv("quickcart_strong_rules.csv", index=False)

print("\nSaved: quickcart_strong_rules.csv")