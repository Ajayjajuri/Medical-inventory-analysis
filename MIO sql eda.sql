create database medical_project ;
create database medical_project ;
# medical inventory dastaet is imported using table data import wizard
###################### EDA using SQL ########################
use medical_project ;
################## undertanding the data #######################
desc mio_dataset;
SELECT Type_of_sales FROM mio_dataset;
select count(*) as countofvalues from mio_dataset;
#There are 14192 entries
select count(*) as countsalesvalues  from mio_dataset where Type_of_sales = "sale";
#Among  14192 entries 12516 are the sales value
select count(*) as countreturnvalues  from mio_dataset where Type_of_sales = "return";
##Among  14192 entries 1676 are the return values
select count(*) as countform1values  from mio_dataset where formulation = "form1";
#11601 are related to form1 type of formulation
select count(*) as countform2values  from mio_dataset where formulation = "form2";
#1323 are form2 kind of formulation
select max(final_sales) from mio_dataset;
# the maximun sale is 39490
select min(final_sales) from mio_dataset where final_sales >0;
# The minimum sale value is 40.192
select avg(final_sales) from mio_dataset;
#The avg sales 234

#----------------distinct counts----------------
select count(distinct(drugname)) as drug_names from mio_dataset;
#There are 752 distinct drugs
select count(distinct(subcat)) as drug_cat from mio_dataset;
#there are 18 types of  catogories 
select count(distinct(subcat1)) as drug_subcat from mio_dataset;
#There are 22 subcatogories of drugs based on condition of use
select count(distinct(patient_id)) as patients from mio_dataset;
#there are 4883 patients 
select count(distinct(specialisation))as count_specilaization,count(distinct(dept))as count_dept from mio_dataset;
## there are 58 specialisation and 3 departments
select count(distinct(patient_id)) as sales_patients from mio_dataset where type_of_sales = "sale"; 
#4632 involved in sales
select count(distinct(patient_id)) as return_patients from mio_dataset where type_of_sales = "return"; 
#1217 contributed for retur

#--------------------business insights------------------------
select sum(quantity) as totalqunatity from  mio_dataset;
#Total of 31703 drugs have been sold
select sum(returnquantity) as totalreturnquantity from mio_dataset;
#total of 4145 drugs have been returned
select sum(final_cost) as totalcost from mio_dataset; 
#1769235.26 is the total expenditure on production of drugs
select sum(final_sales) as totalsales from mio_dataset;
#3317189.916 is the total sales
select sum(rtnmrp) as totalrtnmrp from mio_dataset;
## 413847 worth of drugs have beeen returned
#-------income--------
select (sum(final_sales)-sum(final_cost))-sum(rtnmrp) as totalincome from mio_dataset;
## '1134107 'is the total income generated
#*************EDA before Data preprocessing**************

# first moment business decision / measures of central tendency
select * from mio_dataset;
#mean
SELECT AVG(quantity) AS mean_quantity
FROM mio_dataset;
#The avg qunatity of production is 2
SELECT AVG(final_cost) AS mean_f_cost
FROM mio_dataset;
# the average cost incurred in production is is 133 rupees
SELECT AVG(final_sales) AS mean_F_sales
FROM mio_dataset;
#the avg sales is 242 

# median
SELECT final_cost AS median_cost
FROM (
SELECT final_cost, ROW_NUMBER() OVER (ORDER BY final_cost) AS row_num,
COUNT(*) OVER () AS total_count
FROM mio_dataset
) AS subquery
WHERE row_num = (total_count + 1) / 2 OR row_num = (total_count + 2) / 2;
 
 # the middle most cost value is 54.29
 
# mode
SELECT SubCat AS mode_SubCat
FROM (
SELECT SubCat, COUNT(*) AS frequency
FROM mio_dataset
GROUP BY SubCat
ORDER BY frequency DESC
LIMIT 1
) AS subquery;
# Injetions are the most oftenly sold

SELECT SubCat1 AS mode_SubCat
FROM (
SELECT SubCat1, COUNT(*) AS frequency
FROM mio_dataset
GROUP BY SubCat1
ORDER BY frequency DESC
LIMIT 1
) AS subquery;
 # 'INTRAVENOUS & OTHER STERILE SOLUTIONS' are the most commonly used solutions

#Second Moment Business Decision / Measures of Dispersion
# Standard Deviation of Column4
SELECT STDDEV(final_cost) AS f_cost_stddev
FROM mio_dataset;
# cost of the products are widely dispersed as the stddev is 465

SELECT STDDEV(final_sales) AS f_sales_stddev
FROM mio_dataset;
# The sales of the products are more  widely dispersed as stddev is 671.3

desc mio_dataset;

# Third Moment Business Decision / Skewness

SELECT
(
SUM(POWER(final_cost- (SELECT AVG(final_cost) FROM mio_dataset), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(final_cost) FROM mio_dataset), 3))
) AS skewness
FROM mio_dataset;

# a skewness of 34.5 indicates the dataset has highly right skewed distribution for expenditure

SELECT
(
SUM(POWER(final_sales- (SELECT AVG(final_sales) FROM mio_dataset), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(final_sales) FROM mio_dataset), 3))
) AS skewness
FROM mio_dataset;

# a skewness of 21 indicates the dataset has highly right skewed distribution for sales

select max(final_cost) from mio_dataset;
select min(final_cost) from mio_dataset;

#Fourth Moment Business Decision / Kurtosis
SELECT
(
(SUM(POWER(final_cost- (SELECT AVG(final_cost) FROM mio_dataset), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(final_cost) FROM mio_dataset), 4))) - 3
) AS kurtosis
FROM mio_dataset;

# the kutosis value of 2025.7 for cost shows it has more extreme values than a normal distribution


SELECT
(
(SUM(POWER(final_sales- (SELECT AVG(final_sales) FROM mio_dataset), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(final_sales) FROM mio_dataset), 4))) - 3
) AS kurtosis
FROM mio_dataset;

# the kurtosis value of 950 for sales says there's a high difference in products prices


##################### Handling Duplicates:################

SELECT patient_id, COUNT(*) as duplicate_count
FROM mio_dataset
GROUP BY patient_id
HAVING COUNT(*) > 1;

CREATE TABLE temp_mio_dataset AS
SELECT DISTINCT *
FROM  mio_dataset;
select count(*) from  temp_mio_dataset;

desc temp_mio_dataset;

TRUNCATE TABLE mio_dataset;

INSERT INTO mio_dataset
SELECT * FROM temp_mio_dataset;

DROP TABLE temp_mio_dataset;


################## Missing Values #####################

SELECT count(*) FROM mio_dataset WHERE formulation= '' ;
#There are 650 missing values in formulation
SELECT count(*) FROM mio_dataset WHERE drugname= '' ;
#There are 1659 missing values in drugname
SELECT count(*) FROM mio_dataset WHERE subcat= '' ;
#There are 1659 missing values in subcat
SELECT count(*) FROM mio_dataset WHERE subcat1= '' ;
#There are 1682 missing values in subcat1

################## imputing missing values###############
SELECT count(distinct(Patient_id)) FROM mio_dataset WHERE formulation= '' ;
#There are 561 distinct patients, The unique values in formlation follow only 3, therefore imputing may be a good approach
 UPDATE mio_dataset
SET formulation = (SELECT formulation AS mode_formulation
FROM (
SELECT formulation, COUNT(*) AS frequency
FROM mio_dataset
GROUP BY formulation
ORDER BY frequency DESC
LIMIT 1
) as subquery)
WHERE formulation = '';

SELECT count(*) FROM mio_dataset WHERE formulation= '' ;
#after imputation there are 0 missing values in column 'Formulation'

#########################  Deleting rows with missing values ########################
SELECT count(distinct(Patient_id)) FROM mio_dataset WHERE drugname= '' ;
## There are 1220 distinct patient with drugname missing but the drugname consists of 752 different values therefore imputation is not good a approach thus deleting 
#the rows with missing values may be appropriate

DELETE  FROM mio_dataset
WHERE drugname = '';

 # same goes with subcat and subcat1
 DELETE  FROM mio_dataset
WHERE subcat = '';

 DELETE  FROM mio_dataset
WHERE subcat1 = '';

#####################Discretization/Binning/Grouping ###################
SELECT
  final_cost,
  CASE
    WHEN final_cost <53 THEN 'lower_cost'
    WHEN  final_cost >53 AND column_name < 20 THEN 'high cost'
    ELSE 'Other Bins'
  END AS discretized_column
FROM mio_dataset;
--------------------------------------------------------------
################### EDA after preprocessing ##################



select count(*) as countofvalues from mio_dataset;
#There are 12510 entries after preprocessing
select count(*) as countsalesvalues  from mio_dataset where Type_of_sales = "sale";
#Among  12510 entries 10997 are the sales value
select count(*) as countreturnvalues  from mio_dataset where Type_of_sales = "return";
##Among  12510 entries 1513 are the return values
select count(*) as countform1values  from mio_dataset where formulation = "form1";
# 10569 are related to form1 type of formulation
select count(*) as countform2values  from mio_dataset where formulation = "form2";
#1323 are form2 kind of formulation
select max(final_sales) from mio_dataset;
# the maximun sale is 39490 remains the same
select min(final_sales) from mio_dataset where final_sales >0;
# The minimum sale value is 40.192 
select avg(final_sales) from mio_dataset;
#The avg sales changes to 230

#----------------distinct counts----------------
select count(distinct(drugname)) as drug_names from mio_dataset;
#There are 747 distinct drugs after preprocessing
select count(distinct(subcat)) as drug_cat from mio_dataset;
#there are 17 types of  catogories 
select count(distinct(subcat1)) as drug_subcat from mio_dataset;
#There are 21 subcatogories of drugs based on condition of use
select count(distinct(patient_id)) as patients from mio_dataset;
#there are 4582 patients 
select count(distinct(specialisation))as count_specilaization,count(distinct(dept))as count_dept from mio_dataset;
## there are 56 specialisation and 3 departments
select count(distinct(patient_id)) as sales_patients from mio_dataset where type_of_sales = "sale"; 
#4330 involved in sales
select count(distinct(patient_id)) as return_patients from mio_dataset where type_of_sales = "return"; 
#1142 contributed for returns

#--------------------business insights------------------------
select sum(quantity) as totalqunatity from  mio_dataset;
#Total of 23416 drugs have been sold after preprocesssig
select sum(returnquantity) as totalreturnquantity from mio_dataset;
#total of 2987 drugs have been returned
select sum(final_cost) as totalcost from mio_dataset; 
#'1661399.99' is the total expenditure on production of drugs
select sum(final_sales) as totalsales from mio_dataset;
#'2876071.6' is the total sales
select sum(rtnmrp) as totalrtnmrp from mio_dataset;
## '356907' worth of drugs have beeen returned
#-------income--------
select (sum(final_sales)-sum(final_cost))-sum(rtnmrp) as totalincome from mio_dataset;
## '857764.65' is the total income generated
#*************EDA **************

# first moment business decision / measures of central tendency
select * from mio_dataset;
#mean
SELECT AVG(quantity) AS mean_quantity
FROM mio_dataset;
#The avg qunatity of production is 2
SELECT AVG(final_cost) AS mean_f_cost
FROM mio_dataset;
# the average cost incurred in production is is 132.8 rupees
SELECT AVG(final_sales) AS mean_F_sales
FROM mio_dataset;
#the avg sales is 229.9 

# median
SELECT final_cost AS median_cost
FROM (
SELECT final_cost, ROW_NUMBER() OVER (ORDER BY final_cost) AS row_num,
COUNT(*) OVER () AS total_count
FROM mio_dataset
) AS subquery
WHERE row_num = (total_count + 1) / 2 OR row_num = (total_count + 2) / 2;
 
 # the middle most cost value is 54.29 remains the same
 
# mode
SELECT SubCat AS mode_SubCat
FROM (
SELECT SubCat, COUNT(*) AS frequency
FROM mio_dataset
GROUP BY SubCat
ORDER BY frequency DESC
LIMIT 1
) AS subquery;
# Injetions are the most oftenly sold

SELECT SubCat1 AS mode_SubCat
FROM (
SELECT SubCat1, COUNT(*) AS frequency
FROM mio_dataset
GROUP BY SubCat1
ORDER BY frequency DESC
LIMIT 1
) AS subquery;
 # 'INTRAVENOUS & OTHER STERILE SOLUTIONS' are the most commonly used solutions

#Second Moment Business Decision / Measures of Dispersion
# Standard Deviation of Column4
SELECT STDDEV(final_cost) AS f_cost_stddev
FROM mio_dataset;
# cost of the products are widely dispersed as the stddev is incresed to  493.38

SELECT STDDEV(final_sales) AS f_sales_stddev
FROM mio_dataset;
# The sales of the products are more  widely dispersed as stddev is 689.83

desc mio_dataset;

# Third Moment Business Decision / Skewness

SELECT
(
SUM(POWER(final_cost- (SELECT AVG(final_cost) FROM mio_dataset), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(final_cost) FROM mio_dataset), 3))
) AS skewness
FROM mio_dataset;

# a skewness of 32.69 indicates the dataset has highly right skewed distribution for expenditure

SELECT
(
SUM(POWER(final_sales- (SELECT AVG(final_sales) FROM mio_dataset), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(final_sales) FROM mio_dataset), 3))
) AS skewness
FROM mio_dataset;

# a skewness of 21.75 indicates the dataset has highly right skewed distribution for sales

select max(final_cost) from mio_dataset;
select min(final_cost) from mio_dataset;

#Fourth Moment Business Decision / Kurtosis
SELECT
(
(SUM(POWER(final_cost- (SELECT AVG(final_cost) FROM mio_dataset), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(final_cost) FROM mio_dataset), 4))) - 3
) AS kurtosis
FROM mio_dataset;

# the kutosis value reuced after preprocessing to 1809.70 for cost and shows it has more extreme values than a normal distribution


SELECT
(
(SUM(POWER(final_sales- (SELECT AVG(final_sales) FROM mio_dataset), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(final_sales) FROM mio_dataset), 4))) - 3
) AS kurtosis
FROM mio_dataset;

# the kurtosis value of 965.45 for sales says there's a high difference in products prices

