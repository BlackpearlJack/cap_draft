import streamlit as st
import plotly.express as px
import pandas as pd

def perform_eda(df):
    # Sidebar for Filters
    st.sidebar.header("Filters")
    
    selected_income_bracket = st.sidebar.multiselect(
        "Select Income Bracket(s)",
        options=df['income_bracket'].unique(),
        default=df['income_bracket'].unique()
    )
    
    selected_age_group = st.sidebar.multiselect(
        "Select Age Group(s)",
        options=df['age_group'].unique(),
        default=df['age_group'].unique()
    )
    
    selected_region = st.sidebar.multiselect(
        "Select Region(s)",
        options=df['region'].unique(),
        default=df['region'].unique()
    )
    
    selected_loyalty_score = st.sidebar.slider(
        "Select Loyalty Score Range",
        min_value=float(df['loyalty_score'].min()),
        max_value=float(df['loyalty_score'].max()),
        value=(float(df['loyalty_score'].min()), float(df['loyalty_score'].max()))
    )
    
    # Filter the dataframe based on selected options
    filtered_df = df[
        (df['income_bracket'].isin(selected_income_bracket)) &
        (df['age_group'].isin(selected_age_group)) &
        (df['region'].isin(selected_region)) &
        (df['loyalty_score'].between(*selected_loyalty_score))
    ]
    
    # Key Metrics Section
    st.markdown("### Key Metrics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_customers = filtered_df['user_id'].nunique()
        avg_age = filtered_df['age'].mean()
        st.metric("Total Customers", total_customers)
        st.metric("Average Age", f"{avg_age:.1f}")
    
    with col2:
        avg_purchase_amount = filtered_df['purchase_amount'].mean()
        avg_annual_income = filtered_df['annual_income'].mean()
        st.metric("Average Purchase Amount", f"${avg_purchase_amount:.2f}")
        st.metric("Average Annual Income", f"${avg_annual_income:.2f}")
    
    with col3:
        avg_loyalty_score = filtered_df['loyalty_score'].mean()
        avg_purchase_frequency = filtered_df['purchase_frequency'].mean()
        st.metric("Average Loyalty Score", f"{avg_loyalty_score:.2f}")
        st.metric("Average Purchase Frequency", f"{avg_purchase_frequency:.1f}")
    
    st.markdown("---")
    
    # Summary Statistics in a Dropdown
    with st.expander("Summary Statistics"):
        st.markdown("### Summary Statistics")
        st.write(filtered_df.describe())
    
    st.markdown("---")
    
    # Distribution Plots
    st.markdown("### Distributions")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Age Distribution")
        fig = px.histogram(filtered_df, x='age', nbins=20, title='Age Distribution')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### Annual Income Distribution")
        fig = px.histogram(filtered_df, x='annual_income', nbins=20, title='Annual Income Distribution')
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Purchase Amount Distribution")
        fig = px.histogram(filtered_df, x='purchase_amount', nbins=20, title='Purchase Amount Distribution')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### Purchase Frequency Distribution")
        fig = px.histogram(filtered_df, x='purchase_frequency', nbins=20, title='Purchase Frequency Distribution')
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Box Plots
    st.markdown("### Box Plots by Age Group and Income Bracket")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Purchase Amount by Age Group")
        fig = px.box(filtered_df, x='age_group', y='purchase_amount', title='Purchase Amount by Age Group')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### Purchase Frequency by Age Group")
        fig = px.box(filtered_df, x='age_group', y='purchase_frequency', title='Purchase Frequency by Age Group')
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Purchase Amount by Income Bracket")
        fig = px.box(filtered_df, x='income_bracket', y='purchase_amount', title='Purchase Amount by Income Bracket')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### Purchase Frequency by Income Bracket")
        fig = px.box(filtered_df, x='income_bracket', y='purchase_frequency', title='Purchase Frequency by Income Bracket')
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Scatter Plots
    st.markdown("### Scatter Plots")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Purchase Amount vs Age")
        fig = px.scatter(filtered_df, x='age', y='purchase_amount', trendline='ols', title='Purchase Amount vs Age')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### Purchase Frequency vs Age")
        fig = px.scatter(filtered_df, x='age', y='purchase_frequency', trendline='ols', title='Purchase Frequency vs Age')
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Purchase Amount vs Annual Income")
        fig = px.scatter(filtered_df, x='annual_income', y='purchase_amount', trendline='ols', title='Purchase Amount vs Annual Income')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### Purchase Frequency vs Annual Income")
        fig = px.scatter(filtered_df, x='annual_income', y='purchase_frequency', trendline='ols', title='Purchase Frequency vs Annual Income')
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Correlation Heatmap
    st.markdown("### Correlation Heatmap")
    corr_matrix = filtered_df[['age', 'annual_income', 'purchase_amount', 'purchase_frequency', 'loyalty_score']].corr()
    fig = px.imshow(corr_matrix, 
                text_auto=True, 
                aspect="auto", 
                color_continuous_scale='RdBu_r', 
                title='Correlation Matrix Heatmap')
    st.plotly_chart(fig, use_container_width=True)
