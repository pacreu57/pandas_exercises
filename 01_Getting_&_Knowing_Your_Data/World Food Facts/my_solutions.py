# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Exercise 1

# %% [markdown]
# ### Step 1. Go to https://www.kaggle.com/openfoodfacts/world-food-facts/data

# %% [markdown]
# ### Step 2. Download the dataset to your computer and unzip it.

# %% [markdown]
# ### Step 3. Use the tsv file and assign it to a dataframe called food

# %%
import pandas as pd

# %%
df_food = pd.read_csv(
    '../../datas/en.openfoodfacts.org.products.tsv',
    delimiter='\t'
)

# %% [markdown]
# ### Step 4. See the first 5 entries

# %%
df_food.head()

# %% [markdown]
# ### Step 5. What is the number of observations in the dataset?

# %% 356027 observations
df_food.shape[0]

# %% [markdown]
# ### Step 6. What is the number of columns in the dataset?

# %% 163 columns
df_food.shape[1]

# %% [markdown]
# ### Step 7. Print the name of all the columns.

# %%
df_food.columns

# %% [markdown]
# ### Step 8. What is the name of 105th column?

# %% '-glucose_100g'
df_food.columns[104]

# %% [markdown]
# ### Step 9. What is the type of the observations of the 105th column?

# %% 'float64'
df_food.dtypes[104]

# %% [markdown]
# ### Step 10. How is the dataset indexed?

# %%


# %% [markdown]
# ### Step 11. What is the product name of the 19th observation?

# %% 'Lotus Organic Brown Jasmine Rice'
df_food.product_name.iloc[18]

# %%
