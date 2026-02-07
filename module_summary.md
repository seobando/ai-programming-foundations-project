# Module Summary — Data Workflow Project

**Author:** Sebastian Obando Morales  
**Module:** AI Programming Foundations — Capstone Project 1

---

## Overview

This report summarizes a data workflow project built in **data_workflow.ipynb**. The project uses the **NYC Airbnb Listings** dataset ([Kaggle — New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)) to explore which features are most relevant to listing price. The workflow includes ingestion, cleaning, exploratory analysis, visualizations, and a written summary. The notebook is structured by the project tasks (Tasks 1, 3–8) and is intended as a reproducible foundation for future modeling.

---

## Dataset Description

The dataset represents Airbnb listings in New York City, made available by the Inside Airbnb project and hosted on Kaggle. It is a cross-sectional snapshot of listings with many attributes per listing. After loading, the raw data has on the order of tens of thousands of rows and dozens of columns (e.g. 30,000+ rows and 80+ columns in the version used). Key variables used in this workflow include: **price** (target), **bedrooms**, **bathrooms**, **number_of_reviews**, **accommodates**, **latitude**, **longitude**, **neighbourhood**, **property_type**, and various amenity flags (e.g. parking, TV, AC). The data includes both numeric and categorical variables; some columns have missing values. The dataset meets the project requirements (200+ rows, 5+ columns, CSV, academic use).

---

## Workflow Description (High Level)

The workflow in the notebook follows a standard data-science pipeline:

1. **Ingestion** — The dataset is loaded with Pandas from a CSV file. The first rows are displayed to confirm successful load and column structure.
2. **Cleaning** — Two cleaning functions are defined and applied: (i) removal of extreme price outliers (e.g. above the 99th percentile), and (ii) dropping rows with missing values in key numeric columns (e.g. price, bedrooms, bathrooms, latitude, longitude). This yields a cleaned dataframe used for the rest of the analysis.
3. **Exploratory analysis** — An EDA function (`run_eda_summary`) computes summary statistics for selected numeric columns and correlation of all numeric columns with price. The results are displayed and used to guide which variables to emphasize in visualizations.
4. **Visualizations** — At least three figures are produced with Matplotlib/Seaborn, each with a title and labeled axes: e.g. marginal distributions of key variables (histograms), share of listings by bedroom count, and price versus key variables (boxplots or scatter). Additional plots (e.g. price vs. longitude by bedrooms) support the narrative.
5. **Summary** — A final Markdown section (Task 8) describes what was learned, interesting patterns, limitations and assumptions, and anything surprising or unclear.

---

## Key Decisions and Assumptions

**Cleaning choices**

- **Price outliers:** Rows above the 99th percentile of price were removed to reduce the influence of very high or possibly erroneous values on summaries and future models. This choice is appropriate when the goal is to model “typical” listings; it can underrepresent the high-end segment [1].
- **Missing values:** Rows with missing values in key numeric columns were dropped so that correlation and plots use complete cases only. This assumes that missingness, while not necessarily random, is acceptable to handle by listwise deletion for this exploratory phase; more advanced methods (e.g. imputation) could be considered for production modeling [2].

**EDA focus**

- EDA focused on numeric variables and their correlation with price. Location (latitude/longitude, neighbourhood) and property type were also examined in the notebook. The EDA function restricts correlation to numeric columns to avoid errors and to align with best practice (e.g. Pearson correlation for numeric data).

**What each plot was designed to show**

- **Figure 1 (marginal distributions):** Shape and spread of price, bedrooms, bathrooms, and number_of_reviews (e.g. right skew, spikes at round prices).
- **Figure 2 (% listings by bedrooms):** Distribution of listing size (bedroom count) in percentage terms.
- **Figure 3 (price vs. key variables):** How median (or central) price varies across bedrooms, bathrooms, number_of_reviews, or similar variables (boxplots or analogous plots).
- **Additional plot (price vs. longitude by bedrooms):** Relationship between location (longitude), price, and listing size (bedrooms), illustrating that price and location are related and that the relationship may differ by size.

---

## Results and Interpretation

- **Price and size:** Price is positively associated with accommodates, bedrooms, and bathrooms. Median price tends to increase with number of bedrooms and bathrooms; the relationship is roughly linear for bedrooms in the main range of the data.
- **Price and location:** Longitude (and implicitly neighbourhood) is related to price; certain areas (e.g. Manhattan, parts of Brooklyn) show higher prices. The relationship is not purely linear, which would motivate location-aware or non-linear modeling in a later stage.
- **Distribution of price:** The price distribution is right-skewed with spikes at round numbers (e.g. 50, 100, 150), consistent with human-entered listing prices.
- **Interactions:** The notebook discusses interaction effects (e.g. parking and price by neighbourhood), showing that some overall correlations can change or reverse when conditioning on location.

These results are reflected in the notebook’s Task 8 summary and in the figures referenced above (Figure 1, Figure 2, Figure 3, and the price–longitude plot).

---

## Responsible Practice (Bias and Data Quality)

Cleaning and data handling can introduce bias or misleading results in several ways:

- **Selection bias:** Dropping rows with missing values or removing high-price outliers can make the sample unrepresentative of the full market (e.g. undercounting certain neighbourhoods or property types if missingness is systematic). To reduce this risk, we document exactly which rows are dropped and why; for a next step, we would consider missingness patterns (e.g. by neighbourhood) and possibly imputation or stratified analysis.
- **Measurement bias:** If “price” in the dataset does not reflect actual transaction prices (e.g. list price only), conclusions about “what drives price” may not generalize to realized revenue. We use the variable as provided and state this in the summary.
- **Reproducibility and transparency:** All cleaning steps are implemented in documented functions and applied in a fixed order so that others can reproduce and critique the pipeline. This aligns with recommendations for reproducible and ethical data science [1], [2].

---

## Reproducibility

Someone else can rerun this work as follows:

1. **Environment:** Install dependencies with `pip install -r requirements.txt` (see README). The project includes a `requirements.txt` generated from the working environment (e.g. via `pip freeze > requirements.txt`).
2. **Data:** Obtain the NYC Airbnb dataset from the link above and place the CSV in the path used in the notebook (or edit the load cell).
3. **Execution:** Open `data_workflow.ipynb` in Jupyter (or a compatible environment), select the same Python environment used to install requirements, and run all cells in order.
4. **Version control:** The project is maintained in a Git repository (e.g. **ai-programming-foundations-project**) with multiple commits and at least one additional branch, so progress and alternatives are traceable.

---

## Sources and Citations

[1] Pandas Development Team. *Pandas documentation: User Guide.* 2024.  
    https://pandas.pydata.org/docs/user_guide/index.html  

[2] McKinney, W. *Python for Data Analysis.* 3rd ed. O’Reilly, 2022. (Best practices on missing data and reproducible workflows.)

---

*This document can be exported to PDF (e.g. via your editor or a Markdown-to-PDF tool) for submission as **module_summary.pdf**.*
