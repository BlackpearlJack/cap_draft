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
    
    # Report Section with Modelling and Accuracy Tests Updates
    st.markdown("""
    <div class="report-section">
        <h2>Report</h2>
        <p>The results of the ANOVA tests are summarized in the table below. The F-value indicates the ratio of variance between groups to the variance within groups, while the P-value assesses the probability that the observed differences are due to chance.</p>      
        <h3>Step 3: Modelling (Hypothesis Testing)</h3>
        <p>In this step, we used ANOVA (Analysis of Variance) to analyze differences in customer behavior across different segments. The key variables we modeled and tested include:</p>
        <ul>
            <li><strong>Mean Purchase Amount</strong> across different <strong>age groups</strong> and <strong>income brackets</strong>.</li>
            <li><strong>Mean Purchase Frequency</strong> across different <strong>regions</strong>.</li>
            <li><strong>Mean Loyalty Score</strong> across <strong>age groups</strong> and <strong>regions</strong>.</li>
        </ul>
        <p><strong>Hypothesis Tests:</strong></p>
        <ul>
            <li>Null Hypothesis (H0): There is no significant difference in the metric (e.g., purchase amount) across the groups.</li>
            <li>Alternative Hypothesis (HA): There is a significant difference in the metric across the groups.</li>
        </ul>
        <p>We calculated the F-value and P-value for each hypothesis to assess whether the differences observed were statistically significant. The results are presented in the table format above.</p>
        <h3>Step 4: Accuracy Tests (Validation)</h3>
        <p>To ensure the reliability and significance of the findings from the hypothesis tests, the following steps were taken:</p>
        <ul>
            <li>ANOVA Tests were applied to evaluate the statistical differences in customer behavior metrics (e.g., purchase amount, frequency, loyalty score) across segments.</li>
            <li>The P-value was used as the key indicator of significance. A P-value less than 0.05 indicated a statistically significant difference, leading us to reject the null hypothesis and accept the alternative hypothesis.</li>
        </ul>
        <p>Each test revealed significant differences across the groups, confirming that age groups, income brackets, and regions influence customer behavior metrics. These results provide valuable insights for further modeling or strategy development.</p>
        <h3>Summary of Results:</h3>
        <ul>
            <li><strong>Mean Purchase Amount by Age Group:</strong> The F-value of 308.02 and P-value of 0.0000 indicate a highly significant difference in purchase amounts between different age groups.</li>
            <li><strong>Mean Purchase Amount by Income Bracket:</strong> An F-value of 602.66 and P-value of 0.0000 show a very significant difference in purchase amounts across different income brackets.</li>
            <li><strong>Mean Purchase Frequency by Region:</strong> The F-value of 20.00 and P-value of 0.0000 suggest a significant difference in purchase frequency across regions.</li>
            <li><strong>Mean Loyalty Score by Age Group:</strong> With an F-value of 257.80 and P-value of 0.0000, there is a significant variation in loyalty scores between age groups.</li>
            <li><strong>Mean Loyalty Score by Region:</strong> The F-value of 20.15 and P-value of 0.0000 indicate a significant difference in loyalty scores between regions.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
