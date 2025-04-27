# 📊 COVID-19 Data Analysis & Visualization

This project presents an in-depth analysis and visualization of the COVID-19 pandemic using the **OWID (Our World in Data) COVID-19 Dataset**. It leverages `pandas`, `matplotlib`, `seaborn`, and `numpy` to explore case trends, death rates, vaccination efforts, and other key metrics across different countries and continents.

---

## 🗂️ Dataset

- **Source**: [Our World in Data - COVID-19](https://ourworldindata.org/covid-deaths)
- **File Used**: `owid-covid-dataset.csv`
- **Cleaned Output**: `Cleaned_Covid_Dataset.csv`

---

## 📦 Libraries Used

- `pandas` – Data manipulation and analysis  
- `numpy` – Numerical operations  
- `matplotlib` – Data visualization  
- `seaborn` – Statistical data visualization

---

## 🌍 Countries Analyzed

- India  
- United States  
- Brazil  
- United Kingdom  
- South Africa  

---

## 📈 Key Metrics Explored

- `new_cases_per_million`
- `total_cases_per_million`
- `new_deaths_per_million`
- `total_deaths_per_million`
- `total_vaccinations_per_hundred`
- `total_vaccinations`
- `new_tests`
- `hosp_patients_per_million`
- `reproduction_rate`
- `total_tests`
- `new_cases`
- `new_deaths`
- `stringency_index`

---

## 📊 Visualizations Included

### Line Charts
- New Cases per Million by Country  
- Total Cases per Million by Country  
- New Deaths per Million by Country  
- Total Deaths per Million by Country  
- Reproduction Rate Over Time  

### Scatter Plot
- Vaccination vs New Deaths per Million (India)  
  - Color represents `reproduction_rate`  
  - Size represents `stringency_index`

### Heatmap
- Correlation among different spread-related factors

### Bar Charts
- Total Deaths per Million by Continent  
- Total Cases per Million by Continent

### Boxplot
- Outlier detection in `new_cases` by continent (Log scale)

### Pairplot
- Visual relationships among:
  - `new_cases_per_million`
  - `new_deaths_per_million`
  - `total_vaccinations_per_hundred`
  - `stringency_index`

---

## 🧼 Data Cleaning & Transformation

- Handled missing values in important metrics using `fillna(0)`
- Filtered dataset for selected countries
- Converted date strings into datetime objects
- Saved cleaned dataset to CSV

---

## 📁 Output

- Multiple comparative visualizations (plots)
- Cleaned dataset as `Cleaned_Covid_Dataset.csv`
- Summary statistics and top 5 outlier entries

---

## 📊 Summary Insights

- Countries show diverse COVID-19 trends in both cases and death rates.
- Vaccination rollout and stringency measures influence death rates.
- Strong correlation observed between tests, restrictions, and case numbers.
- Outlier detection identifies critical case spikes.

---

## ▶️ How to Run

1. **Install Required Libraries**  
   ```bash
   pip install pandas numpy matplotlib seaborn
