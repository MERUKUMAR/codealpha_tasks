# codealpha_tasks

---------------------------**TASK 1: WEB SCRAPER**----------------------------------------------
#  BBC News Web Scraper

This project is a simple web scraper built using **Python** and **BeautifulSoup** to extract the latest news headlines from the [BBC News](https://www.bbc.com/news) website. It collects the titles and links of top articles and saves them into a CSV file for further analysis or automation tasks.

---

##  Features

- Scrapes top news headlines from BBC News homepage
- Extracts both the **title** and **URL** of each article
- Cleans and removes duplicates
- Saves the output to a CSV file (`bbc_news_headlines.csv`)
- Fully customizable and beginner-friendly

---

##  Technologies Used

- Python 3.x
- BeautifulSoup4
- Requests
- Pandas

---

## 🛠️ Setup Instructions

### 1. Clone this repository or download the files
git clone https://github.com/MERUKUMAR/codealpha_tasks.git
cd codealpha_tasks

**Install Dependencies**:
pip install requests beautifulsoup4 pandas

**OUTPUT**
bbc_news_headlines.csv

**Use Cases**:
Create a custom news dashboard
Perform sentiment analysis on latest headlines
Track changes in media coverage over time
Learn and practice web scraping for real-world websites

 **Disclaimer**:
This scraper is built for educational purposes only. Please respect BBC's Terms of Service and avoid overloading their servers. Avoid frequent scraping or automation without permission.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------** TASK 2: Exploratory Data Analysis (EDA)**----------------------------------------------------


# Superstore EDA Project

This project showcases a comprehensive Exploratory Data Analysis (EDA) performed on the popular Superstore dataset using Python. The goal is to extract meaningful business insights through data visualization and statistical analysis.

## Tools & Libraries Used
**Python** (Jupyter Notebook)
**Pandas** – for data manipulation
**Matplotlib & Seaborn** – for data visualization

## Dataset
The dataset used is [Superstore.csv], which contains transactional records including:
Order details (Date, Category, Segment, etc.)
Sales performance (Sales, Profit, Discount)
Shipping information
Regional breakdown

# EDA Workflow
## 1. Data Loading & Cleaning
Loaded the CSV using Pandas
Checked for missing values and duplicates
Converted date columns to datetime format

## 2. Univariate Analysis
Countplot for Category
Histplot and Boxplot for Sales and Profit

## 3. Bivariate & Correlation Analysis
Scatter plot for Sales vs Profit
Heatmap of correlations between key numeric features
Boxplot of Segment vs Profit

## 4. Time Series Analysis
Created Month column
Plotted Monthly Sales Trend

## 5. Insights Extracted
🔸 Most sold category
🔸 Region with highest sales
🔸 Segment with highest profit
🔸 Sales-Profit correlation

## 🛠️ Setup Instructions

### 1. Clone this repository or download the files
git clone https://github.com/MERUKUMAR/codealpha_tasks.git
cd codealpha_tasks

**Install Dependencies**:
pip install pandas matplotlib.pyplot seaborn

# Report 

A detailed PDF report has been created containing:
Step-by-step explanation of each EDA stage
Cleanly formatted results and summaries
Key insights for business strategy

**Superstore_EDA_Report** will be visible in the repository check it out!

## Run
Open the Jupyter Notebook and run the EDA steps:
jupyter notebook Superstore_EDA.ipynb

**Use Cases**:
Business Performance Analysis
Customer & Segment Insights
Trend & Forecast Preparation
Inventory & Category Management
