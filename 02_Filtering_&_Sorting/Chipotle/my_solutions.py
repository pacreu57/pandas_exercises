# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %% [markdown]
# # Ex1 - Filtering and Sorting Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# %%
import pandas as pd

# %% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# ### Step 3. Assign it to a variable called chipo.

# %%
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, delimiter='\t')

# %% [markdown]
# ### Step 4. How many products cost more than $10.00?

# %% Transform the item_price to a float (Solution 1)
dollar_to_float = lambda x: float(x[1:])
chipo.item_price = chipo.item_price.apply(dollar_to_float)

# %% Transform the item_price to a float (Solution 2)
prices = [float(value[1:]) for value in chipo.item_price]
chipo.item_price = prices

# %% 
chipo_products = chipo.drop_duplicates(['item_name'])
chipo_products['price_per_item'] = chipo_products.item_price / chipo_products.quantity
len(chipo_products[chipo_products.price_per_item > 10.0])

# %% [markdown]
# ### Step 5. What is the price of each item? 
# ###### print a data frame with only two columns item_name and item_price

# %%
chipo_products[['item_name', 'price_per_item']]

# %% [markdown]
# ### Step 6. Sort by the name of the item

# %%
chipo_products_2 = chipo_products[['item_name', 'price_per_item']]
chipo_products_2.sort_values(by='item_name')

# %% [markdown]
# ### Step 7. What was the quantity of the most expensive item ordered?

# %%
chipo.sort_values(by='item_price', ascending=False).head(1)

# %% [markdown]
# ### Step 8. How many times was a Veggie Salad Bowl ordered?

# %%
chipo_salad = chipo[chipo.item_name =='Veggie Salad Bowl']
chipo_salad.quantity.sum()

# %% [markdown]
# ### Step 9. How many times did someone order more than one Canned Soda?

# %%
chipo_soda = chipo[chipo.item_name =='Canned Soda']
len(chipo_soda[chipo_soda.quantity > 1])

# %%
