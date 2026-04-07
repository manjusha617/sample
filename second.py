import streamlit as st
st.title("speed fine")
speed=st.number_input("enter the speed ravi travelled per hour:")
helmet=st.selectbox("enter is wearing helmet:(yes/no):")
documents=st.selectbox("enter is he carriying:(yes/no):")
if st.button("calculate bill"):
    total=0
if speed>80 and helmet=="no" and documents =="no":
    total=2500
else:
  total=0
  if helmet == "no":
     total+=500
  if documents=="no":
     total+=700
  if speed>80:
    total+=1000
if total>0:
  st.error("total fine:",total)
else:
  st.sucess("he didn't have to pay any fine.")
