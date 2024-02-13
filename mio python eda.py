#####----------MIO python EDA----------#####
#EDA using python

import pandas as pd
data = pd.read_excel(r"C:\Users\ajay a j\Desktop\projects questions\Medical Inventory Optimaization Dataset.xlsx")
data.head()
############### Basic  #############
data.info()
datadesc= data.describe()



data['Patient_ID'].value_counts()
# there are 4883 distinct patients
data['DrugName'].value_counts()
#751 unique drug names
data['Typeofsales'].value_counts()
# There are 12537 sales and 1681 returns
data['Formulation'].value_counts()
#Form1     11622
#Form2      1325
#patent      539
#Form3        79

data['Quantity'].sum()
#31731
data['Final_Sales'].sum()
# 3327556.556
data['Final_Cost'].sum()
#1774747.02
data['RtnMRP'].sum()
# 414124.202
data['ReturnQuantity'].sum()
#4151
##First Moment Business Decision / Measures of Central Tendency##########
########### Mean 
meanquantity = data['Quantity'].mean()
print(meanquantity)

# THE mean of quantity is 2.23
mean_Final_Cost = data['Final_Cost'].mean()
print(mean_Final_Cost) #=124.824
mean_Final_Sales = data['Final_Sales'].mean()
print(mean_Final_Sales) #=234.03

############## Median
median_qunatity = data['Quantity'].median()
print(median_qunatity) # 1
median_Final_Cost = data['Final_Cost'].median()
print(median_Final_Cost) # 53.65
median_Final_Sales = data['Final_Sales'].median()
print(median_Final_Sales) #86.424
 
# mode
mode_SubCat = data['SubCat'].mode()
print(mode_SubCat) 
# Injections are the most commonly sold type of drug

mode_DrugName = data['DrugName'].mode()
print(mode_DrugName) 
# SODIUM CHLORIDE IVF 100ML is higly sold drug
mode_SubCat1 = data['SubCat1'].mode()
print(mode_SubCat1)
# INTRAVENOUS & OTHER STERILE SOLUTIONS are the medical conditional drug sold more oftenly

###Second Moment Business Decision / Measures of Dispersion

#standard deviation
std_quantity = data['Quantity'].std()
print(std_quantity) #5.13
# quantity folllows regular pattern and smaller variabiltity
std_ReturnQuantity = data['ReturnQuantity'].std()
print(std_ReturnQuantity)
# 1.64
std_Final_Cost = data['Final_Cost'].std()
print(std_Final_Cost) 

#464.787 inidcates larger variaility
std_Final_Sales = data['Final_Sales'].std()
print(std_Final_Sales)
#671.26 shows larger variability
std_RtnMRP = data['RtnMRP'].std()
print(std_RtnMRP) 
#182.26inidcates larger variaility

 #variance 
 
var_RtnMRP = data['RtnMRP'].var()
print(var_RtnMRP)
#33219.55
var_ReturnQuantity = data['ReturnQuantity'].var()
print(var_ReturnQuantity)
#2.7 
var_quantity = data['Quantity'].var()
print(var_quantity)
# 26.34 
var_Final_Cost = data['Final_Cost'].var()
print(var_Final_Cost) 
# 216023.04
var_Final_Sales = data['Final_Sales'].var()
print(var_Final_Sales)
# 450592.09


##Third Moment Business Decision / Skewness
skewness_Quantity = data['Quantity'].skew()
print(skewness_Quantity)
# It is a positive skewness as the value is 11.34
skewness_rQuantity = data['ReturnQuantity'].skew()
print(skewness_rQuantity)
#It is a positive skewness as the value is 17.17
skew_Final_Cost = data['Final_Cost'].skew()
print(skew_Final_Cost) 
# It is a positive skewness as the value is 34.50
skew_Final_Sales = data['Final_Sales'].skew()
print(skew_Final_Sales)
# It is a positive skewness as the value is 21
skew_RtnMRP = data['RtnMRP'].skew()
print(skew_RtnMRP)
# It is a positive skewness as the value is 15.79

#Fourth Moment Business Decision / Kurtosis
kurtosis_Quantity = data['Quantity'].kurtosis()
print(kurtosis_Quantity)
# heavy tails with some outliers (180.15)
kurtosis_rQuantity = data['ReturnQuantity'].kurtosis()
print(kurtosis_rQuantity)
# heavy tails with some outliers (409.41)
kurtosis_Final_Cost = data['Final_Cost'].kurtosis()
print(kurtosis_Final_Cost) 
## heavy tails with extreme outliers (2025.86)
kurtosis_Final_Sales = data['Final_Sales'].kurtosis()
print(kurtosis_Final_Sales)
# heavy tails with extreme outliers (948.52)
kurtosis_RtnMRP = data['RtnMRP'].kurtosis()
print(kurtosis_RtnMRP)
# heavy tails with some outliers (403.52)


###  Graphical Representation
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

#histogram

plt.hist(data['Quantity'], bins=5,edgecolor='black')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.title('Histogram of quantity')
plt.show()

# the plot shows most of the data is between 0 to 5
data['Final_Cost'].max()
plt.hist(data['Final_Cost'], bins=100,edgecolor='black')
plt.xlabel('Final_Cost')
plt.ylabel('Frequency')
plt.title('Histogram of Final_Cost')
plt.show()

data['Final_Cost'].max()
plt.hist(data['Final_Sales'], bins=100,edgecolor='black')
plt.xlabel('Final_Sales')
plt.ylabel('Frequency')
plt.title('Histogram of Final_Sales')
plt.show()

#Scatter plot
plt.scatter(data['Final_Cost'], data['Final_Sales'])
plt.xlabel('Final_Cost')
plt.ylabel('Final_Sales')
plt.title('cost vs sales')
plt.show()

plt.scatter(data['Quantity'], data['Final_Sales'])
plt.xlabel('Quantity')
plt.ylabel('Final_Sales')
plt.title('Quantity vs sales')
plt.show()

plt.scatter(data['Quantity'], data['Final_Cost'])
plt.xlabel('Quantity')
plt.ylabel('Final_Cost')
plt.title('Quantity vs  Final_Cost')
plt.show()

#box plot
plt.boxplot(data['Quantity'])
plt.title ('boxplot on quantity')
#box plot on quantity purely shows the presence of outliers
plt.boxplot(data['Final_Sales'])
plt.title('boxplot on Final_Sales')

plt.boxplot(data['Final_Cost'])
plt.title('boxplot on Final_Cost')

######### Typecasting
data.info()
data.describe
data['Patient_ID'] = data['Patient_ID'].astype(object)
print(data['Patient_ID'].dtypes)

#changed the patient_id from int to object

##----------->Handling Duplicates
dupli=data.duplicated()

data.drop_duplicates(inplace = True)

##------------>Outlier Treatment

Q1 = data['Quantity'].quantile(0.25)
Q3 = data['Quantity'].quantile(0.75)
IQR = Q3 - Q1
data = data[(data['Quantity'] >= Q1 - 1.5*IQR) & (data['Quantity'] <= Q3 + 1.5*IQR)]
print(data)

plt.boxplot(data['Final_Sales'])

Q1 = data['Final_Cost'].quantile(0.25)
Q3 = data['Final_Cost'].quantile(0.75)
IQR = Q3 - Q1
data = data[(data['Final_Cost'] >= Q1 - 1.5*IQR) & (data['Final_Cost'] <= Q3 + 1.5*IQR)]
print(data)

Q1 = data['Final_Sales'].quantile(0.25)
Q3 = data['Final_Sales'].quantile(0.75)
IQR = Q3 - Q1
data = data[(data['Final_Sales'] >= Q1 - 1.5*IQR) & (data['Final_Sales'] <= Q3 + 1.5*IQR)]



#----------->Zero & near Zero Variance features

variance = data.var()
near_zero_var_features = variance[variance < 0.01]
print(near_zero_var_features)

#----------->Missing Values

missing_form =data['Formulation'].isnull().sum()
missing_form
#there are 588 missing values in the formulation 
# Impute missing values in formulation column with the mode
# Impute missing values in a specific column with the mean
# Fill missing values with the mode
data['Formulation'].fillna(data['Formulation'].mode()[0], inplace=True)

missing_Drugname =data['DrugName'].isnull().sum()
#there are 1239 missing drug names
# it must be imputed
data['DrugName'].fillna(data['DrugName'].mode()[0], inplace=True)

missing_subcat =data['SubCat'].isnull().sum()
#there are 1239 missing values in subcat and it must be imputed with mode
data['SubCat'].fillna(data['SubCat'].mode()[0], inplace=True)

missing_subcat =data['SubCat1'].isnull().sum()
#there are 1248 missing values
data['SubCat1'].fillna(data['SubCat1'].mode()[0], inplace=True)

#--------->Normalization
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
data['Quantity'] = scaler.fit_transform(data[['Quantity']])
print(data)

data['Final_Cost'] = scaler.fit_transform(data[['Final_Cost']])


data['Final_Sales'] = scaler.fit_transform(data[['Final_Sales']])



#---------->Dummy Variable Creation
dummy_vars = pd.get_dummies(data['Formulation'])
data = pd.concat([data, dummy_vars], axis=1)
print(data)
dummy_subcat = pd.get_dummies(data['SubCat'])
data = pd.concat([data, dummy_vars], axis=1)

dummy_subcat1 = pd.get_dummies(data['SubCat1'])
data = pd.concat([data, dummy_vars], axis=1)

#------> AUTO EDA <---------#

# Sweetviz
###########

import sweetviz as sv
df= pd.read_csv(r"C:\Users\ajay a j\Desktop\projects questions\MIO_dataset.csv")
s = sv.analyze(data)
s.show_html()


# Autoviz
###########
# pip install autoviz
from autoviz.AutoViz_Class import AutoViz_Class

av = AutoViz_Class()
a = av.AutoViz(r"C:\Users\ajay a j\Desktop\projects questions\MIO_dataset.csv", chart_format = 'html')


# If the dependent variable is known:
a = av.AutoViz(r"C:\Users\ajay a j\Desktop\projects questions\MIO_dataset.csv", depVar = 'gmat') # depVar - target variable in your dataset



# D-Tale
########

# pip install dtale   # In case of any error then please install werkzeug appropriate version (pip install werkzeug==2.0.3)
import dtale
import pandas as pd

datatale = pd.read_csv(r"C:\Users\ajay a j\Desktop\projects questions\MIO_dataset.csv")

d = dtale.show(datatale)
d.open_browser()


# Pandas Profiling
###################

# pip install pandas_profiling
from pandas_profiling import ProfileReport 

p = ProfileReport(data)
p
p.to_file("output.html")







#####------> EDA after Data preprocessing <--------###
###### basic EDA #############

data.info()
data['Patient_ID'].value_counts()
# there are 4421 distinct patients
data['DrugName'].value_counts()
#610 unique drug names
data['Typeofsales'].value_counts()
# There are 8846 sales and 1452 returns

data['Formulation'].value_counts()
#Form1     9190
#Form2     1044
#Patent      40
#Form3       24
data['Quantity'].sum()
#4093.66
data['Final_Sales'].sum()
#3597.559
data['Final_Cost'].sum()
#1946.968
data['RtnMRP'].sum()
# 209245.206
data['ReturnQuantity'].sum()
#3646

##First Moment Business Decision / Measures of Central Tendency##########
########### Mean 
meanquantity = data['Quantity'].mean()
print(meanquantity)
# THE mean of quantity is 0
mean_Final_Cost = data['Final_Cost'].mean()
print(mean_Final_Cost) #0.21
mean_Final_Sales = data['Final_Sales'].mean()
print(mean_Final_Sales) #0

############## Median
median_qunatity = data['Quantity'].median()
print(median_qunatity) # 0
median_Final_Cost = data['Final_Cost'].median()
print(median_Final_Cost) # 0.14
median_Final_Sales = data['Final_Sales'].median()
print(median_Final_Sales) #0
 
# mode
mode_SubCat = data['SubCat'].mode()
print(mode_SubCat) 
# Injections still are the most commonly sold type of drug

mode_DrugName = data['DrugName'].mode()
print(mode_DrugName) 
# SODIUM CHLORIDE IVF 100ML is higly sold drug
mode_SubCat1 = data['SubCat1'].mode()
print(mode_SubCat1)
# INTRAVENOUS & OTHER STERILE SOLUTIONS are the medical conditional drug sold more oftenly

###Second Moment Business Decision / Measures of Dispersion

#standard deviation
std_quantity = data['Quantity'].std()
print(std_quantity)
# 0 qunatity folllows regular pattern and smaller variabiltity 
std_ReturnQuantity = data['ReturnQuantity'].std()
print(std_ReturnQuantity)
# 0

std_Final_Cost = data['Final_Cost'].std()
print(std_Final_Cost) 

#0.2 inidcates smaller variaility
std_Final_Sales = data['Final_Sales'].std()
print(std_Final_Sales)
# 0  indicates regular pattern and smaller variabiltity 
std_RtnMRP = data['RtnMRP'].std()
print(std_RtnMRP) 
## 0 indicates regular pattern and smaller variabiltity 


#variance

var_quantity = data['Quantity'].var()
print(var_quantity)
# 0.06
var_Final_Cost = data['Final_Cost'].var()
print(var_Final_Cost) 
# 0.04
var_Final_Sales = data['Final_Sales'].var()
print(var_Final_Sales)
# 0.05
var_RtnMRP = data['RtnMRP'].var()
print(var_RtnMRP)
#0.00
var_ReturnQuantity = data['ReturnQuantity'].var()
print(var_ReturnQuantity)
#0.00

##Third Moment Business Decision / Skewness
skewness_Quantity = data['Quantity'].skew()
print(skewness_Quantity)
#value of 0.6 indicates a perfectly symmetrical distribution
skewness_rQuantity = data['ReturnQuantity'].skew()
print(skewness_rQuantity)
#6.99
skew_Final_Cost = data['Final_Cost'].skew()
print(skew_Final_Cost) 
# #value of 1.58 indicates a perfectly symmetrical positive skew distribution

skew_Final_Sales = data['Final_Sales'].skew()
print(skew_Final_Sales)
# #value of 0 indicates a perfect distribution
skew_RtnMRP = data['RtnMRP'].skew()
print(skew_RtnMRP)
# It is a positive skewness as the value is 6.40


#Fourth Moment Business Decision / Kurtosis
kurtosis_Quantity = data['Quantity'].kurtosis()
print(kurtosis_Quantity)
##value of 0 indicates a normal distribution
kurtosis_rQuantity = data['ReturnQuantity'].kurtosis()
print(kurtosis_rQuantity)
# heavy tails with some outliers (60.3)

kurtosis_Final_Cost = data['Final_Cost'].kurtosis()
print(kurtosis_Final_Cost) 
## heavy tails with less outliers as the value is 2.14
kurtosis_Final_Sales = data['Final_Sales'].kurtosis()
print(kurtosis_Final_Sales)
# normalized data as the value is 0
kurtosis_RtnMRP = data['RtnMRP'].kurtosis()
print(kurtosis_RtnMRP)
# heavy tails with some outliers (54.38)



######## Graphical Representation  after EDA




#histogram

plt.hist(data['Quantity'], bins=10,edgecolor='black')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.title('Histogram of quantity')
plt.show()

# the plot shows most of the data is between 0 to 5
data['Final_Cost'].max()
plt.hist(data['Final_Cost'], bins=100,edgecolor='black')
plt.xlabel('Final_Cost')
plt.ylabel('Frequency')
plt.title('Histogram of Final_Cost')
plt.show()

data['Final_Cost'].max()
plt.hist(data['Final_Sales'], bins=100,edgecolor='black')
plt.xlabel('Final_Sales')
plt.ylabel('Frequency')
plt.title('Histogram of Final_Sales')
plt.show()

#Scatter plot
plt.scatter(data['Final_Cost'], data['Final_Sales'])
plt.xlabel('Final_Cost')
plt.ylabel('Final_Sales')
plt.title('cost vs sales')
plt.show()

plt.scatter(data['Quantity'], data['Final_Sales'])
plt.xlabel('Quantity')
plt.ylabel('Final_Sales')
plt.title('Quantity vs sales')
plt.show()

plt.scatter(data['Quantity'], data['Final_Cost'])
plt.xlabel('Quantity')
plt.ylabel('Final_Cost')
plt.title('Quantity vs  Final_Cost')
plt.show()

#box plot
plt.boxplot(data['Quantity'])
plt.title ('boxplot on quantity')
#box plot on quantity purely shows the presence of outliers
plt.boxplot(data['Final_Sales'])
plt.title('boxplot on Final_Sales')

plt.boxplot(data['Final_Cost'])
plt.title('boxplot on Final_Cost')