import pandas as pd

def load_data():
    # Load the dataset
    df = pd.read_csv('data/Customer Purchasing Behaviors.csv')
    
    # Create age groups with specified labels, excluding 'senior'
    df['age_group'] = pd.cut(df['age'], bins=[18, 25, 44, 59], labels=['young adult', 'adult', 'middle age'])
    
    # Create income brackets using quantiles
    df['income_bracket'] = pd.qcut(df['annual_income'], q=3, labels=['low', 'medium', 'high'])
    
    return df
