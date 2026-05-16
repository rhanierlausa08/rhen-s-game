import streamlit as st
st.write("WELCOME TO RHEN'S WEBSITE")
name = st.text_input("WHAT IS YOUR NAME?")
if name:
    st.write(f"### NICE TO MEET YOU! {name.upper()}")
st.write("LETS PLAY A GAME!") 
user_answer = st.radio("DO YOU WANT TO PLAY?", ["SELECT AN OPTION", "YES", "NO" ])
if user_answer == "YES":
    st.write("GREAT! LETS PLAY!")
else: st.write("OKAY, MAYBE NEXT TIME!")
favorite_color = st.text_input("WHAT IS MY FAVORITE COLOR? ")
if favorite_color.lower() == "blue":
    st.write("CORRECT! BLUE IS MY FAVORITE COLOR!")
else: 
    st.write("WRONG!")
user_answer = st.radio("DO YOU WANT TO CONTINUE?", ["SELECT AN OPTION", "YES", "NO"])
if user_answer == "YES":
    st.write("GREAT! LET'S CONTINUE!\n")
else:
     st.write("OK, maybe next time!")
favorite_food = st.text_input("WHAT IS MY FAVORITE FOOD? ")
if favorite_food.lower() == "adobo":
    st.write("CORRECT! MAY KISS KA SAKIN")
else: st.write("SAYOP BOANG BOANG")

