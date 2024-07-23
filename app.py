import streamlit as st
import requests

st.set_page_config(
    page_title="Brain Wars",
    page_icon="icon.png",
    menu_items={
        "About":"Get ready for a Battle of the Brains with Brain Wars! Our trivia game features diverse categories such as Entertainment, Sports & Leisure, Language, and Art & Literature. Test your wits and see how you stack up in this ultimate trivia showdown. With questions ranging from General Knowledge to Religion & Mythology, it's time to show off your brainpower!"
    }   
)

st.write("<h2 style='color:#FFA500;font-size:33px;'>Test Your Wits in the Ultimate Trivia Showdown!</h2>",unsafe_allow_html=True)

category=st.selectbox("Select a Category",["Art & Literature","Language","Science & Nature","General","Food & Drink","People & Places","Geography","History & Holidays","Entertainment","Toys & Games","Music","Mathematics","Religion & Mythology","Sports & Leisure"])

btn=st.button("Generate")

category_map = {
    "Art & Literature": "artliterature",
    "Language": "language",
    "Science & Nature": "sciencenature",
    "General": "general",
    "Food & Drink": "fooddrink",
    "People & Places": "peopleplaces",
    "Geography": "geography",
    "History & Holidays": "historyholidays",
    "Entertainment": "entertainment",
    "Toys & Games": "toysgames",
    "Music": "music",
    "Mathematics": "mathematics",
    "Religion & Mythology": "religionmythology",
    "Sports & Leisure": "sportsleisure"
}

if btn:
    cat_gry=category_map[category]
    try:
        api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(cat_gry)
        response = requests.get(api_url, headers={'X-Api-Key': '2jWCY0dASiPZc7RLybXvXA==R9oC0XPKPWiGJ6k6'})
        if response.status_code == requests.codes.ok:
            data=response.json()[0]
            st.write(f"<h4 style=font-size:27px;color:lightgreen;>{data['question']}</h4>",unsafe_allow_html=True)
            with st.expander("Answer"):
                st.write(f"<h4 style=color:#7DF9FF;>{data['answer']}</h4>",unsafe_allow_html=True)
    except:
        st.error("Network Error")
