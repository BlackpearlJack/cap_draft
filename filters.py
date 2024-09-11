import streamlit as st

def apply_filters(df):
    st.sidebar.header('Filters')
    age_group = st.sidebar.multiselect(
        'Select Age Group(s)',
        options=df['age_group'].unique(),
        default=df['age_group'].unique()
    )
    income_bracket = st.sidebar.multiselect(
        'Select Income Bracket(s)',
        options=df['income_bracket'].unique(),
        default=df['income_bracket'].unique()
    )
    # Apply filters to dataframe
    filtered_df = df[
        (df['age_group'].isin(age_group)) &
        (df['income_bracket'].isin(income_bracket))    
    ]

    return filtered_df, age_group, income_bracket
