
#These are the functions used in DiabetesPlotting.py

# importing required libraries
import matplotlib.pyplot as plt # type: ignore
import pandas as pd


#loading CSV
# input: filepath as a string
# output: dataframe object
def load_csv(filepath):
    try:
        df = pd.read_csv(filepath)
        print("CSV file loaded successfully")
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

#cleaning data: removes whitespace in column names and removes rows with missing values
# input: dataframe object and required_columns as a list
# output: cleaned up dataframe object
def clean_data(df, required_columns):
    #stripping whitespace in column names
    df.columns=df.columns.str.strip()
    #dropping rows where required columns have missing data
    df_clean=df.dropna(subset=required_columns)
    #keep only those required_columns
    df_clean=df_clean[required_columns]
    print("Dataframe cleaned successfully")
    return df_clean

#plotting lines
# input:
    #df =dataframe object 
    # x_col = name of column for x-axis
    # y_col = name of column for y_axis
    # title = title of the plot as a string (optional)
    # xlabel = label on  x-axis (optional)
    # y_label= label on y-axis (optional)
    # filename = filename that graph will be saved as (optional)
#output:
    # shows line plot with x_col data on x-axis and y_col data on y_axis
    # saves line plot as filename if filename given
def plot_line(df,x_col,y_col,title="Plot",xlabel=None,ylabel=None,filename=None):
    if x_col not in df.columns or y_col not in df.columns:
        print("One or both columns '{x_col}','{y_col}' not found in dataframe.")
    plt.figure(figsize=(10,5))
    plt.plot(df[x_col],df[y_col],marker='o',linestyle='-')
    plt.title(title)
    plt.xlabel(xlabel if xlabel else x_col)
    plt.ylabel(ylabel if ylabel else y_col)
    plt.grid(True)
    plt.tight_layout()
    if filename:
        plt.savefig(filename) 
        print("Plot saved to {filename}")
    plt.show()

#plotting boxplot (for when data is binary)
# input:
    #df =dataframe object 
    # x_col = name of column for x-axis
    # y_col = name of column for y_axis
    # title = title of the plot as a string (optional)
    # xlabel = label on  x-axis (optional)
    # y_label= label on y-axis (optional)
    # filename = filename that graph will be saved as (optional)
#output:
    # shows boxplot with x_col data on x-axis and y_col data on y_axis
    # saves boxplot as filename if filename given
def plot_boxplot(df,x_col,y_col,title="Plot",xlabel=None,ylabel=None,filename=None):
    if x_col not in df.columns or y_col not in df.columns:
        print("One or both columns '{x_col}','{y_col}' not found in dataframe.")
    group_0=df[df[x_col]==0][y_col]
    group_1=df[df[x_col]==1][y_col]
    plt.figure(figsize=(10,5))
    plt.boxplot([group_0,group_1],labels=["No","Yes"])
    plt.title(title)
    plt.xlabel(xlabel if xlabel else x_col)
    plt.ylabel(ylabel if ylabel else y_col)
    plt.grid(True)
    plt.tight_layout()
    if filename:
        plt.savefig(filename) 
        print("Plot saved to {filename}")
    plt.show()

#plotting a scatter plot
# input:
    #df =dataframe object 
    # x_col = name of column for x-axis
    # y_col = name of column for y_axis
    # title = title of the plot as a string (optional)
    # xlabel = label on  x-axis (optional)
    # y_label= label on y-axis (optional)
    # filename = filename that graph will be saved as (optional)
#output:
    # shows scatter plot with x_col data on x-axis and y_col data on y_axis
    # saves scatter plot as filename if filename given
def plot_scatter(df,x_col,y_col,title="Plot",xlabel=None,ylabel=None,filename=None):
    if x_col not in df.columns or y_col not in df.columns:
        print("One or both columns '{x_col}','{y_col}' not found in dataframe.")
    plt.figure(figsize=(10,5))
    plt.scatter(df[x_col],df[y_col],color='blue',alpha=0.6,edgecolor='w',s=70)
    plt.title(title)
    plt.xlabel(xlabel if xlabel else x_col)
    plt.ylabel(ylabel if ylabel else y_col)
    plt.grid(True)
    plt.tight_layout()
    if filename:
        plt.savefig(filename) 
        print("Plot saved to {filename}")
    plt.show()