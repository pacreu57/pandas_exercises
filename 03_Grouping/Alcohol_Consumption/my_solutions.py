# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %% [markdown]
# # Ex - GroupBy

# ### Introduction:
# 
# GroupBy can be summarized as Split-Apply-Combine.
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# Check out this [Diagram](http://i.imgur.com/yjNkiwL.png)
#   
# ### Step 1. Import the necessary libraries

# %%
import pandas as pd

# %% [markdown]
# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv). 
#
# ### Step 3. Assign it to a variable called drinks.

# %%
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'
drinks = pd.read_csv(url, delimiter=',', index_col='country')

# %% [markdown]
# ### Step 4. Which continent drinks more beer on average?

# %%
drinks.groupby('continent').beer_servings.mean()

# %% [markdown]
# ### Step 5. For each continent print the statistics for wine consumption.

# %%
drinks.groupby('continent').wine_servings.describe()

# %% [markdown]
# ### Step 6. Print the mean alcohol consumption per continent for every column

# %%
drinks.groupby('continent').mean()

# %% [markdown]
# ### Step 7. Print the median alcohol consumption per continent for every column

# %%
drinks.groupby('continent').median()

# %% [markdown]
# ### Step 8. Print the mean, min and max values for spirit consumption.
# #### This time output a DataFrame

# %%
drinks.groupby('continent').agg({'spirit_servings': ['mean', 'min', 'max']})

# %%
