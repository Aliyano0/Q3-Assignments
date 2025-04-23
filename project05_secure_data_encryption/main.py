import os
import json
import time
import streamlit as st
import hashlib
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac

# Generate a key (this should be stored securely in production)
SAVE_FILE = "./data.json"
SALT = b"secure_salt_value"

if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0
# Navigation
if 'selection' not in st.session_state:
    st.session_state['selection'] = 0

########### HELPER FUNCTIONS ################
def load_data():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as file:
            return json.load(file)
    return {}

stored_data = load_data()

def save_data(data):
    with open(SAVE_FILE, "w") as file:
        json.dump(data, file, indent=4)
    return "Data saved successfully!"

### 10 sec sleep timer for exceeded failed attempts limit ###
def ten_second_timer():
    placeholder = st.empty()
    for i in range(10, 0, -1):
        placeholder.markdown(f"⏳ Time remaining: **{i}** seconds")
        time.sleep(1)
    placeholder.markdown("**Redirecting to login page...**")


###   Function to hash passkey   ###
def generate_key(passkey):
    # Derive a key using PBKDF2
    key = pbkdf2_hmac('sha256', passkey.encode(), SALT, 100000)
    return urlsafe_b64encode(key)

def hash_passkey(password):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), SALT, 100000).hex()

def encrypt_data(text, key):
    cipher = Fernet(generate_key(key))
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, key):
    hashed_passkey = hash_passkey(key)
    hashed_passkey = str(hashed_passkey)

    for item in stored_data[st.session_state["login_username"]]["data"]:
        if item["passkey"] == hashed_passkey and item["encrypted_text"] == encrypted_text:
            print(hashed_passkey)
            cipher = Fernet(generate_key(key))
            st.session_state.failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()
   
    st.session_state.failed_attempts +=  1    
    return None
            
    


###  Callback Function for navigation on button.  ###
def onclick(selection_input):
    if selection_input == "Home":
        st.session_state['selection'] = 0
    if selection_input == "Store Data":
        st.session_state['selection'] = 1
    if selection_input == "Retrieve Data":
        st.session_state['selection'] = 2
    if selection_input == "Login":
        st.session_state['selection'] = 3
    if selection_input == "Sign Up":
        st.session_state['selection'] = 4
    



###   Streamlit UI   ###
st.title("🔒 Secure Data Encryption System")


menu = ["Home", "Store Data", "Retrieve Data", "Login", "Sign Up"]
choice = st.sidebar.selectbox("Navigation", menu, index=st.session_state['selection'])




### PAGES ###

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")

    if "login_username" in st.session_state:
        st.subheader(f"🤖 Welcome {st.session_state.login_username}!")
        cols = st.columns([0.2,0.8])
        with cols[0]:
            st.button("Store New Data", on_click=lambda: onclick("Store Data"), key="storebtn")     
        with cols[1]:
            st.button("Retrieve Your Data", on_click=lambda: onclick("Retrieve Data"), key="retrievepbtn")     
    else:
        cols = st.columns([0.11,0.89])
    # Arg attribute wasn't working so I have implemented JavaScript type callback logic.
        with cols[0]:
            st.button("Login", on_click=lambda: onclick("Login"), key="loginbtn")
        with cols[1]:    
            st.button("Sign-Up", on_click=lambda: onclick("Sign Up"), key="signupbtn")  
           
elif choice == "Sign Up":
    st.subheader("🖋 Register a New User.")

    username = st.text_input("Enter your username.")
    password = st.text_input("Enter your password.", type="password")
    if st.button("Register"):
        if password and username:
            if username in stored_data:
                st.warning("⚠ Username already exists.")
            else:
                stored_data[username] = {
                    "password": hash_passkey(password),
                    "data": []
                }
                save_data(stored_data)
                st.success("✅ User registered successfully!")
        else:
            st.error("Both fields are required.")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_username = st.text_input("Enter you username:")
    login_pass = st.text_input("Enter Master Password:", type="password")
    login_btn = st.button("Login")
    if login_username and login_pass:
        if login_btn:
            login_pass = hash_passkey(login_pass)

            if (login_username in stored_data) and (login_pass == stored_data[login_username]["password"]):
                st.session_state.login_username = login_username
                st.session_state.failed_attempts = 0
                st.success(f"✅ Reauthorized successfully! Welcome {login_username}!")
                time.sleep(1)
                st.session_state.selection = 0 
                st.rerun()
                st.button("Go to HomePage", on_click=lambda: onclick("Home"), key="homebtn")     



            elif login_username not in stored_data or login_pass != stored_data[login_username]["password"]:
                
                    
                st.error(f"❌ Incorrect password or username!")
            # elif failed_attempts > 3:
            #     st.rerun()
    # else:
    #     st.warning("Please enter both Username and Password.")

elif choice == "Store Data":
    if "login_username" in st.session_state:
        st.subheader("📂 Store Data Securely")
        user_data = st.text_area("Enter Data:")
        passkey = st.text_input("Enter Passkey:", type="password")

        if st.button("Encrypt & Save"):
            if user_data and passkey:
                hashed_passkey = hash_passkey(passkey)
                encrypted_text = encrypt_data(user_data, passkey)
                stored_data[st.session_state["login_username"]]["data"].append({"encrypted_text": encrypted_text, "passkey": hashed_passkey})
                save_data(stored_data)
                st.success("✅ Data stored securely!")
            else:
                st.error("⚠️ Both fields are required!")
    else:
        st.warning("Login first to store the data!")

elif choice == "Retrieve Data":
    if "login_username" in st.session_state:
        st.subheader("🔍 Retrieve Your Data")
        # encrypted_text = st.text_area("Enter Encrypted Data:")
        if stored_data[st.session_state["login_username"]]["data"]:
            for item in stored_data[st.session_state["login_username"]]["data"]:
                st.code(f"{item["encrypted_text"]}")
        else:
            st.warning("No encrypted data found!")

        encrypted_text = st.text_area("Enter Encrypted Data: ")
        passkey = st.text_input("Enter Passkey:", type="password")
        
        if st.button("Decrypt"):
            if encrypted_text and passkey:
                    decrypted_text = decrypt_data(encrypted_text, passkey)
                    if decrypted_text:
                        st.success(f"✅ Decrypted Data: {decrypted_text}")
                    else: 
                        st.session_state.failures = 3 - st.session_state.failed_attempts
                        st.error(f"❌ Incorrect passkey! Attempts remaining: {str(st.session_state.failures)}")     
                        
                    if  st.session_state.failed_attempts >= 3:
                        st.error("🔒 Too many failed attempts! Redirecting to Login Page after 60 sec cooldown!")
                        ten_second_timer()
                        # time.sleep(10)
                        del st.session_state["login_username"]
                        st.session_state.selection = 3 
                        st.rerun()
                            
                        
            else:
                st.error("⚠️ Both fields are required!")    

    else:
        st.warning("Login first to retreive the data!")


