
#Purpose:
# Analyze factors and determine whether there's a correlation present between factors and diabetes

#Importing important functions
from utils import load_csv

#Importing data 
Dia_df=load_csv("data/diabetes_data.csv")

#Creating a binary diabetes column 
# No diabetes= 0 and Prediabetic or Diabetes =1
Dia_df['Diabetes_binary']=Dia_df['Diabetes_012'].apply(lambda x: 0 if x==0 else 1)

#Group comparison for overview (can be expanded to include more factors):
# 1) takes average of BMI, Age, and number of days of 'not good' mental health and physical health 
# 2) Allows for comparison of averages between those with and without diabetes
# 3) Outputs a table to a .CSV file titled "group_comparison"
Dia_df.groupby('Diabetes_binary')[['Age','BMI','MentHlth','PhysHlth']].mean().to_csv("output/group_comparison.csv")

#T-test to check if BMI is statistically significant:
#Is the mean BMI of people with diabetes signficantly different from people without diabetes?

#importing ttest_ind function from scipy library
from scipy.stats import ttest_ind 
#create two groups
group_no_diabetes = Dia_df[Dia_df['Diabetes_binary']==0]['BMI']
group_diabetes = Dia_df[Dia_df['Diabetes_binary']==1]['BMI']
#run independent  t-test
# Welch's t-test because group sizes are unequal
t_stat,p_value = ttest_ind(group_no_diabetes,group_diabetes,equal_var=False)
#print results
print(f"T-statistic: {t_stat:.3e}")
print(f"P-value: {p_value:.3e}")
if p_value <0.05:
    print("The difference in BMI between groups is statistically significant.")
    print("Warning: The p-value may be very small, but it is not actually zero")
else:
    print("The difference in BMI between groups is NOT statistically significant.")
