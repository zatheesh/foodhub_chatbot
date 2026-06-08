import streamlit as st
import streamlit_authenticator as stauth

# User credentials
names = ["Satheesh", "Admin"]
usernames = ["satheesh", "admin"]

# Generate hashed passwords once
passwords = ["foodhub123", "admin123"]

#hashed_passwords = stauth.Hasher(passwords).generate()
hashed_passwords = stauth.Hasher.hash_list(passwords)

authenticator = stauth.Authenticate(
    {
        "usernames": {
            usernames[0]: {
                "name": names[0],
                "password": hashed_passwords[0]
            },
            usernames[1]: {
                "name": names[1],
                "password": hashed_passwords[1]
            }
        }
    },
    "foodhub_cookie",
    "foodhub_key",
    cookie_expiry_days=1
)

#name, authentication_status, username = authenticator.login(
    #"Login",
    #"main"
#)

name, authentication_status, username = authenticator.login(
    location="main"
)

if authentication_status:

    #authenticator.logout("Logout","sidebar")
    authenticator.logout(
    button_name="Logout",
    location="sidebar"
    )

    st.success(f"Welcome {name}")

    st.title("🍔 FoodHub Customer Support Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role":"assistant",
                "content":"Hi! I’m FoodHub Assistant."
            }
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input(
        "Example: Where is my order O12488?"
    )

    if user_input:

        st.session_state.messages.append(
            {"role":"user","content":user_input}
        )

        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("assistant"):
            with st.spinner(
                "Checking FoodHub records..."
            ):

                response = chatagent(user_input)

            st.write(response)

        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":response
            }
        )

elif authentication_status == False:
    st.error("Invalid username/password")

elif authentication_status == None:
    st.warning("Please login")
