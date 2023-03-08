import streamlit
import pandas
streamlit.title('My parents new healthy diner')
streamlit.header('Lets see breakfast Menu')
streamlit.text('🐟Fish oil')
streamlit.text('🍀Spinach')
streamlit.text('🥚Eggs')

streamlit.header('Build your own smoothie')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# putting a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

streamlit.dataframe(my_fruit_list)
