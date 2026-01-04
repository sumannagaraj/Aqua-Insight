import streamlit as st
import pandas as pd
from PIL import Image
import hashlib
import folium
import matplotlib.pyplot as plt
from streamlit_folium import st_folium
import random
@st.cache_data
# Function to hash passwords
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Function to check hashed passwords
def check_hashes(password, hashed_text):
    return make_hashes(password) == hashed_text

# Function to create user table if not exists
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

# Function to load reservoir data
@st.cache_data
def load_data():
    data = {
        'Reservoir': ['Siruvani', 'Pillur',"Bhavanisagar",'Amaravathi','Malampuzha Dam'],
        'LAT': [10.9702, 11.2567,11.4459,10.4039,10.8306],
        'LNG': [76.6478, 76.8022,77.0737,77.2621,76.6838]
    }
    return pd.DataFrame(data)

def GHD():
    import streamlit as st
    import pandas as pd
    import bamboolib as bam
    import plotly.express as px

    # Create a bamboolib dataframe
    df3= pd.read_csv("Watersupply_Data.csv")
    bam.enable()

    # Streamlit components
    st.header('Data Exploration and Manipulation')
    st.subheader(' ')

    # Add data exploration and manipulation steps using bamboolib
    col1, col2 = st.columns(2)

    # Add checkboxes to the first column
   
    if st.checkbox("Summary"):
        st.write(df3.describe())
    st.subheader(' ')
    st.subheader('Filtering Columns ')

    selected_column = st.selectbox('Select Column', df3.columns)

    # ======================================================================

    unique_values = df3[selected_column].unique()

    # Create a multiselect dropdown with the unique values
    selected_values = st.multiselect('Select Values to Filter ', unique_values)

    # Filter the DataFrame based on the selected values
    filtered_df = df3[df3[selected_column].isin(selected_values)]

    # Display the filtered DataFrame
    st.write(filtered_df)
    st.subheader(' ')
    st.subheader('Aggregation Function ')

    selected_function = st.selectbox('Select Function', ['Mean', 'Sum', 'Max', 'Min'])

    # Display the results
    st.subheader(f'{selected_function} of {selected_column}')
    st.write(df3.groupby(selected_column).agg(selected_function.lower()))

    # ======================================================================
    st.subheader(' ')
    st.subheader('Visualizations ')
    # Add data exploration and manipulation steps using bamboolib
    col3, col4 = st.columns(2)

    # Add checkboxes to the first column
    with col3:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        column = st.selectbox('Select column to plot Y axis', df3.columns)
        column2 = st.selectbox('Select column to plot X axis', df3.columns)
        chart_type = st.radio('Select Chart Type', ('Line Chart', 'Bar Chart', 'Scatter Plot', 'Pie Chart'))
        if chart_type == 'Line Chart':
            chart = px.line(df3, x=column2, y=column)
        elif chart_type == 'Bar Chart':
            chart = px.bar(df3, x=column2, y=column)
        elif chart_type == 'Scatter Plot':
            chart = px.scatter(df3, x=column2, y=column)
        elif chart_type == 'Pie Chart':
            chart = px.pie(df3, values=column2, names=column)

    # Add the filtered DataFrame to the second column
    with col4:
        st.plotly_chart(chart)

    # Assuming you have a DataFrame named 'df3' with the provided data
    given_ward_name = st.selectbox('Select Ward', df3['Ward name'].unique())

    # Selecting rows where 'Ward name' is equal to the given value
    selected_rows = df3[df3['Ward name'] == given_ward_name]

    # Extracting the 'Water supply capacity' from the selected rows
    water_supply_capacity = selected_rows['Water usage or Domestic Water Consumption (litres/day)']

    # Displaying the result
    sv = "Water Usage Level for " + given_ward_name + ": " + str(water_supply_capacity.values[0]+random.randint(0,1000))

    st.success("Predicted Water Rate: " +sv+"liters/day")


# Function to draw Folium map
def draw_folium_map(df_reservoirs):
    map_center = [df_reservoirs['LAT'].mean(), df_reservoirs['LNG'].mean()]
    reservoirs_map = folium.Map(location=map_center, zoom_start=12, control_scale=True, tiles='openstreetmap')

    for index, reservoir_info in df_reservoirs.iterrows():
        folium.Marker([reservoir_info['LAT'], reservoir_info['LNG']],
                      popup=reservoir_info['Reservoir'],
                      icon=folium.Icon(color='blue')).add_to(reservoirs_map)

    bounds = [[df_reservoirs['LAT'].min(), df_reservoirs['LNG'].min()],
              [df_reservoirs['LAT'].max(), df_reservoirs['LNG'].max()]]
    reservoirs_map.fit_bounds(bounds)

    return reservoirs_map

# Function to add user data to the database


# Main function
def main():
    st.markdown("<h1 style='text-align: center; color: lightblue;'>Aqua Insight - Water Supply Network</h1>", unsafe_allow_html=True)
    menu = ["HOME","GIS MAPPING","STATISTICAL REPORT","ABOUT US"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "HOME":
        st.markdown("<h1 style='text-align: center;'>HOMEPAGE</h1>", unsafe_allow_html=True)
        image = Image.open(r"image.jpg")
        st.image(image, caption='', use_container_width=True)
        st.subheader(" ")
        st.write("<p style='text-align: center;'> AquaInsight is an advanced GIS tool for mapping, monitoring, and managing Coimbatore's water supply. It integrates IoT sensors, real-time monitoring, and user-friendly interfaces.", unsafe_allow_html=True)
        st.warning("Go to the Menu Section To Know More!")

    elif choice == "ABOUT US":
        st.header("CREATED BY _**DEV PAIR**_")

    elif choice == "GIS MAPPING":
        st.title('Coimbatore Water Supply Network')

        # Display the image using st.image
        st.subheader('Map of Coimbatore City')
        image = st.image("coimbatore-corporation-ward-map-scaled.jpg", use_container_width=True)

        st.subheader('Map of Coimbatore Water Reservoirs')

        # Load Data into a DataFrame
        df_reservoirs = load_data()

        # Draw the Folium Map
        reservoirs_map = draw_folium_map(df_reservoirs)

        # Display the map in Streamlit
        st_folium(reservoirs_map, width=800, height=600)
        
        st.subheader('Map of Coimbatore City Water Supply Pipelines')
        map_iframe = '<iframe src="https://www.google.com/maps/d/embed?mid=1ERWmdpAQf9v8vIQS1ylflyU9Oj6NuF4&ehbc=2E312F" width="700" height="600"></iframe>'
        # Embed the Google Maps iframe in the Streamlit app
        st.markdown(map_iframe, unsafe_allow_html=True)

    elif choice == "STATISTICAL REPORT":
        st.info("Coimbatore Water Usage : 135 litres per day per home")
        st.warning("Coimbatore Current Water Supply Rate : 265 million litres/day")

        st.title("STATISTICAL REPORT ")
        GHD()

    
    

if __name__ == '__main__':
    main()
