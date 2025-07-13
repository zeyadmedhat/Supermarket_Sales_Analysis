
import pandas as pd
import plotly.express as px
import streamlit as st

# Page layout
st.set_page_config(page_title='Supermarket Sales Analysis', layout='wide', page_icon=':shopping_cart:')

# Title
st.markdown("""
    <h1 style='text-align: center; color: white;'>Supermarket Sales Analysis</h1>
    <p style='text-align: center; color: white;'>An interactive analysis of supermarket sales data</p>
""", unsafe_allow_html=True)

page = st.sidebar.radio('Pages', ['Home', 'Uni-variate Analysis', 'Bi-variate Analysis', 'Multi-variate Analysis'])

df = pd.read_csv('supermarket_sales_analysis.csv')
df['Date'] = pd.to_datetime(df['Date'])

if page == 'Home':
    # An image
    st.markdown("""
    <div style='text-align: center;'>
        <img src='https://raw.githubusercontent.com/TheMrityunjayPathak/Super-Market-Sales-Analysis/main/images/supermarket.jpg' style='max-width: 60%; height: auto;'>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced welcome message
    st.subheader('Welcome to the Supermarket Sales Analysis App!')
    st.write("""
        Explore the insights of supermarket sales data with interactive visualizations.
        Use the sidebar to navigate through various analyses and discover trends, patterns, and key metrics.
    """)

    # Summary section
    st.subheader('What You Can Do')
    st.write("""
        - Analyze sales trends over time.
        - Compare sales across different branches and product lines.
        - Visualize customer demographics and preferences.
        - Gain insights into sales performance and customer behavior.
    """)

    # Improved data description
    st.subheader('Dataset Overview')
    st.dataframe(df)
    st.write("""
        The dataset includes the following key features:
        - **Invoice ID**: Unique identifier for each transaction
        - **Branch**: Store location
        - **City**: City of the store
        - **Customer Type**: Type of customer (e.g., Member, Normal)
        - **Gender**: Gender of the customer
        - **Product Line**: Category of products sold
        - **Unit Price**: Price per unit of product
        - **Quantity**: Number of units sold
        - **Tax 5%**: Tax applied to the sale
        - **Total**: Total sale amount
        - **Date**: Date of transaction
        - **Time**: Time of transaction
        - **Payment Method**: Method of payment used
        - **Rating**: Customer rating of the transaction
    """)

    # Navigation tips
    st.subheader('Navigation Tips')
    st.write("""
        - Use the sidebar to switch between different analysis pages.
        - Select columns and chart types to customize your visualizations.
        - Hover over charts for detailed information.
    """)
 

# Uni-variate Analysis
elif page == 'Uni-variate Analysis':

    # Read the data
    st.subheader('Data Overview')

    st.dataframe(df.head())

    df_coloumns = df.columns.drop(['Invoice ID', 'Time', 'Date'])

    st.subheader('Uni-variate Analysis')

    col = st.selectbox('Select Column for Analysis', df_coloumns)

    chart = st.selectbox('Select Chart Type', ['Histogram', 'Box Plot', 'Pie Chart'])

    if chart == 'Histogram':
        if df[col].dtype == 'object':
            ordered_categories = df[col].value_counts().index.tolist()
            fig = px.histogram(data_frame=df, y=col, color=col,
                                category_orders={col: ordered_categories},
                                text_auto=True,
                                title=f'{col} Distribution')
            st.plotly_chart(fig)
        else:
            fig = px.histogram(data_frame=df, y=col, text_auto=True, title=f'{col} Distribution')
            st.plotly_chart(fig)

    elif chart == 'Box Plot':
        if df[col].dtype == 'object':
            st.warning('Box plot is only applicable for numerical data.')
        else:
            fig = px.box(data_frame=df, y=col, title=f'{col} Distribution')
            st.plotly_chart(fig)

    elif chart == 'Pie Chart':
        if df[col].dtype == 'object':
            fig = px.pie(data_frame=df, names=col,title=f'{col} Distribution')
            st.plotly_chart(fig)
        else:
            st.warning('Pie chart is only applicable for categorical data.')


# Bi-variate Analysis
elif page == 'Bi-variate Analysis':

    # Read the data
    st.subheader('Data Overview')

    st.dataframe(df.head())

    df_coloumns = df.columns.drop('Invoice ID')

    st.subheader('Bi-variate Analysis')

    first_col = st.selectbox('Select First Column', df_coloumns)
    second_col = st.selectbox('Select Second Column', df_coloumns)

    chart_type = st.selectbox('Select Chart Type', ['Scatter Plot', 'Histogram', 'Line Chart'])

    if chart_type == 'Scatter Plot':
        if df[first_col].dtype == 'object' or df[second_col].dtype == 'object':
            st.warning('Scatter plot is only applicable for numerical data.')
        else:
            fig = px.scatter(data_frame=df, x=first_col, y=second_col, title=f'{first_col} vs {second_col} Distribution')
            st.plotly_chart(fig)

    elif chart_type == 'Histogram':
        if df[first_col].dtype == 'object' and df[second_col].dtype == 'object':
            st.warning('Histogram is only applicable for numerical data or categorical data.')
        else:
            fig = px.histogram(data_frame=df, x=first_col, y=second_col, 
                                text_auto=True, 
                                title=f'{first_col} vs {second_col} Distribution')
            st.plotly_chart(fig)

    elif chart_type == 'Line Chart':
        if df[first_col].dtype == 'object' or df[second_col].dtype == 'object':
            st.warning('Line chart is only applicable for numerical data.')
        else:
            # Sort the DataFrame by the first column (x-axis)
            df_sorted = df.sort_values(by=first_col)
            fig = px.line(data_frame=df_sorted, x=first_col, y=second_col, title=f'{first_col} vs {second_col} Distribution')
            st.plotly_chart(fig)


# Multi-variate Analysis
elif page == 'Multi-variate Analysis':

    # Read the data
    st.subheader('Data Overview')

    st.dataframe(df.head())

    df_coloumns = df.columns.drop(['Invoice ID', 'Time', 'Date'])

    st.subheader('Multi-variate Analysis')

    first_col = st.selectbox('Select First Column', df_coloumns)
    second_col = st.selectbox('Select Second Column', df_coloumns)
    color_col = st.selectbox('Select Color Column', df_coloumns)

    chart_type = st.selectbox('Select Chart Type', ['Histogram', 'Box Plot'])

    if chart_type == 'Histogram':
        if df[first_col].dtype == 'object' and df[second_col].dtype == 'object' and df[color_col].dtype == 'object':
            st.warning('Histogram is only applicable for numerical data or categorical data.')
        else:
            fig = px.histogram(data_frame=df, x=first_col, y=second_col, color=color_col, text_auto=True, 
                                barmode='group',
                                 title=f'{first_col} vs {second_col} by {color_col} Distribution')
            st.plotly_chart(fig)

    elif chart_type == 'Box Plot':
        if df[first_col].dtype == 'object' or df[second_col].dtype == 'object' or df[color_col].dtype == 'object':
            st.warning('Box plot is only applicable for numerical data.')
        else:
            fig = px.box(data_frame=df, x=first_col, y=second_col, color=color_col, title=f'{first_col} vs {second_col} by {color_col} Distribution')
            st.plotly_chart(fig)
