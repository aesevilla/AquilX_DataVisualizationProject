#sources of data:
# https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset

from utils import load_csv, clean_data, plot_line, plot_boxplot, plot_scatter

Dia_df=load_csv("data/diabetes_data.csv")
columns=["HighChol","Age","BMI"]
Dia_df_clean=clean_data(Dia_df,columns)
x_col=columns[0]
y_col=columns[1]
title1="High Cholesterol Status Among Adolescents"
plot_boxplot(Dia_df_clean,x_col,y_col,title1,filename="Boxplot_HighCholStatus_Age")
x_col1=columns[1]
y_col1=columns[2]
title2="Scatter Plot of BMI vs. Age"
plot_scatter(Dia_df_clean,x_col1,y_col1,title2,filename="Scatter_BMI_Age")