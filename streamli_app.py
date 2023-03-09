import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

# create a function
def get_fruityvice_response (this_fruit_choice):
       fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
       fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       return fruityvice_normalized

       
       
streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Favorites')

streamlit.text('\U0001F44D Omega 3 & Bueberry Oatmel')
streamlit.text('🦻 Kale, Spinach & Rocket Smoothy')
streamlit.text('🧠 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)),['Avocado','Strawberries'])
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('FruityVice Fruit Advise')
try:
   fruit_choice = streamlit.text_input("What fruit would you like information about?")
   if not fruit_choice:
     streamlit.error("Please select a fruit to get information")
   else:
       back_from_function = get_fruityvice_response(fruit_choice)
       #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
       #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       # write your own comment - what does this do?
       streamlit.dataframe(back_from_function)
        
except URLerror as e:
  streamlit.error()
      
#streamlit.write('The user entered ', fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon" + fruit_choice)
#streamlit.text(fruityvice_response.json())

# write your own comment 

#my_cur = my_cnx.cursor()
streamlit.header("The Fruit List Contains")
#create function
def get_fruit_load_list():
    with  my_cnx.cursor() as my_cur:
       my_cur.execute("Select * from fruit_load_list")
       return my_cur.fetchall()

# Create a button
if streamlit.button('View Out Fruit List Add Your Favorites'):   
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])    
   my_data_row2 = get_fruit_load_list()
   my_cnx.close()
   streamlit.dataframe(my_data_row2)    

#streamlit.stop()
my_cnx2 = snowflake.connector.connect(**streamlit.secrets["snowflake"]) 
my_cur2 =  my_cnx2.cursor()
add_my_fruit = streamlit.text_input("What fruit would you like to add?")
my_cur2.execute ( "insert into fruit_load_list values ('" + add_my_fruit + "')")
my_cnx2.close()
streamlit.write('Thanks For Adding ', add_my_fruit)

#insert_query = "INSERT INTO sqlite_tablename (email, firstname, lastname) values %s"
#insert into fruit_load_list_2 (FRUIT_NAME) select  'jackfruit';
