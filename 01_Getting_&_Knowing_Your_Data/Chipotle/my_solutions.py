# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %% [markdown]
# # Ex2 - Getting and Knowing your Data
#
# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# %%
import pandas as pd

# %% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 
#
# ### Step 3. Assign it to a variable called chipo.

# %%
df_chipo = pd.read_csv(
    'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv',
    sep='\t'
)

# %% [markdown]
# ### Step 4. See the first 10 entries

# %%
df_chipo.head(10)

# %% [markdown]
# ### Step 5. What is the number of observations in the dataset?

# %%
# Solution 1
df_chipo.shape[0]

# %%
# Solution 2
len(df_chipo)

# %%
# Solution 3
df_chipo.info()

# %% [markdown]
# ### Step 6. What is the number of columns in the dataset?

# %%
df_chipo.shape[1]

# %% [markdown]
# ### Step 7. Print the name of all the columns.

# %%
df_chipo.columns

# %% [markdown]
# ### Step 8. How is the dataset indexed?

# %%
df_chipo.index

# %% [markdown]
# ### Step 9. Which was the most-ordered item? 

# %%
c = df_chipo.groupby(['item_name']).sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1)

# %% [markdown]
# ### Step 10. For the most-ordered item, how many items were ordered?

# %%
c = df_chipo.groupby(['item_name']).sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1)

# %% [markdown]
# ### Step 11. What was the most ordered item in the choice_description column?

# %%
c = df_chipo.groupby(['choice_description']).sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1)

# %% [markdown]
# ### Step 12. How many items were orderd in total?

# %%
df_chipo.quantity.sum()

# %% [markdown]
# ### Step 13. Turn the item price into a float

# %% [markdown]
# #### Step 13.a. Check the item price type

# %%
df_chipo.item_price.dtype

# %% [markdown]
# #### Step 13.b. Create a lambda function and change the type of item price

# %%
dollarizer = lambda x: float(x[1:])
df_chipo.item_price = df_chipo.item_price.apply(dollarizer)

# %% [markdown]
# #### Step 13.c. Check the item price type

# %%
df_chipo.item_price.dtype

# %% [markdown]
# ### Step 14. How much was the revenue for the period in the dataset?

# %%
'$' + str((df_chipo.quantity * df_chipo.item_price).sum())

# %% [markdown]
# ### Step 15. How many orders were made in the period?

# %%
df_chipo.order_id.nunique()
# df_chipo.order_id.value_counts().count()

# %% [markdown]
# ### Step 16. What is the average revenue amount per order?

# %%
# Solution 1
df_chipo['revenue'] = df_chipo.quantity * df_chipo.item_price
order_grouped = df_chipo.groupby(['order_id']).sum()
avg_revenue = order_grouped.mean()['revenue']
'$' + format(avg_revenue, '.2f')

# %%
# Solution 2
df_chipo['revenue'] = df_chipo.quantity * df_chipo.item_price
avg_revenue = df_chipo.groupby(['order_id']).sum().mean()['revenue']
'$' + format(avg_revenue, '.2f')

# %% [markdown]
# ### Step 17. How many different items are sold?

# %%
df_chipo.item_name.nunique()

# %%
