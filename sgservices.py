import streamlit as st
from PIL import Image
import time

# Load the uploaded image
logo_path = "SATHESH GOUD.jpg"
main = "SATHESH GOUD.jpg"
logo = Image.open(logo_path)

# Page Configuration
st.set_page_config(
    page_title="SG Services",
    page_icon=logo,
    layout="centered",
)

# App Title and Banner
st.markdown("""
        <style>
        .container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            height: 100vh;
        }
        .banner {
            font-size: 2.8em;
            font-weight: bold;
            text-align: center;
            color: #FF6F61;
            margin-bottom: 10px;
        }
        .tagline {
            font-size: 1.5em;
            text-align: center;
            color: #555;
            margin-top: -15px;
        }
        .subtext {
            font-size: 1.2em;
            text-align: center;
            color: #777;
            margin-bottom: 25px;
        }
        .congrats-box {
            background-color: #F9F9F9;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .button-center {
            margin-top: 20px;
        }
    </style>
    <div class="banner"> !!! Congratulations !!!<br> SATHESH GOUD SERVICES PRIVATE LIMITED!</div>
    <div class="tagline">POWERING PROGRESS TOGETHER</div>
    <div class="subtext">We're thrilled to release the new website, "SG Services."</div>
""", unsafe_allow_html=True)

# Display the logo
st.image(main, use_container_width = True)

# Company Info Section
st.markdown("""
<div class="congrats-box">
    <h3 style="text-align: center;">SG SERVICES PVT. LTD.</h3>
    <p style="text-align: center; font-size: 1.1em;">
        MD & CEO : <b> MR.Sathesh Goud</b> 
    </p>
</div>
""", unsafe_allow_html=True)

# High-Level Content
st.write("""
### A New Chapter of Innovation and Excellence
This is a defining moment for **Sathesh Goud Services Pvt. Ltd.** as we launch the website that symbolizes growth, innovation, and success. Congratulations to the team for their hard work and dedication.

It's time to take **SG SERVICES** live and let the world see the fruits of your efforts.
""")

# Release Button
st.markdown('<div class="button-center">', unsafe_allow_html=True)
if st.button("🚀 Go Live with SG Service"):
    st.balloons()
    st.markdown("[Click here to open SG Service](https://sgservices.in/)", unsafe_allow_html=True)
    st.success("Website successfully launched! 🌟")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<hr style="border: 1px solid #ddd; margin-top: 30px;">
<p style="text-align: center; font-size: 0.9em; color: #888;">
    Built with ❤️ to celebrate this incredible milestone. Here's to many more successes!
</p>
""", unsafe_allow_html=True)
