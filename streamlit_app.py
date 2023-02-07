pip install streamlit-authenticator
import streamlit as st
import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
















# import streamlit
# import pandas
# import requests
# from urllib.error import URLError

# streamlit.title('My Parents New Healthy Diner')
# streamlit.header('Breakfast Menu')
# streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
# streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
# streamlit.text('🐔 Hard-Boiled Free-Range Egg')
# streamlit.text('🥑🍞 Avocado Toast')
# streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_fruit_list = my_fruit_list.set_index('Fruit')

# # Let's put a pick list here so they can pick the fruit they want to include 
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
# fruits_to_show = my_fruit_list.loc[fruits_selected] #pandas.dataFrame.loc[source] Access a group of rows and columns by label(s) or a boolean array.
# # Display the table on the page.
# streamlit.dataframe(fruits_to_show)



# #Create the repeatable code block (called a function)
# def get_fruityvice_data(this_fruit_choice):
#   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#   #take the json version of the response and normalize it
#   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#   return fruityvice_normalized
  
# #New Section to display fruityvice api response
# streamlit.header("Fruityvice Fruit Advice!")
# try:
#   fruit_choice = streamlit.text_input('What fruit would you like information about?')
#   if not fruit_choice:
#     streamlit.error("Please select a fruit to get information.")
#   else:
#     back_from_function=get_fruityvice_data(fruit_choice)
#     # output it the screen as table
#     streamlit.dataframe(back_from_function)
    
# except URLError as E:
#   streamlit.error()
  
# streamlit.write('The user entered ', fruit_choice)


# #don't run anything past here while troubleshoot
# # streamlit.stop()

# streamlit.header("View Our Fruit List - Add Your Favorites!")
# #Snowflake-related functions
# def get_fruit_load_list():
#   with my_cnx.cursor() as my_cur:
#     my_cur.execute("select * from fruit_load_list")
#     return my_cur.fetchall()

# #Add a button to load the fruit
# if streamlit.button('Get Fruit List'):
#   my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
#   my_data_rows = get_fruit_load_list()
#   my_cnx.close()
#   streamlit.dataframe(my_data_rows)

# # streamlit.stop() #to troubleshoot

# #Allow the end user to add a fruit to the list
# def insert_row_snowflake(new_fruit):
#   with my_cnx.cursor() as my_cur:
#     my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
#     return "Thanks for adding " + new_fruit

# add_my_fruit = streamlit.text_input('What fruit would you like to add?')
# if streamlit.button('Add a Fruit to the List'):
#   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#   back_from_function=insert_row_snowflake(add_my_fruit)
#   my_cnx.close()
#   streamlit.text(back_from_function)

