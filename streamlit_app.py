import streamlit;
import pandas;
import requests;
import snowflake.connector 

streamlit.title('My parents new healthy diner');
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#import pandas;

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries']);
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#import requests;

def get_fruityvice_data ( this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
      return pandas.json_normalize(fruityvice_response.json())

streamlit.header('Fruityvice Fruit Advice !')

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
  else:
      streamlit.dataframe(get_fruityvice_data(fruit_choice))
except URLError as e:
    streamlit.error()



#import snowflake.connector 

streamlit.header("The fruit list contains :")

def get_fruit_load_list():
      with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * from fruit_load_list")      
         return my_cur.fetchall();
      
def insert_row(new_fruit):
      with my_cnx.cursor() as my_cur:
            my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")      
            return "Thanks for adding " + new_fruit
            
      
if streamlit.button('Get Fruit Load List'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows = get_fruit_load_list()
      streamlit.dataframe(my_data_rows)
      my_cnx.close()
            
add_my_fruit = add_fruit = streamlit.text_input('Which fruit to add ?')

if streamlit.button('Add Fruit to the List'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      streamlit.text(insert_row(add_my_fruit))
      my_cnx.close()
           
streamlit.stop()

                                

