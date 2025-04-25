
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("C:\\Users\\hp\\Downloads\\owid-covid-dataset.csv")
data["date"] = pd.to_datetime(data["date"])


print("Available Columns in Dataset:\n", data.columns.tolist())

# Define metrics and countries
metrics = [
    "new_cases_per_million", "total_cases_per_million", "new_deaths_per_million", 
    "total_deaths_per_million",  "total_vaccinations_per_hundred", "total_vaccinations",
    "new_tests",  "hosp_patients_per_million", "reproduction_rate", "total_tests",
    "new_cases", "new_deaths", "stringency_index"
]
countries = ["India", "United States", "Brazil", "United Kingdom", "South Africa"]

# Handle null values
print("Null Value Counts:\n", data.isnull().sum())
for col in metrics:
    if col in data.columns:
        data[col] = data[col].fillna(0)
    else:
        print(f"Warning: Column '{col}' not found in dataset.")


country_data = data[data["location"].isin(countries)]

#Country-Wise Trends for Per-Million Metrics

plt.figure(figsize=(14, 8))
for country in countries:
    country_subset = country_data[country_data["location"] == country]
    plt.plot(country_subset["date"], country_subset["new_cases_per_million"], label=country)
plt.title("New Cases per Million by Country", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("New Cases per Million", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
#plt.show()


plt.figure(figsize=(14, 8))
for country in countries:
    country_subset = country_data[country_data["location"] == country]
    plt.plot(country_subset["date"], country_subset["total_cases_per_million"], label=country)
plt.title("Total Cases per Million by Country", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total Cases per Million", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
#plt.show()


plt.figure(figsize=(14, 8))
for country in countries:
    country_subset = country_data[country_data["location"] == country]
    plt.plot(country_subset["date"], country_subset["new_deaths_per_million"], label=country)
plt.title("New Deaths per Million by Country", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("New Deaths per Million", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
#plt.show()


plt.figure(figsize=(14, 8))
for country in countries:
    country_subset = country_data[country_data["location"] == country]
    plt.plot(country_subset["date"], country_subset["total_deaths_per_million"], label=country)
plt.title("Total Deaths per Million by Country", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total Deaths per Million", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
#plt.show()


india_data = data[data["location"] == "India"]


# Reproduction Rate Over Time
plt.figure(figsize=(14, 8))
for country in countries:
    country_subset = country_data[country_data["location"] == country]
    plt.plot(country_subset["date"], country_subset["reproduction_rate"], label=country)
plt.title("Reproduction Rate Over Time by Country", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Reproduction Rate", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)


#Vaccination vs Mortality (India)
plt.figure(figsize=(10, 6))
sns.scatterplot(x="total_vaccinations_per_hundred", y="new_deaths_per_million", data=india_data, color="purple")
plt.title("Total Vaccinations per Hundred vs. New Deaths per Million in India", fontsize=14)
plt.xlabel("Total Vaccinations per Hundred", fontsize=12)
plt.ylabel("New Deaths per Million", fontsize=12)
#plt.show()

#Factors Influencing Spread
factors_data = data[["new_cases_per_million", "new_deaths_per_million", "new_tests", 
                    "hosp_patients_per_million", "stringency_index"]].dropna()
plt.figure(figsize=(10, 8))
sns.heatmap(factors_data.corr(), annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlation of Factors Influencing COVID-19 Spread", fontsize=14)
#plt.show()

#Regional Differences
continent_data = data.groupby("continent")[["total_cases_per_million", "total_deaths_per_million"]].mean().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x="continent", y="total_deaths_per_million", hue="continent", data=continent_data, palette="muted", legend=False)
plt.title("Average Total Deaths per Million by Continent", fontsize=14)
plt.xlabel("Continent", fontsize=12)
plt.ylabel("Total Deaths per Million", fontsize=12)
#plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x="continent", y="total_cases_per_million", hue="continent", data=continent_data, palette="pastel", legend=False)
plt.title("Average Total Cases per Million by Continent", fontsize=14)
plt.xlabel("Continent", fontsize=12)
plt.ylabel("Total Cases per Million", fontsize=12)
#plt.show()

#Outlier Detection

Q1 = data["new_cases"].quantile(0.25)
Q3 = data["new_cases"].quantile(0.75)
IQR = Q3 - Q1
outliers = data[(data["new_cases"] > (Q3 + 1.5 * IQR)) | (data["new_cases"] < (Q1 - 1.5 * IQR))]
print(f"Number of outliers in new cases: {len(outliers)}")
plt.figure(figsize=(10, 6))
sns.boxplot(x="continent", y="new_cases", legend=False, hue="continent",  data=data, palette="pastel")
plt.title("Boxplot of New Cases by Continent (Outlier Detection)", fontsize=14)
plt.xlabel("Continent", fontsize=12)
plt.ylabel("New Cases", fontsize=12)
plt.yscale("log")
#plt.show()

#Pairplot
pairplot_metrics = ["new_cases_per_million", "new_deaths_per_million", 
                   "total_vaccinations_per_hundred", "stringency_index"]
data_subset = country_data[["location"] + pairplot_metrics].dropna()

sns.pairplot(data=data_subset, hue="location", palette="Set2", diag_kind="kde")
plt.suptitle("Pairplot of COVID-19 Metrics (All Years)", y=1.02, fontsize=14)
plt.show()

 
print("\nSummary Statistics for New Cases per Million:")
print(data["new_cases_per_million"].describe())
print("\nTop 5 Outliers in New Cases per Million:")
print(data[["location", "date", "new_cases_per_million"]].sort_values(by="new_cases_per_million", ascending=False).head())


data.to_csv("C:\\Users\\hp\\Downloads\\Cleaned_Covid_Dataset.csv")

