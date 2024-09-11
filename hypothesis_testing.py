import streamlit as st
import pandas as pd
import scipy.stats as stats

def load_css(file_name):
    with open(file_name) as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def perform_two_way_anova(df):
    st.header("Hypothesis Testing Results")

    # Load custom CSS
    load_css('styles.css')

    # Styled About Section
    st.markdown("""
    <div class="about-section">
        <h2>About the Hypothesis Tests</h2>
        <p>This section presents the results of hypothesis testing conducted to analyze various metrics of customer behavior. 
        The tests include comparisons of means across different groups to understand how variables such as purchase amount, 
        purchase frequency, and loyalty score vary by age group, income bracket, and region. The specific hypotheses tested are:</p>
        <ul>
            <li><strong>Mean Purchase Amount Across Age Groups</strong>: Determines if the mean purchase amount differs between different age groups.</li>
            <li><strong>Mean Purchase Amount Across Income Brackets</strong>: Assesses if the mean purchase amount varies across income brackets.</li>
            <li><strong>Mean Purchase Frequency Across Regions</strong>: Examines if the mean purchase frequency is different among various regions.</li>
            <li><strong>Mean Loyalty Score Across Age Groups</strong>: Tests whether the mean loyalty score is consistent across different age groups.</li>
            <li><strong>Mean Loyalty Score Across Regions</strong>: Evaluates if the mean loyalty score varies between regions.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Helper function to create styled HTML table
    def create_html_table(data):
        html = "<table>"
        html += "<tr><th>Test</th><th>F-value</th><th>P-value</th><th>Result</th></tr>"
        for index, row in data.iterrows():
            result = "Significant" if row['P-value'] < 0.05 else "Not Significant"
            html += f"<tr><td>{row['Test']}</td><td>{row['F-value']:.2f}</td><td>{row['P-value']:.4f}</td><td>{result}</td></tr>"
        html += "</table>"
        return html

    # Create an empty DataFrame to store results
    results_df = pd.DataFrame(columns=["Test", "F-value", "P-value"])

    # Test 1: Mean Purchase Amount Across Age Groups
    age_groups = df['age_group'].unique()
    purchase_amount_by_age = [df[df['age_group'] == age]['purchase_amount'] for age in age_groups]
    f_val, p_val = stats.f_oneway(*purchase_amount_by_age)
    results_df = pd.concat([results_df, pd.DataFrame([{
        "Test": "Mean Purchase Amount by Age Group",
        "F-value": f_val,
        "P-value": p_val
    }])], ignore_index=True)

    # Test 2: Mean Purchase Amount Across Income Brackets
    income_brackets = df['income_bracket'].unique()
    purchase_amount_by_income = [df[df['income_bracket'] == income]['purchase_amount'] for income in income_brackets]
    f_val, p_val = stats.f_oneway(*purchase_amount_by_income)
    results_df = pd.concat([results_df, pd.DataFrame([{
        "Test": "Mean Purchase Amount by Income Bracket",
        "F-value": f_val,
        "P-value": p_val
    }])], ignore_index=True)

    # Test 3: Mean Purchase Frequency Across Regions
    regions = df['region'].unique()
    purchase_frequency_by_region = [df[df['region'] == region]['purchase_frequency'] for region in regions]
    f_val, p_val = stats.f_oneway(*purchase_frequency_by_region)
    results_df = pd.concat([results_df, pd.DataFrame([{
        "Test": "Mean Purchase Frequency by Region",
        "F-value": f_val,
        "P-value": p_val
    }])], ignore_index=True)

    # Test 4: Mean Loyalty Score Across Age Groups
    loyalty_scores_by_age = [df[df['age_group'] == age]['loyalty_score'] for age in age_groups]
    f_val, p_val = stats.f_oneway(*loyalty_scores_by_age)
    results_df = pd.concat([results_df, pd.DataFrame([{
        "Test": "Mean Loyalty Score by Age Group",
        "F-value": f_val,
        "P-value": p_val
    }])], ignore_index=True)

    # Test 5: Mean Loyalty Score Across Regions
    loyalty_scores_by_region = [df[df['region'] == region]['loyalty_score'] for region in regions]
    f_val, p_val = stats.f_oneway(*loyalty_scores_by_region)
    results_df = pd.concat([results_df, pd.DataFrame([{
        "Test": "Mean Loyalty Score by Region",
        "F-value": f_val,
        "P-value": p_val
    }])], ignore_index=True)

    # Display results as a styled HTML table
    html_table = create_html_table(results_df)
    st.markdown(html_table, unsafe_allow_html=True)
    
     # Report Section
    st.markdown("""
    <div class="report-section">
        <h2>Report</h2>
        <p>The results of the ANOVA tests are summarized in the table below. The F-value indicates the ratio of variance between groups to the variance within groups, while the P-value assesses the probability that the observed differences are due to chance.</p>      
        <h3>Summary of Results:</h3>
        <ul>
            <li><strong>Mean Purchase Amount by Age Group:</strong> The F-value of 308.02 and P-value of 0.0000 indicate a highly significant difference in purchase amounts between different age groups.</li>
            <li><strong>Mean Purchase Amount by Income Bracket:</strong> An F-value of 602.66 and P-value of 0.0000 show a very significant difference in purchase amounts across different income brackets.</li>
            <li><strong>Mean Purchase Frequency by Region:</strong> The F-value of 20.00 and P-value of 0.0000 suggest a significant difference in purchase frequency across regions.</li>
            <li><strong>Mean Loyalty Score by Age Group:</strong> With an F-value of 257.80 and P-value of 0.0000, there is a significant variation in loyalty scores between age groups.</li>
            <li><strong>Mean Loyalty Score by Region:</strong> The F-value of 20.15 and P-value of 0.0000 indicate a significant difference in loyalty scores between regions.</li>
        </ul>
        <p>All tests show statistically significant differences, suggesting that customer behavior metrics such as purchase amount, frequency, and loyalty score vary significantly by age group, income bracket, and region. These insights can help in tailoring marketing strategies and improving customer targeting.</p>
    </div>
    """, unsafe_allow_html=True)
