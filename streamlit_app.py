import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("Hii guys")

streamlit.header("Breakfast Menu")
streamlit.text("🥣Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗Kale,Spinach & Rocket Smoothiee")
streamlit.text("🐔Hard-Boiled Free-Range egg")
streamlit.text("🥑🍞Avocado Toast")
streamlit.header("'🍌🥭 Build Your Own Fruit Smoothie 🥝🍇'")   


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response= requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())      # taking the json version of the response and normalise it
    return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")

try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
       streamlit.error('Please select a fruit to get information.')
   else:  
       backfrom_function= get_fruityvice_data(fruit_choice)  
       streamlit.dataframe(backfrom_function)    # output it in the screen as a table
except URLError as e:
   streamlit.error()


# streamlit.stop()
streamlit.header("View Our Fruit List-Add Your Favourites!")
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
       my_cur.execute("select * from fruit_load_list")
       return my_cur.fetchall()

if streamlit.button('Get Fruit load list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows= get_fruit_load_list()
   my_cnx.close()
   streamlit.dataframe(my_data_rows)
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

# my_data_rows = my_cur.fetchall()

# streamlit.dataframe(my_data_rows)

def insert_fruit_snowflake(newfruit):
   with my_cnx.cursor() as my_cur:
       my_cur.execute("insert into fruit_load_list values ('"+newfruit+"')")
       return 'thanks for adding '+newfruit

fruit_add = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    backfrom_function= insert_fruit_snowflake(fruit_add)
    streamlit.text(backfrom_function)
# streamlit.write('Thanks for adding ', fruit_add)

# my_cur.execute("insert into fruit_load_list values ('from streamlit')")
