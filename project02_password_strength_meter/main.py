import re
import streamlit as st
import math 
import random

st.set_page_config(page_title="🦾 Password Strength Meter", layout="wide")
st.title("🦾 Password Strength Meter")
st.subheader("🤔 How secure is your Password?")
st.write("💡 Tip: Try to make your passwords at least 15 characters long including an uppercase and a lowercase letter and a number and a special character.")

password: str = st.text_input("Enter your password", type="password")

button = st.button("Check Strength")

st.write(f"Your Password Length: {len(password)}")

def suggest_password():
    # String Setup
    pass_str: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789[!@#$%^&*]"
    str_length: int = len(pass_str)

    # Random Length for suggested password
    password_length: int = random.randint(15,24)

    suggested_password = ""

    # Iterating the random int from password lentgh.
    for i in range(password_length):

        # Getting random index in each iteration.
        random_index: int =  math.floor(random.random()*str_length)

        # Concatenating previous string and new character at the random index in each iteration.
        suggested_password += pass_str[random_index]
    
    st.info(f"🔑 Suggested Password: {suggested_password}")

def check_password_strength(password):
    score = 0
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        st.error("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.error("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        st.error("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.error("❌ Include at least one special character (!@#$%^&*).")

    # Above 15 characters
    if len(password)>= 15:
        score += 1


    # Common Passwords
    if password == "Password123$" or password == "Qwerty123@":
        st.error("❌ Your password is too common!")
    
    # Strength Rating
    if len(password) < 1:
        st.error("❌ Enter your password first!")
        suggest_password()
    elif score == 5:
        st.success("✅ Strong Password!")
    elif score == 3 or score == 4:
        st.warning("⚠️ Moderate Password - Suggested Password Length is 15 or more.")
        suggest_password()
    else:
        st.error("❌ Weak Password - Improve it using the suggestions above.")
        suggest_password()


# Get user input
if button:
    check_password_strength(password)