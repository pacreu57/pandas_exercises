# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %% [markdown]
# # Regiment
#
# ### Introduction:
# 
# Special thanks to: http://chrisalbon.com/ for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# %%
import pandas as pd

# %% [markdown]
# ### Step 2. Create the DataFrame with the following values:

# %%
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

# %% [markdown]
# ### Step 3. Assign it to a variable called regiment.
# #### Don't forget to name each column

# %%
regiment = pd.DataFrame(raw_data)

# %% [markdown]
# ### Step 4. What is the mean preTestScore from the regiment Nighthawks?  

# %%
regiment.groupby(['regiment']).mean().loc[['Nighthawks'], ['preTestScore']]

# %% [markdown]
# ### Step 5. Present general statistics by company

# %%
regiment.groupby(['company']).describe()

# %% [markdown]
# ### Step 6. What is the mean of each company's preTestScore?

# %%
regiment.groupby(['company']).mean().loc[:, ['preTestScore']]

# %% [markdown]
# ### Step 7. Present the mean preTestScores grouped by regiment and company

# %%
regiment.groupby(['regiment', 'company']).preTestScore.mean()

# %% [markdown]
# ### Step 8. Present the mean preTestScores grouped by regiment and company without heirarchical indexing

# %%
regiment.groupby(['regiment', 'company']).preTestScore.mean().unstack()

# %% [markdown]
# ### Step 9. Group the entire dataframe by regiment and company

# %%
regiment.groupby(['regiment', 'company']).mean()

# %% [markdown]
# ### Step 10. What is the number of observations in each regiment and company

# %%
regiment.groupby(['regiment', 'company']).size()

# %% [markdown]
# ### Step 11. Iterate over a group and print the name and the whole data from the regiment

# %%
for name, group in regiment.groupby('regiment'):
        print(name)
        print(group)

# %%
