# %%
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename="log.log", format='[%(asctime)s][%(levelname)s]%(message)s', level=logging.DEBUG)
logger.info("hellow")

# %%
import pandas as pd
import sqlite3

# %%
df = pd.read_csv("/Users/yahyeabdiasis/Downloads/BE0101D8_20241216-142116.csv")

# %%
df["�lder"] = df["�lder"].str.replace(" �r", "")

# %%
df

# %%
import pytest
def add_one(x):
    return x + 1
def test_add_one():
    assert add_one(3)==4

# %% [markdown]
# 

# %%
con = sqlite3.connect("min_databas.db")

# %%
df.to_sql("min_tabell", con, if_exists="replace")

# %%


# %%


# %%



