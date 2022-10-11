#----------------------------------------------------------------------------------------------------------------------------
# Imports
import streamlit as st
import random
import string
from PIL import Image
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Title and Logo
title_container = st.beta_container()
col1, col2 = st.beta_columns([1, 5])
image = Image.open('assets/logo.JPG')
with title_container:
    with col1:
       st.image(image)
    with col2:
        st.title('Password Generator')
        st.markdown("""
Create strong Passwords to protect your accounts

""")
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# User Input
st.write('')
col1, col2 = st.beta_columns([1,1])

pass_len = col1.number_input('Select your password length', min_value=4, max_value=128, value=8)
col2.empty()

cb_lower = st.checkbox('Include Lowercase Characters (eg. abcdef)', value=True)
cb_upper = st.checkbox('Include Uppercase Characters (eg. ABCDEF)', value=True)
cb_digit = st.checkbox('Include Digits (eg. 12345)', value=True)
cb_special = st.checkbox('Include Special Characters (eg. !@#$%)', value=True)
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Body
chars = ''

if cb_lower:
    chars += string.ascii_lowercase

if cb_upper:
    chars += string.ascii_uppercase

if cb_digit:
    chars += string.digits

if cb_special:
    chars += string.punctuation
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Main Function
def generate_password(len):
    password = ''
    for pwd in range(len):
        password += random.choice(chars)
    return password

col1, col2, col3, col4 = st.beta_columns([1,1,5,5])

btn_gen = col1.button('Generate')

pass_gen = ''
flag = 0

if not chars:
    st.error('Please Select atleast one option')
else:
    if btn_gen:
        pass_gen = generate_password(pass_len)
        flag = 1
        
st.write('')
st.text_area('Generated password:',value=pass_gen)
if flag==1:
    st.success('Password Generated')
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Links
st.write('')
st.markdown(f"To check if your password is safe from hackers and data breaches visit this <a href='https://sajinshivdas-passwordchecker-password-checker-webapp-ywv0rj.streamlitapp.com/'>Password Checker</a>.", unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------
# Footer
footer="""<style>
#MainMenu {visibility: hidden;}

a:link , a:visited{
color: black;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Made in Streamlit by <a href='https://sajinshivdas.com/cybersecurity/infosec-tools-and-utilities/'>Sajin Shivdas</a>.

</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------------------------------------



#############################################################################################################################
#############################################################################################################################
