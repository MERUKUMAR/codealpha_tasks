# codealpha_tasks

# NOTE:
## Relevant Files For Particular Tasks
## TASK 1: WEB SCRAPER
i)web scraping.py
 ii)bbc_news_headlines.csv

## TASK 2: Exploratory Data Analysis (EDA)
i)EDA.ipynb
 ii)Superstore.csv
 iii)Superstore_EDA_Report.pdf

## TASK 3: DATA VISUALIZATION
i)Data Visualization.ipynb
 ii)data_visualization_portfolio(2).pdf
 iii)tudent_habits_performance.csv
 iv)dashboard.pbix

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

-------------------------------------------------------------------**TASK 2: Exploratory Data Analysis (EDA)**----------------------------------------------------


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

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--------------------------------------------**TASK 3: DATA VISUALIZATION**--------------------------------

#  Student Habits & Academic Performance – Data Visualization Project

This project explores how student lifestyle habits impact academic performance using data visualization techniques. It was developed as part of **Task 3** for a Data Analytics Internship.

---

##  Objective

Transform raw student data into compelling visuals and data stories that support decision-making and provide insights into effective academic behaviors.

---

##  Dataset Overview

- **Source**: Provided by internship program
- **Format**: CSV / Excel
- **Fields**:
  - `study_hours_per_day`
  - `sleep_hours`
  - `diet_quality`
  - `exercise_frequency`
  - `mental_health_rating`
  - `part_time_job`
  - `exam_score`
  - `gender`, etc.

---

##  Tools Used

- **Python**: Data cleaning and visualizations
  - Libraries: `Pandas`, `Matplotlib`, `Seaborn`
- **Tableau / Power BI**: Dashboard creation
- **PDF**: For portfolio 

---

##  Visualizations Created

- Histogram: Study hours and exam score distributions
- Correlation Heatmap
- Scatter Plot: Study Hours vs Exam Score
- Box Plot: Exam Score by Part-Time Job
- Bar Chart: Average Score by Diet Quality
- Pairplot: Multivariate relationships

---


##  Insights

- More study hours = higher exam scores
- No part-time job and healthy diet = better academic performance
- Balanced sleep, exercise, and study leads to optimal results

---

##  Next Steps
- Extend the project with predictive modeling (e.g., regression)
- Share insights on LinkedIn, GitHub, or a personal portfolio site
