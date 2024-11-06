import streamlit as st
from send_email import send_email


st.header("Contact us")

with st.form(key="email_forms"):
    user_name = st.text_input("Name")
    user_subject = st.text_input("Subject")
    user_email = st.text_input("Email")
    option = st.selectbox(
        "Budget",
        ("less than $1000", "less than $2000", "Over $5000"),
    )
    raw_message = st.text_area("Your Message")

    message = f"""\
user_name : New user_name
subject : New email form {user_email}
    
from: {user_name}
{raw_message}

"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("message sent successfully")

