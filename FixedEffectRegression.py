import pandas as pd
import statsmodels.api as sm



df = pd.read_excel("GridExport.xlsx")

# Create a fixed effect model
# The fixed effect model is a regression model that includes a set of dummy variables, one for each individual in the sample.
# The dummy variables are used to control for the individual-specific effects, which are assumed to be constant over time.

columns_to_mean = ["FY0" , "FY1", "FY2", "FY3", "FY4", "FY5", "FY6", "FY7", "FY8" ,"FY9"]
df['FYmean'] = df[columns_to_mean].mean(axis=1)

mean_women_percentage = df["Women"].mean()
mean_FYmean = df["FYmean"].mean()

df["women_mean"] = mean_women_percentage
df["FYmean_mean"] = mean_FYmean

df["WM"] = df["Women"] - df["women_mean"]
df["FM"] = df["FYmean"] - df["FYmean_mean"]

# Create a fixed effect model
print(df.head())
model = sm.OLS(df.FM, df.WM)
results = model.fit()
print(results.summary())


# The coefficient is -0.0012, which means that for every 1% increase in the percentage of Women in a company, the average YTD decreases by 0.0012%.
# This is a small effect, the statistical significance is to be valued depending on our estimations