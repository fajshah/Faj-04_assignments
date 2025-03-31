import streamlit as st
import requests

# API URL
API_URL = "https://restcountries.com/v3.1/name/"

# Streamlit App UI
st.set_page_config(page_title="🌍 Country Info Cards", layout="centered")

st.title("🌍 Country Information Cards")
st.write("🔍 کسی بھی ملک کی معلومات حاصل کریں!")

# User Input
country = st.text_input("ملک کا نام درج کریں:")

if st.button("🔍 Search"):
    if country:
        try:
            response = requests.get(API_URL + country)
            if response.status_code == 200:
                data = response.json()[0]

                # Extract Country Details
                name = data["name"]["common"]
                flag = data["flags"]["png"]
                capital = data.get("capital", ["N/A"])[0]
                region = data.get("region", "N/A")
                subregion = data.get("subregion", "N/A")
                population = data.get("population", "N/A")
                area = data.get("area", "N/A")
                currency = list(data["currencies"].keys())[0]
                language = ", ".join(data["languages"].values())

                # Display Country Card
                st.image(flag, width=150)
                st.markdown(f"## 📍 {name}")
                st.write(f"**🏛 دارالحکومت:** {capital}")
                st.write(f"**🌍 علاقہ:** {region} | **📌 ذیلی علاقہ:** {subregion}")
                st.write(f"**👥 آبادی:** {population:,}")
                st.write(f"**📏 رقبہ:** {area:,} km²")
                st.write(f"**💰 کرنسی:** {currency}")
                st.write(f"**🗣 زبانیں:** {language}")

            else:
                st.error("❌ ملک نہیں ملا! براہ کرم درست نام درج کریں۔")

        except Exception as e:
            st.error(f"⚠️ ایرر: {e}")

    else:
        st.warning("⚠️ براہ کرم ملک کا نام درج کریں!")
