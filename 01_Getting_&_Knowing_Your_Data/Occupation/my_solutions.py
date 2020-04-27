# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %% [markdown]
# # Ex3 - Getting and Knowing your Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# %%
import pandas as pd

# %% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user).

# %%
 
# %% [markdown]
# ### Step 3. Assign it to a variable called users and use the 'user_id' as index

# %% Solution 1
users = pd.read_csv(
    'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user',
    delimiter='|',
    index_col='user_id'
)

# %% [markdown]
# ### Step 4. See the first 25 entries

# %%
users.head(25)

# %% [markdown]
# ### Step 5. See the last 10 entries

# %%
users.tail(10)

# %% [markdown]
# ### Step 6. What is the number of observations in the dataset?

# %%
len(users)

# %% [markdown]
# ### Step 7. What is the number of columns in the dataset?

# %%
len(users.columns)

# %% [markdown]
# ### Step 8. Print the name of all the columns.

# %%
users.columns

# %% [markdown]
# ### Step 9. How is the dataset indexed?

# %%
users.index

# %% [markdown]
# ### Step 10. What is the data type of each column?

# %%
users.dtypes

# %% [markdown]
# ### Step 11. Print only the occupation column

# %%
users.occupation

# %% [markdown]
# ### Step 12. How many different occupations are in this dataset?

# %%
users.occupation.nunique()

# %% [markdown]
# ### Step 13. What is the most frequent occupation?

# %%
users.occupation.value_counts().index[0]

# %% [markdown]
# ### Step 14. Summarize the DataFrame.

# %% By default, only the numeric colomns are summarized
users.describe()

# %% [markdown]
# ### Step 15. Summarize all the columns

# %%
users.describe(include='all')

# %% [markdown]
# ### Step 16. Summarize only the occupation column

# %%
users.occupation.describe()

# %% [markdown]
# ### Step 17. What is the mean age of users?

# %%
round(users.age.mean())

# %% [markdown]
# ### Step 18. What is the age with least occurrence?

# %%
age_occurrences = users.age.value_counts()
least_occurence = age_occurrences.min()
age_occurrences.where(age_occurrences == least_occurence).dropna()

# %%
