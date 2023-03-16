
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Madrid Real Estate Valuator',
                  layout='wide',
                  initial_sidebar_state='expanded')


model = st.container()

with model:

    import streamlit as st
    import pandas as pd
    from sklearn.linear_model import LinearRegression

    # Load the data
    df = pd.read_csv(r"C:\Users\DavidVicente\Desktop\IronHack\Final_Project\Apartment_Valuator\Data\model_df.csv")
    
    # Define the features and target variable
    X = df[['sq_mt_built', 'n_rooms', 'n_bathrooms', 'floor', 'house_type_id', 
            'is_new_development', 'has_ac', 'has_fitted_wardrobes', 'has_lift',
            'is_exterior', 'has_garden', 'has_pool', 'has_terrace', 'has_balcony',
            'has_storage_room', 'is_accessible', 'has_green_zones', 'has_parking',
            'District_code']]
    y = df['buy_price']

    # Create a Linear Regression model and fit it to the data
    lr = LinearRegression()
    lr.fit(X, y)

    # Set up the Streamlit app
    st.title("Predicting House Prices")

    # Setting Dictionaries

    yes_no_dict = {0:'No', 1:'Yes'}

    rooms_number = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6 or More'}

    bathrooms_number = {1:'1',2:'2',3:'3',4:'4',5:'5 or More'}

    floor_info = {1:'1st',2:'2nd',3:'3rd',4:'4th',5:'5th',6:'6th',7:'7th',8:'8th',9:'9th',10:'Basement Apartment',11:'House'}

    house_type = {1:'Apartment',2:'Duplex',3:'Penthouse',4:'House or Chalet'}

    district_info = {1:'Arganzuela',2:'Barajas',3:'Carabanchel',4:'Centro',
                     5:'Chamartín',6:'Chamberí',7:'Ciudad Lineal',8:'Ciudad Lineal',
                     9:'Hortaleza', 10:'Latina', 11:'Moncloa', 12:'Moratalaz', 13:'Puente de Vallecas',
                     14:'Retiro',15:'Salamanca', 17:'Tetuán',18:'Usera',19:'Vicálvaro',20:'Villa de Vallecas',
                     21:'Villaverde'}


    # Input values for the features
    sq_mt_built = st.number_input('Enter the square meters built:', min_value=0.0)
    
    
    # n_rooms = st.number_input('Enter the number of rooms:', min_value=0, step=1)
    # n_bathrooms = st.number_input('Enter the number of bathrooms:', min_value=0, step=1)
    # floor = st.number_input('Enter the floor number:', min_value=0, step=1)
    # house_type_id = st.number_input('Enter the house type:', min_value=0, step=1)

    
    
    # Select Box Inputs
    
    district_code = st.selectbox('Enter the district code:', [district_info[1],district_info[2],district_info[3],district_info[4],district_info[5],
                                 district_info[6],district_info[7],district_info[8],district_info[9],district_info[10],district_info[11],district_info[12],
                                 district_info[13],district_info[14],district_info[15],district_info[17],district_info[18],district_info[19],district_info[20],
                                 district_info[21]])
    
    n_rooms = st.selectbox('Select number of rooms:',[rooms_number[0],rooms_number[1],rooms_number[2],rooms_number[3],rooms_number[4],rooms_number[5],rooms_number[6]])
    n_bathrooms = st.selectbox('Select the number of bathrooms:', [bathrooms_number[1],bathrooms_number[2],bathrooms_number[3],bathrooms_number[4],bathrooms_number[5]])
    floor = st.selectbox('Enter the floor number:', [floor_info[10],floor_info[1],floor_info[2],floor_info[3],floor_info[4],floor_info[5],floor_info[6],floor_info[7],floor_info[8],floor_info[9],floor_info[11]])
    house_type_id = st.selectbox('Enter the house type:', [house_type[1],house_type[2],house_type[3],house_type[4]])

    # Radio box inputs

    is_new_development = st.radio('Is it a new development?', [yes_no_dict[1], yes_no_dict[0]])
    has_ac = st.radio('Does it have air conditioning?', [yes_no_dict[1], yes_no_dict[0]])
    has_fitted_wardrobes = st.radio('Does it have fitted wardrobes?', [yes_no_dict[1], yes_no_dict[0]])
    has_lift = st.radio('Does it have a lift?', [yes_no_dict[1], yes_no_dict[0]])
    is_exterior = st.radio('Is it exterior?', [yes_no_dict[1], yes_no_dict[0]])
    has_garden = st.radio('Does it have a garden?', [yes_no_dict[1], yes_no_dict[0]])
    has_pool = st.radio('Does it have a pool?', [yes_no_dict[1], yes_no_dict[0]])
    has_terrace = st.radio('Does it have a terrace?', [yes_no_dict[1], yes_no_dict[0]])
    has_balcony = st.radio('Does it have a balcony?', [yes_no_dict[1], yes_no_dict[0]])
    has_storage_room = st.radio('Does it have a storage room?', [yes_no_dict[1], yes_no_dict[0]])
    is_accessible = st.radio('Is it accessible?', [yes_no_dict[1], yes_no_dict[0]])
    has_green_zones = st.radio('Does it have green zones?', [yes_no_dict[1], yes_no_dict[0]])
    has_parking = st.radio('Does it have parking?', [yes_no_dict[1], yes_no_dict[0]])


    
    # Changing the values selected by the user


    yes_no_dict = {'No':0, 'Yes':1}


    is_new_development = yes_no_dict[is_new_development]
    has_ac = yes_no_dict[has_ac]
    has_fitted_wardrobes = yes_no_dict[has_fitted_wardrobes]
    has_lift = yes_no_dict[has_lift]
    is_exterior = yes_no_dict[is_exterior]
    has_garden = yes_no_dict[has_garden]
    has_pool = yes_no_dict[has_pool]
    has_terrace = yes_no_dict[has_terrace]
    has_balcony = yes_no_dict[has_balcony]
    has_storage_room = yes_no_dict[has_storage_room]
    is_accessible = yes_no_dict[is_accessible]
    has_green_zones = yes_no_dict[has_green_zones]
    has_parking = yes_no_dict[has_parking]


    # Rooms dict
    rooms_number = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6 or More':6}
    n_rooms = rooms_number[n_rooms]


    # bath dict
    bathrooms_number = {'1':1,'2':2,'3':3,'4':4,'5 or More':5}
    n_bathrooms = bathrooms_number[n_bathrooms]

    #floor dict
    floor_info = {'1st':1,'2nd':2,'3rd':3,'4th':4,'5th':5,'6th':6,'7th':7,'8th':8,'9th':9,'Basement Apartment':10,'House':11}
    floor = floor_info[floor]


    # House dict
    house_type = {'Apartment':1,'Duplex':2,'Penthouse':3,'House or Chalet':4}
    house_type_id = house_type[house_type_id]

    # Distric dict

    district_info = {'Arganzuela':1,'Barajas':2,'Carabanchel':3,'Centro':4,
                     'Chamartín':5,'Chamberí':6,'Ciudad Lineal':7,'Ciudad Lineal':8,
                     'Hortaleza':9, 'Latina':10, 'Moncloa':11, 'Moratalaz':12,'Puente de Vallecas':13,
                     'Retiro':14,'Salamanca':15,'Tetuán':17,'Usera':18,'Vicálvaro':19,'Villa de Vallecas':20,
                     'Villaverde':21}

    district_code = district_info[district_code]


    def predict():
        # Make a prediction based on the input values

        
        prediction = lr.predict([[sq_mt_built, n_rooms, n_bathrooms, floor, house_type_id, 
                                is_new_development, has_ac, has_fitted_wardrobes, has_lift,
                                is_exterior, has_garden, has_pool, has_terrace, has_balcony,
                                has_storage_room, is_accessible, has_green_zones, has_parking,
                                district_code]])
        
        prediction_1 = prediction*0.95
        prediction_2 = prediction*1.05
        
        # st.write(f'The predicted buy price is between: {prediction_1[0]:,.2f} - {prediction_2[0]:,.2f}', font_size=1500)

        # st.markdown(f'<div style="font-size: 200%; width: 50%; padding: 10px; background-color: lightgray;">The predicted buy price is between: {prediction_1[0]:,.2f} EUR - {prediction_2[0]:,.2f} EUR</div>', unsafe_allow_html=True)

        st.markdown(f"""
            <style>
                .result-container {{
                    background-color: #F4F4F4;
                    border-radius: 10px;
                    padding: 20px;
                    box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
                    font-size: 68px;
                    width: 80%;
                    text-align: center;
                    margin: auto;
                    margin-top: 50px;
                    margin-bottom: 50px;
                }}
                .result-container p {{
                    font-size: 30px;
            </style>
            <div class="result-container">
                <p>The predicted buy price is between:</p>
                <h1>{prediction_1[0]:,.2f} EUR - {prediction_2[0]:,.2f} EUR </h1>
            </div>
        """, unsafe_allow_html=True)

    # st.button('Predict', on_click=predict)

    st.button('Predict', on_click=lambda: predict())



   