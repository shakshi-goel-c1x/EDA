# EDA
EDA on the SOKA logs

The assignment is to perform Exploratory Data Analysis on the datasets where data is analyzed to summarize the main characteristics of the datasets. Steps involved in an EDA are as follows:
  1) Look at the structure of the data
  2) Pose an initial question that the data could answer 
  3) Access the fitness of the data and check if it needs any cleaning. Clean the data if required.
  4) Visualise the data into different types of graphs like Bar Chart, Box Plot, Line Graphs, Scatter Plots, etc
  5) Find out the patterns and trends from these visualisations
  6) Arrive at useful insights and conclusions


## Step 1 Importing the packages
Packages like pandas, numpy, matplotlib, seaborn, pandas_profiling are imported

## Step 2 Reading the datasets
Using the read_csv of the pandas library, the different datasets are read

## Step 3 Basic Look at the dataset
Different functions are used as follows:
  1) shape : Returns a tuple object with the number of rows and the number of columns
  2) list : Returns a list with the different column/variable names as strings
  3) head 
  4) tail
  
## Step 4 Summarization of the individual variables
1)MEASURES OF CENTRAL DEPENDENCY
  a) Mean
  b) Mode
  c) Median
2)MEASURES OF DISPERSION
  a) Standard Deviation
  b) Range
  c) Interquartile Range

Using the function describe, we can get all the above measure
