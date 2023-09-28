import streamlit

streamlit.title("Hii guys")

streamlit.header("Breakfast Menu")
streamlit.text("🥣Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗Kale,Spinach & Rocket Smoothiee")
streamlit.text("🐔Hard-Boiled Free-Range egg")
streamlit.text("🥑🍞Avocado Toast")
streamlit.header("'🍌🥭 Build Your Own Fruit Smoothie 🥝🍇'")   

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
# streamlit.text(fruityvice_response.json())

# taking the json version of the response and normalise it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it in the screen as a table
streamlit.dataframe(fruityvice_normalized)
