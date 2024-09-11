import streamlit as st
import pandas as pd
import plotly.express as px
from filters import apply_filters
import scipy.stats as stats

def load_css(file_name):
    with open(file_name) as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def custom_card(title, value, content):
    st.markdown(f"""
    <div class="custom-card">
        <h4>{title}</h4>
        <p class="value">{value}</p>
        <p class="content">{content}</p>
    </div>
    """, unsafe_allow_html=True)
    
def chi_square_test(df, column_name):
    """
    Perform a chi-square test for the distribution of a categorical variable.

    Parameters:
    df (pd.DataFrame): DataFrame containing the data.
    column_name (str): The column name for the categorical variable.

    Returns:
    chi2_stat (float): The chi-square statistic.
    p_value (float): The p-value of the test.
    """
    contingency_table = pd.crosstab(index=df[column_name], columns='count')
    chi2_stat, p_value, _, _ = stats.chi2_contingency(contingency_table)
    return chi2_stat, p_value

    
def calculate_avg_loyalty_by_region(df):
    """
    Calculate the average loyalty score by region.

    Parameters:
    df (pd.DataFrame): DataFrame containing customer data with 'region' and 'loyalty_score' columns.

    Returns:
    pd.DataFrame: DataFrame with 'region' and 'avg_loyalty_score' columns.
    """
    avg_loyalty_by_region = df.groupby('region')['loyalty_score'].mean().reset_index()
    avg_loyalty_by_region.columns = ['region', 'avg_loyalty_score']
    return avg_loyalty_by_region

def calculate_avg_purchase_frequency_by_region(df):
    """
    Calculate the average purchase frequency by region.

    Parameters:
    df (pd.DataFrame): DataFrame containing customer data with 'region' and 'purchase_frequency' columns.

    Returns:
    pd.DataFrame: DataFrame with 'region' and 'avg_purchase_frequency' columns.
    """
    avg_purchase_frequency_by_region = df.groupby('region')['purchase_frequency'].mean().reset_index()
    avg_purchase_frequency_by_region.columns = ['region', 'avg_purchase_frequency']
    return avg_purchase_frequency_by_region

def perform_eda(df):
    # Load custom CSS
    load_css('styles.css')

    # Apply filters
    filtered_df, age_group, income_bracket = apply_filters(df)
    
    if filtered_df.empty:
        st.write("No data available for the selected filters.")
        return


    # Overview Section
    st.header('Overview')

    # Create columns
    col1, col2, col3, col4 = st.columns(4, gap="medium")

    # Populate columns with metrics
    with col1:
        custom_card('Total Number of Customers', str(filtered_df['user_id'].nunique()), 'Total Customers')
    with col2:
        custom_card('Average Purchase Amount', f"${filtered_df['purchase_amount'].mean():.2f}", 'Average Purchase Amount')
    with col3:
        custom_card('Average Purchase Frequency', f"{filtered_df['purchase_frequency'].mean():.2f}", 'Average Purchase Frequency')
    with col4:
        custom_card('Mean Loyalty Score', f"{filtered_df['loyalty_score'].mean():.2f}", 'Mean Loyalty Score')

    # Create columns with small gap
    col1, col2, col3 = st.columns((1.5, 4.5, 2), gap="small")
    
    # Placeholder content for column 1 and 2
    with col1:
        st.subheader("Distribution by Age Group")
        age_group_distribution = filtered_df['age_group'].value_counts().reset_index()
        age_group_distribution.columns = ['age_group', 'count']
        fig_age_group_pie = px.pie(age_group_distribution, names='age_group', values='count', title="Age Group Distribution")
        st.plotly_chart(fig_age_group_pie)

        st.subheader("Distribution by Income Bracket")
        income_bracket_distribution = filtered_df['income_bracket'].value_counts().reset_index()
        income_bracket_distribution.columns = ['income_bracket', 'count']
        fig_income_bracket_pie = px.pie(income_bracket_distribution, names='income_bracket', values='count', title="Income Bracket Distribution")
        st.plotly_chart(fig_income_bracket_pie)
    with col2:
        st.subheader("Correlation Heatmap")
        
        # Filter numeric columns for correlation heatmap
        numeric_df = filtered_df.select_dtypes(include=['number']).drop(columns=['user_id'])
        corr_matrix = numeric_df.corr()
        
        fig_corr_heatmap = px.imshow(corr_matrix, text_auto=True, title="Correlation Heatmap")
        st.plotly_chart(fig_corr_heatmap)
        
        st.subheader("Distribution of Purchase Amounts")
        fig_purchase_amount = px.histogram(filtered_df, x='purchase_amount', nbins=30, title="Distribution of Purchase Amounts")
        st.plotly_chart(fig_purchase_amount)

        st.subheader("Purchase Frequency by Age Group")
        fig_purchase_frequency_age = px.bar(filtered_df.groupby('age_group')['purchase_frequency'].mean().reset_index(),
                                            x='age_group', y='purchase_frequency', title="Purchase Frequency by Age Group")
        st.plotly_chart(fig_purchase_frequency_age)

        st.subheader("Loyalty Score by Income Bracket")
        fig_loyalty_income = px.box(filtered_df, x='income_bracket', y='loyalty_score', title="Loyalty Score by Income Bracket")
        st.plotly_chart(fig_loyalty_income)       
        

    # Column 3: Dataset and About Section
    with col3:
        st.subheader("Loyalty score by region")
        
        # Calculate average loyalty score by region and display as a styled table
        avg_loyalty_by_region = calculate_avg_loyalty_by_region(filtered_df)
        
        # Generate HTML table with custom styling
        st.markdown("""
        <table>
            <tr>
                <th>Region</th>
                <th>Average Loyalty Score</th>
            </tr>
            """ + "".join(
                f"<tr><td>{row['region']}</td><td><div class='progress-bar-container'><div class='progress-bar' style='width: {row['avg_loyalty_score']/avg_loyalty_by_region['avg_loyalty_score'].max()*100}%;'>{row['avg_loyalty_score']:.2f}</div></div></td></tr>"
                for _, row in avg_loyalty_by_region.iterrows()
            ) + """
        </table>
        """, unsafe_allow_html=True)
        
        st.subheader ("Purchase Frequency by region")
        
        # Calculate average purchase frequency by region and display as a styled table
        avg_purchase_frequency_by_region = calculate_avg_purchase_frequency_by_region(filtered_df)
        
        # Generate HTML table with custom styling
        st.markdown("""
        <table>
            <tr>
                <th>Region</th>
                <th>Average Loyalty Score</th>
            </tr>
            """ + "".join(
                f"<tr><td>{row['region']}</td><td><div class='progress-bar-container'><div class='progress-bar' style='width: {row['avg_purchase_frequency']/avg_purchase_frequency_by_region['avg_purchase_frequency'].max()*100}%;'>{row['avg_purchase_frequency']:.2f}</div></div></td></tr>"
                for _, row in avg_purchase_frequency_by_region.iterrows()
            ) + """
        </table>
        """, unsafe_allow_html=True)
        
        # Chi-Square Test for Region
        st.subheader("Chi-Square Test for Regions")
        chi2_stat, p_value = chi_square_test(filtered_df, 'region')
        st.write(f"Chi-Square Statistic: {chi2_stat:.2f}")
        st.write(f"P-Value: {p_value:.4f}")

        # Interpretation of the chi-square test result
        if p_value < 0.05:
            st.write("The p-value is less than 0.05, indicating that the distribution of regions is significantly different from what would be expected by chance.")
        else:
            st.write("The p-value is greater than 0.05, indicating that the distribution of regions is not significantly different from what would be expected by chance.")
       
        
        
        
        st.subheader("Download Dataset")
        st.markdown("""
        You can download the dataset used for this analysis from the following link:
        [Customer Purchasing Behaviors Dataset](https://www.kaggle.com/datasets/hanaksoy/customer-purchasing-behaviors/data)
        """)
        
        st.subheader("About the Project")
        st.markdown("""
        This project analyzes customer purchasing behavior and segmentation using various metrics such as purchase amount, 
        purchase frequency, and loyalty score. The goal is to understand how these metrics vary by different customer attributes 
        like age group, income bracket, and region.

        Key objectives include:
        - Understanding customer behavior patterns.
        - Identifying significant differences in purchasing metrics across various segments.
        - Providing actionable insights for targeted marketing strategies.

        The dataset used for this analysis includes customer attributes and purchasing data, which helps in segmenting and 
        analyzing customer behavior effectively.
        """)
