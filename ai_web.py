import streamlit as st

# Configure the page title and an awesome browser tab icon
st.set_page_config(page_title="Rhen's Website", page_icon="🕹️")

st.write("# 🚀 WELCOME TO RHEN'S WEBSITE")
st.write("---")

name = st.text_input("📝 WHAT IS YOUR NAME?")

if name:
    # A beautiful, clean container for the greeting
    with st.container(border=True):
        st.write(f"### ✨ NICE TO MEET YOU, {name.upper()}! ✨")
        st.write("Let's see how well you know me.") 
    
    st.write("") # Adds clean vertical spacing
    
    # Using columns for the first choice
    c1, c2 = st.columns([2, 1])
    with c1:
        user_answer = st.radio("🕹️ DO YOU WANT TO PLAY A GAME?", ["SELECT AN OPTION", "YES", "NO"])
    
    if user_answer == "YES":
        st.write("---")
        
        # Wrapping the game inside a bordered card
        with st.container(border=True):
            st.write("## 🎨 LEVEL 1: COLORS")
            favorite_color = st.text_input("WHAT IS MY FAVORITE COLOR? ", key="color_input")
            
            if favorite_color:
                if favorite_color.lower() == "blue":
                    st.write("🟩 **CORRECT! BLUE IS MY FAVORITE COLOR!**")
                    
                    st.write("")
                    continue_answer = st.radio("➡️ DO YOU WANT TO CONTINUE?", ["SELECT AN OPTION", "YES", "NO"], key="continue_input")
                    
                    if continue_answer == "YES":
                        st.write("---")
                        
                        with st.container(border=True):
                            st.write("## 🍲 LEVEL 2: FOOD")
                            favorite_food = st.text_input("WHAT IS MY FAVORITE FOOD? ", key="food_input")
                            
                            if favorite_food:
                                if favorite_food.lower() == "adobo":
                                    st.balloons() # Floating animation!
                                    st.write("🥰 **CORRECT! MAY KISS KA SAKIN!**")
                                else: 
                                    st.write("🟥 **SAYOP BOANG BOANG!** 😜")
                                    
                    elif continue_answer == "NO":
                        st.write("*OK, maybe next time! 👋*")
                else: 
                    st.write("🟥 **WRONG! TRY AGAIN!**")
                    
    elif user_answer == "NO":
        st.write("*OKAY, MAYBE NEXT TIME! 👋*")