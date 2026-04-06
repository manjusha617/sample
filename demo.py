import streamlit as st

st.title("Chess Board Color Finder ♟️")

position = st.text_input("Enter position (like a1, b3):")

if position:
    column = position[0].lower()
    row = int(position[1])

    column_num = ord(column) - ord('a') + 1
    total = column_num + row

    if total % 2 == 0:
        st.write("Black ⬛")
    else:
        st.write("White ⬜")
