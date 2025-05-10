# AquilX_DataVisualizationProject

This project is a personal data analysis and visualization tool built to explore and visualize patient health indicators from the [Kaggle Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset). It focuses on comparing biometric data (e.g., Age, BMI) with binary health outcomes like high glucose status.  
This was developed as a skills project to demonstrate Python programming, data cleaning, and data visualization techniques.

---

## 🚀 Features

- Load & clean CSV datasets using pandas
- Modular code with reusable functions (`utils.py`)
- Generate line plots, scatter plots, histograms, and boxplots with matplotlib
- Explore relationships between patient metrics (e.g., Age vs Glucose, BMI vs HighGlucose)
- Designed for easy re-use with any similar dataset

---

## 🛠️ Technologies Used

- Python 3.13
- pandas
- matplotlib


## 💻 Folder Structure
AquilX_CSVProject/
├── data/                    # 📂 Raw dataset files (CSV files go here)
│   └── diabetes_data.csv
│
├── output/                  # 📂 Saved plots and images
│   ├── example_boxplot.png
│   └── example_scatter.png
│
├── utils.py                 # 📝 Reusable functions for cleaning + plotting
├── DiabetesPlotting.py      # 📝 Main script (can also be called main.py)
├── requirements.txt         # 📝 Python package dependencies
├── README.md                # 📝 Project overview + instructions (this file)




