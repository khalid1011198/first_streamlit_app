import streamlit
import pandas
streamlit.title('My parents new healthy diner')
streamlit.header('Lets see breakfast Menu')
streamlit.text('🐟Fish oil')
streamlit.text('🍀Spinach')
streamlit.text('🥚Eggs')

streamlit.header('Build your own smoothie')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
