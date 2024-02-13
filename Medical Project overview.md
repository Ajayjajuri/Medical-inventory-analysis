# overview of steel project

This data analysis project aims to provide insights in to the sales of the pharmaceutical products of an pharmaceutical company of a leading hospital in india company over the past year. By analyzing various aspects of the sales data , we seek to indentify trends, make data-drien recommendations, and gain a deeper understanding of the client performance

## Table of contents
- [Data sources](#data-sources)
- [Tools](#tools)
- [Data Cleaning/ Preparation](#data-cleaning-preparation)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Results/ Findings](#results-findings)
- [Recommendations](#recommendations)


_
## Data sources
Medical_set : The primary dataset used for this analysis is the "MIO_data.csv" file containing detailed information about each sale made by production company

## Tools
- Excel - Data store , Data Cleaning
- Python -Exploratory Data Analysis, Data preprocessing
- MySql - Data Analysis
- PowerBI - creating reports and Dashboards
- (Tableau - when there is need of map visualization)
- Google Data studio/Looker studio - creating Dashboards


## Data Cleaning/ Preparation
In the data preparation phase, We performed these task
1. Data loading and inspection
2. Handling missing values
3. Data cleaning and formatting

## Exploratory Data Anlaysis 
- In the initial EDA phase, We performed four business moments
1. First business moment ( Measures of central tendency)
2. Second business moment ( Measures of dispersion)
3. Third business moment ( Skewness)
4. Fourth business moment ( Kurtosis)

## Data Analysis
```sql
 SELECT Quantity AS mode_Quantity
FROM (
SELECT Quantity, COUNT(*) AS frequency
FROM steelset
GROUP BY Quantity
ORDER BY frequency DESC
LIMIT 1
) AS subquery;
```

## Results/ Findings
1.The companys sales have been steadily reducing over past year, due to bounce rate
2.31703 no of drugs have been sold and 4145 have been returned
3.1769235.26 is the total expenditure on production of drugs
4.3317189.916 worth of drugs have been sold
5.413847 worth of drugs have been returned
6.1134107 of income have been generated

## Recommendations
Based on the anlaysis , we recommend the following actions:
• Demand Forecasting
•	Optimal Inventory Levels
•	Real-time Monitoring
•	Enhanced Communication
•	Data-Driven Decision-Making
•	Technology Integration	


## Limitations
 I had to remove all zero values from rtnmrp and rtnquantity because they would affected the accuracy of my conclusions for the analysis . There are still few outliers even after the ommision 
