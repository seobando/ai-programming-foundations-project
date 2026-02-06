# AI Programming Foundations — Data Workflow Project

## Project Description

This project implements a complete data workflow for exploring NYC Airbnb listing data. The notebook loads and cleans the data, runs exploratory analysis to find features that influence price, and produces visualizations to support insights. The goal is to identify which features are most relevant to listing price and to practice reproducible EDA suitable as a foundation for future modeling.

## What was Built

- **data_workflow.ipynb**: A Jupyter notebook that follows the project task structure (Tasks 1, 3–8). It includes:
  - Data ingestion (load CSV, display first rows)
  - Two cleaning functions with docstrings (`clean_price_outliers`, `drop_missing_in_key_columns`) applied to the dataset
  - One EDA function (`run_eda_summary`) for summary statistics and correlation with price
  - At least three visualizations (Matplotlib/Seaborn) with titles and labeled axes
  - A written summary and interpretation (insights, patterns, limitations, assumptions)
- **requirements.txt**: Python dependencies for reproducing the environment.

## Dataset

**NYC Airbnb Listings (pricing and listing characteristics)**  
- Link: [Kaggle — New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)  
- Place the dataset file (e.g. `airbnb_nyc.csv` or the repo’s CSV) in the project folder or adjust the path in the notebook’s load cell.

## How to Run the Project

### 1. Install dependencies

From the project root (`ai-programming-foundations-project`):

```bash
pip install -r requirements.txt
```

To regenerate `requirements.txt` from your environment:

```bash
pip freeze > requirements.txt
```

### 2. Open and run the notebook

- Open **data_workflow.ipynb** in Jupyter Notebook, JupyterLab, or VS Code.
- Ensure the kernel uses the same Python environment where you installed the requirements.
- Run all cells (e.g. “Run All”) from top to bottom. The notebook loads the CSV from the path set in the load cell (e.g. `data/airbnb_nyc.csv` or `airbnb_nyc.csv`); place your file accordingly or edit the path.

### 3. Optional: use a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

Then select the `.venv` kernel in Jupyter when opening `data_workflow.ipynb`.

---

## Bias Awareness (Data Cleaning)

Poor data cleaning can introduce bias in several ways:

- **Removing high-price outliers** (e.g. top 1% by price) can underrepresent luxury or unusual listings and make models less accurate for high-end segments. We justify this by focusing on “typical” listings for most use cases.
- **Dropping rows with missing values** in key columns (e.g. price, bedrooms, location) can bias results if missingness is not random (e.g. certain neighborhoods or property types report less often). We use complete-case analysis only for numeric correlation and plots; documenting this choice helps others assess bias.
- **Not documenting cleaning steps** would make it hard to reproduce or question decisions. All cleaning functions are documented with docstrings and applied in a clear order in the notebook.

Being explicit about what was removed and why (as in the notebook and in **module_summary.pdf**) is part of responsible practice.

---

## Future Integration Reflections

- **ML workflow changes**: This workflow is a suitable base for ML: the same cleaning and EDA steps would feed into feature engineering and train/test splits. We would add explicit train/validation/test splits, avoid using test data in cleaning/EDA, and consider encoding categoricals and scaling for models.
- **Neural network preparation**: For neural nets we would add or extend: normalization/standardization of numeric features, encoding of categorical variables (e.g. one-hot or embeddings), handling of sequences or text if used, and a clear separation of feature matrix and target (e.g. price) for supervised learning.
- **Agentic automation potential**: Parts of this workflow (loading, cleaning, running EDA, generating standard plots) could be automated by an agent that reads the dataset schema and project instructions, then produces or updates a notebook. Human review would still be needed for domain choices (e.g. which outliers to drop, which variables to focus on) and interpretation.
