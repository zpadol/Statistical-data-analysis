# Multivariate analysis of quality of life in Polish voivodeships (2025)

## Project description

**Why multivariate analysis?**
Quality of life and socio-economic development cannot be captured by a single indicator (e.g. wages alone). They depend on many dimensions at once: labour market, housing, environment, safety, entrepreneurship, and more. Multivariate methods combine several indicators into one synthetic measure (linear ordering) and group similar regions together (cluster analysis).

**What is studied?**
The project compares the 16 Polish voivodeships in terms of quality of life and level of socio-economic development. It is inspired by the article *"Wielowymiarowe ujęcie zróżnicowania poziomu jakości życia w województwach w Polsce"* by E. Roszko-Wójtowicz and M. M. Grzelak (2018), updated with 2025 data and extended with additional methods.

**Data**
- 9 diagnostic variables from Statistics Poland (GUS, Local Data Bank), one per quality-of-life domain: green areas share, dust emissions, gross wages, investment expenditure per capita, unemployment rate, crimes per 1000 inhabitants, businesses per 1000 inhabitants, dwellings completed per 1000 inhabitants, population density.
- 16 voivodeships, year 2025.
- After exploratory analysis, 2 variables were removed: gross wages (coefficient of variation below 10%) and green areas share (correlation with population density above 0.9). 7 variables remain.

**What was done**
1. Selection of variables and classification into stimulants and destimulants.
2. Exploratory data analysis (descriptive statistics, correlation matrix).
3. Standardization and weights based on squared correlation coefficients.
4. Two linear ordering methods: sum of standardized values (non-reference method) and Hellwig's taxonomic measure (reference method). Rankings were compared with the Spearman correlation.
5. Cluster analysis on standardized data: k-means (partitioning) and Ward's method (hierarchical). The number of clusters was chosen using the elbow method, Silhouette and Calinski-Harabasz indices, and the dendrogram.

**Main conclusions**
- Both rankings are highly consistent (Spearman correlation about 0.95). Mazowieckie ranks first and Warmińsko-mazurskie last in both methods; the same five voivodeships are at the top (Mazowieckie, Wielkopolskie, Pomorskie, Małopolskie, Dolnośląskie).
- The Mazowieckie result is probably inflated by the situation of Warsaw.
- Cluster analysis suggests 3 groups (more developed regions, less developed regions, and Śląskie as an outlier due to its extreme emissions and density). The structure is weak (Silhouette about 0.32), so the clusters should be treated as tendencies rather than sharply separated groups.
- Results depend on the choice of weights and are sensitive to outliers (Śląskie, Mazowieckie) because of the small sample (n = 16).

## Repository files

1. **`Analiza wielowymiarowa.docx`** – project report: aim, variables, EDA, linear ordering, cluster analysis, results and summary.
2. **`Same_Dane_Bazowe.xlsx`** – raw data: all 9 diagnostic variables for 16 voivodeships (GUS), before any selection.
3. **`Porządkowanie_liniowe.xlsx`** – linear ordering calculations: descriptive statistics, correlation matrix, variable weights, standardization, both methods (sum of standardized values, Hellwig), final indices and ranks.
4. **`Dane_Analiza_Skupien.xlsx`** – standardized data of the 7 selected variables used as input for cluster analysis.
5. **`analiza-skupien.py`** – Python code for cluster analysis (k-means, Ward, elbow method, Calinski-Harabasz and Silhouette indices, dendrogram).

## How to run

```bash
pip install pandas numpy scikit-learn scipy matplotlib openpyxl
python analiza-skupien.py
```

Place `Dane_Analiza_Skupien.xlsx` in the same folder as the script.
