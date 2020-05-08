# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %% [markdown]
# # Ex2 - Filtering and Sorting Data
#
# # This time we are going to pull data directly from the internet.
# 
# ### Step 1. Import the necessary libraries

# %%
import pandas as pd

# %% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv). 
#
# ### Step 3. Assign it to a variable called euro12.

# %%
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
euro12 = pd.read_csv(url, delimiter=',')

# %% [markdown]
# ### Step 4. Select only the Goals column.

# %%
euro12['Goals']

# %% [markdown]
# ### Step 5. How many team participated in the Euro2012?

# %%
euro12['Team'].nunique()

# %% [markdown]
# ### Step 6. What is the number of columns in the dataset?

# %%
len(euro12.columns)

# %% [markdown]
# ### Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline

# %%
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]

# %% [markdown]
# ### Step 8. Sort the teams by Red Cards, then to Yellow Cards

# %%
discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)

# %% [markdown]
# ### Step 9. Calculate the mean Yellow Cards given per Team

# %%
round(discipline['Yellow Cards'].mean())

# %% [markdown]
# ### Step 10. Filter teams that scored more than 6 goals

# %%
euro12[euro12['Goals'] > 6]

# %% [markdown]
# ### Step 11. Select the teams that start with G

# %%
euro12[euro12['Team'].str.startswith('G')]

# %% [markdown]
# ### Step 12. Select the first 7 columns

# %%
euro12.iloc[:, 0:7]

# %% [markdown]
# ### Step 13. Select all columns except the last 3.

# %%
euro12.iloc[:, 0:-3]


# %% [markdown]
# ### Step 14. Present only the Shooting Accuracy from England, Italy and Russia

# %%
euro12.loc['England']

# %%
