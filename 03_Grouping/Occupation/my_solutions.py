# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %% [markdown]
# # Occupation
#
# ### Introduction:
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# %%
import pandas as pd

# %% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 

# ### Step 3. Assign it to a variable called users.

# %%
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users = pd.read_csv(url, sep='|', index_col='user_id')

# %% [markdown]
# ### Step 4. Discover what is the mean age per occupation

# %%
users.groupby('occupation').age.mean()

# %% [markdown]
# ### Step 5. Discover the Male ratio per occupation and sort it from the most to the least

# %%
def gender_to_numeric(gender):
    if gender == 'M':
        return 1
    else:
        return 0

users['gender_n'] = users['gender'].apply(gender_to_numeric)

ratio = 100 * users.groupby('occupation').gender_n.sum() / users.occupation.value_counts()

ratio.sort_values(ascending=False)

# %% [markdown]
# ### Step 6. For each occupation, calculate the minimum and maximum ages

# %%
users.groupby('occupation').age.agg(['min', 'max'])

# %% [markdown]
# ### Step 7. For each combination of occupation and gender, calculate the mean age

# %%
users.groupby(['occupation', 'gender']).age.mean().unstack()

# %% [markdown]
# ### Step 8.  For each occupation present the percentage of women and men

# %%
gender_occup = users.groupby(['occupation', 'gender']).agg({'gender': 'count'})
occup_count = users.groupby('occupation').count()
occup_gender = 100 * gender_occup / occup_count
occup_gender.loc[:, 'gender'].unstack()

# %%
