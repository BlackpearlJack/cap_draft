import pandas as pd
import scipy.stats as stats
import streamlit as st
import plotly.graph_objects as go

def perform_hypothesis_testing(df):
    st.write("## Hypothesis Testing")

    # Define hypotheses and results
    results = []

    # Hypothesis 1: Mean Purchase Amount by Region
    st.write("### 1. Mean Purchase Amount by Region")
    st.write("**Null Hypothesis (H0):** The mean purchase amount is the same across different regions.")
    st.write("**Alternative Hypothesis (H1):** The mean purchase amount is different across regions.")
    
    regions = df['region'].unique()
    region_data = [df[df['region'] == region]['purchase_amount'] for region in regions]
    f_stat, p_value = stats.f_oneway(*region_data)
    
    st.write(f"F-statistic: {f_stat:.2f}")
    st.write(f"P-value: {p_value:.2f}")
    
    results.append(["Mean Purchase Amount by Region", f_stat, p_value])
    
    if p_value < 0.05:
        st.write("**Conclusion:** Reject the null hypothesis. There is a significant difference in mean purchase amount between different regions.")
    else:
        st.write("**Conclusion:** Fail to reject the null hypothesis. There is no significant difference in mean purchase amount between different regions.")
    
    st.write("---")

    # Hypothesis 2: Purchase Frequency Across Age Groups
    st.write("### 2. Purchase Frequency Across Age Groups")
    st.write("**Null Hypothesis (H0):** There is no difference in purchase frequency across different age groups.")
    st.write("**Alternative Hypothesis (H1):** There is a significant difference in purchase frequency across age groups.")
    
    age_groups = df['age_group'].unique()
    age_group_data = [df[df['age_group'] == group]['purchase_frequency'] for group in age_groups]
    f_stat, p_value = stats.f_oneway(*age_group_data)
    
    st.write(f"F-statistic: {f_stat:.2f}")
    st.write(f"P-value: {p_value:.2f}")
    
    results.append(["Purchase Frequency Across Age Groups", f_stat, p_value])
    
    if p_value < 0.05:
        st.write("**Conclusion:** Reject the null hypothesis. There is a significant difference in purchase frequency across different age groups.")
    else:
        st.write("**Conclusion:** Fail to reject the null hypothesis. There is no significant difference in purchase frequency across age groups.")
    
    st.write("---")

    # Hypothesis 3: Purchase Frequency Across Income Brackets
    st.write("### 3. Purchase Frequency Across Income Brackets")
    st.write("**Null Hypothesis (H0):** There is no difference in purchase frequency across different income brackets.")
    st.write("**Alternative Hypothesis (H1):** There is a significant difference in purchase frequency across different income brackets.")
    
    income_brackets = df['income_bracket'].unique()
    income_bracket_data = [df[df['income_bracket'] == bracket]['purchase_frequency'] for bracket in income_brackets]
    f_stat, p_value = stats.f_oneway(*income_bracket_data)
    
    st.write(f"F-statistic: {f_stat:.2f}")
    st.write(f"P-value: {p_value:.2f}")
    
    results.append(["Purchase Frequency Across Income Brackets", f_stat, p_value])
    
    if p_value < 0.05:
        st.write("**Conclusion:** Reject the null hypothesis. There is a significant difference in purchase frequency across income brackets.")
    else:
        st.write("**Conclusion:** Fail to reject the null hypothesis. There is no significant difference in purchase frequency across income brackets.")
    
    st.write("---")

    # Hypothesis 4: Loyalty Score Across Regions
    st.write("### 4. Loyalty Score Across Regions")
    st.write("**Null Hypothesis (H0):** There is no difference in loyalty score across different regions.")
    st.write("**Alternative Hypothesis (H1):** There is a significant difference in loyalty score across regions.")
    
    region_data = [df[df['region'] == region]['loyalty_score'] for region in regions]
    f_stat, p_value = stats.f_oneway(*region_data)
    
    st.write(f"F-statistic: {f_stat:.2f}")
    st.write(f"P-value: {p_value:.2f}")
    
    results.append(["Loyalty Score Across Regions", f_stat, p_value])
    
    if p_value < 0.05:
        st.write("**Conclusion:** Reject the null hypothesis. There is a significant difference in loyalty score across regions.")
    else:
        st.write("**Conclusion:** Fail to reject the null hypothesis. There is no significant difference in loyalty score across regions.")
    
    st.write("---")

    # Hypothesis 5: Purchase Amount Across Age Groups
    st.write("### 5. Purchase Amount Across Age Groups")
    st.write("**Null Hypothesis (H0):** The mean purchase amount is the same across different age groups.")
    st.write("**Alternative Hypothesis (H1):** The mean purchase amount is different across age groups.")
    
    age_group_data = [df[df['age_group'] == group]['purchase_amount'] for group in age_groups]
    f_stat, p_value = stats.f_oneway(*age_group_data)
    
    st.write(f"F-statistic: {f_stat:.2f}")
    st.write(f"P-value: {p_value:.2f}")
    
    results.append(["Purchase Amount Across Age Groups", f_stat, p_value])
    
    if p_value < 0.05:
        st.write("**Conclusion:** Reject the null hypothesis. There is a significant difference in mean purchase amount across different age groups.")
    else:
        st.write("**Conclusion:** Fail to reject the null hypothesis. There is no significant difference in mean purchase amount across age groups.")
    
    st.write("---")

    # Hypothesis 6: Loyalty Score Across Income Brackets
    st.write("### 6. Loyalty Score Across Income Brackets")
    st.write("**Null Hypothesis (H0):** The loyalty score is the same across different income brackets.")
    st.write("**Alternative Hypothesis (H1):** The loyalty score is different across income brackets.")
    
    income_bracket_data = [df[df['income_bracket'] == bracket]['loyalty_score'] for bracket in income_brackets]
    f_stat, p_value = stats.f_oneway(*income_bracket_data)
    
    st.write(f"F-statistic: {f_stat:.2f}")
    st.write(f"P-value: {p_value:.2f}")
    
    results.append(["Loyalty Score Across Income Brackets", f_stat, p_value])
    
    if p_value < 0.05:
        st.write("**Conclusion:** Reject the null hypothesis. There is a significant difference in loyalty score across income brackets.")
    else:
        st.write("**Conclusion:** Fail to reject the null hypothesis. There is no significant difference in loyalty score across income brackets.")
    
    st.write("---")

    # Create a DataFrame for results
    results_df = pd.DataFrame(results, columns=["Test", "F-statistic", "P-value"])

    # Create table figure using Plotly
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(results_df.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[results_df[col] for col in results_df.columns],
                   fill_color='lavender',
                   align='left'))
    ])

    # Update layout to add title
    fig.update_layout(title="Hypothesis Testing Results")

    # Save the figure
    fig.write_image('figures/hypothesis_testing_results.png')
    st.image('figures/hypothesis_testing_results.png', caption='Hypothesis Testing Results')
