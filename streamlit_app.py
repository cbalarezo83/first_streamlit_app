
import streamlit;

streamlit.title('My parents new healthy diner');
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas;

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries']);
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

import requests;
streamlit.header('Fruityvice Fruit Advice !')
fruit_choice = streamlit.text_input('What fruit dude?','Kiwi')
streamlit.write('User entered',fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector 

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list where fruit_name <>'' ")
#my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit list contains :")
streamlit.dataframe(my_data_rows)

add_fruit = streamlit.text_input('Which fruit to add ?')
my_cur.execute("insert into fruit_load_list values('" + add_fruit + "')" )
