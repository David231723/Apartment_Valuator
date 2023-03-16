import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(page_title='Madrid Real Estate Valuator',
                  layout='wide',
                  initial_sidebar_state='expanded')


header = st.container()

dataset = st.container()


with header:
    st.title('Madrid Real Estate Market Overview')

with dataset:
    st.header('Data Overview')
    st.text('This view is only showing 50 random rows from the df')

    df = pd.read_csv(r"C:\Users\DavidVicente\Desktop\IronHack\Final_Project\Apartment_Valuator\Data\cleaned_df.csv")
    df['eurm2'] = round(df['buy_price'] / df['sq_mt_built'],2)
    sum_df = df[['title','Neighborhood_name','District_name','house_type_id','n_rooms','n_bathrooms','floor','eurm2']]
    st.write(df.sample(50))

    st.header('Districs by EUR/m2')

        # Group the DataFrame by District_name and calculate the median of eurm2
    df_grouped = df.groupby('District_name').agg({'eurm2': 'median'}).reset_index()

    # Sort the DataFrame in descending order based on the median eurm2
    df_grouped = df_grouped.sort_values('eurm2', ascending=True)

    # Calculate the mean eurm2 for color conditional formatting
    mean_eurm2 = df_grouped['eurm2'].mean()

    # Create the horizontal bar chart using Plotly Express with color conditional formatting
    fig = px.bar(df_grouped, x='eurm2', y='District_name',
                orientation='h',
                color='eurm2',
                color_continuous_scale='Blues',
                height=600,
                title='Median EUR/m2 by District ')

    # Set the x-axis title
    fig.update_xaxes(title_text='EUR/m2')

    # Apply color conditional formatting based on the mean eurm2
    fig.update_traces(marker=dict(line=dict(width=1, color='Gray'),
                                color=px.colors.diverging.RdBu_r, 
                                coloraxis_colorbar=dict(title='eurm2'),
                                colorscale='Blues', 
                                reversescale=True),
                    selector=dict(type='bar', marker=dict(color=df_grouped['eurm2']<mean_eurm2)))


    fig.update_layout(width=1500)

    fig.update_layout(margin=dict(l=150))


    # Show the plot
    st.write(fig)



    st.header('Neighborhood by EUR/m2')

    # Group the DataFrame by District_name and calculate the median of eurm2
    df_grouped = df.groupby('Neighborhood_name').agg({'eurm2': 'median'}).reset_index()

    # Sort the DataFrame in descending order based on the median eurm2
    df_grouped = df_grouped.sort_values('eurm2', ascending=True)

    # Calculate the mean eurm2 for color conditional formatting
    mean_eurm2 = df_grouped['eurm2'].mean()

    # Create the horizontal bar chart using Plotly Express with color conditional formatting
    fig = px.bar(df_grouped, x='eurm2', y='Neighborhood_name',
                orientation='h',
                color='eurm2',
                color_continuous_scale='Blues',
                height=600,
                title='Median EUR/m2 by Neighborhood ')

    # Set the x-axis title
    fig.update_xaxes(title_text='EUR/m2')

    # Apply color conditional formatting based on the mean eurm2
    fig.update_traces(marker=dict(line=dict(width=1, color='Gray'),
                                color=px.colors.diverging.RdBu_r, 
                                coloraxis_colorbar=dict(title='eurm2'),
                                colorscale='Blues', 
                                reversescale=True),
                    selector=dict(type='bar', marker=dict(color=df_grouped['eurm2']<mean_eurm2)))

    fig.update_layout(width=1500)


    fig.update_layout(margin=dict(l=200))


    # Show the plot
    st.write(fig)




    st.header('House Type EUR/m2')



    # Group the DataFrame by house_type_id and calculate the median of eurm2
    df_grouped = df.groupby('house_type_id').agg({'eurm2': 'median'}).reset_index()

    # Sort the DataFrame in descending order based on the median eurm2
    df_grouped = df_grouped.sort_values('eurm2', ascending=False)

    # Create the bar chart using Plotly Express
    fig = px.bar(df_grouped, x='house_type_id', y='eurm2',
                color='house_type_id',
                color_discrete_sequence=px.colors.qualitative.Dark2,
                title='Median EUR/m2 by House Type')

    # Set the x-axis title
    fig.update_xaxes(title_text='House Type')

    # Set the y-axis title
    fig.update_yaxes(title_text='Median EUR/m2')

    fig.update_layout(width=1400)



    # Show the plot
    st.write(fig)


    st.header('Price Distribution by House Type')

    fig = px.box(df,x='house_type_id',y='buy_price',color='house_type_id', color_discrete_sequence=px.colors.qualitative.Dark24)

    fig.update_layout(width=1400)

     # Show the plot
    st.write(fig)



    st.header('Price Distribution by Number of rooms')

    fig = px.box(df,x='n_rooms',y='buy_price',color='n_rooms', color_discrete_sequence=px.colors.qualitative.Dark24)

    fig.update_layout(width=1400)

    
    st.write(fig)



    st.header('Top 10 Most Expensive Apartments')

    sorted_df = df.sort_values(by=['buy_price'],ascending=False)

    sorted_df = sorted_df[['title','buy_price','sq_mt_built','n_rooms','n_bathrooms','house_type_id','District_name','Neighborhood_name']]

    st.write(sorted_df.head(10))



    st.header('m2 Price vs Sq Meter Build Median per Neighborhood')

    # Group the DataFrame by District_name, Neighborhood_name and calculate the median of sq_mt_built, n_rooms, and eurm2
    df_grouped = df.groupby(['District_name']).agg({'buy_price': 'median', 'sq_mt_built': 'median', 'eurm2': 'median'}).reset_index()

    # Create the scatter plot using Plotly Express with marker-coded neighborhoods by district
    fig = px.scatter(df_grouped, x='sq_mt_built', y='eurm2',
                    color='District_name',
                    color_discrete_sequence=px.colors.qualitative.Dark24,
                    size='buy_price',
                    size_max=60,
                    hover_name='District_name',
                    hover_data={'buy_price': True, 'sq_mt_built': True, 'eurm2': True, 'District_name': False},
                    custom_data=['District_name'])

    # Set the axis titles
    fig.update_xaxes(title_text='Sq Meter Build')
    fig.update_yaxes(title_text='EUR/m2 Median')

    fig.update_layout(height=800)

    fig.update_layout(width=1400)

    

    # Show the plot
    st.write(fig)






