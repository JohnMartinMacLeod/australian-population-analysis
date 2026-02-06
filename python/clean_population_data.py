import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"
output_path = BASE_DIR / "data" / "processed" / "clean_population_data.csv"

df1 = pd.read_csv(DATA_DIR / "population_1.csv")
df2 = pd.read_csv(DATA_DIR / "population_2.csv")

data_start_row = 9

df1_data = df1.iloc[data_start_row:].copy()
df2_data = df2.iloc[data_start_row:].copy()

df1_data = df1_data.rename(columns={df1_data.columns[0]: "year"})
df2_data = df2_data.rename(columns={df2_data.columns[0]: "year"})

df_combined = pd.concat(
    [df1_data, df2_data.drop(columns=["year"])],
    axis=1
)

long_df = df_combined.melt(
    id_vars=["year"],
    var_name="measure",
    value_name="population"
)

parts = long_df["measure"].str.split(";",expand=True)
long_df["sex"] = parts[1].str.strip()
long_df["age"] = parts[2].str.strip()
long_df = long_df.drop(columns=["measure"])
long_df["year"] = long_df["year"].str.split("-").str[1].astype(int)

long_df["age"] = long_df["age"].replace("100 and over", "100").astype(int)

long_df = long_df[["year", "sex", "age", "population"]]

long_df.to_csv(output_path, index=False)