import streamlit as st
import requests

st.set_page_config(page_title="Travel Planner Assistant", page_icon="🧳")

st.title("🧳 Travel Planner Assistant")
st.markdown("Plan your next trip with the help of AI. Just type your travel request below:")

# Kullanıcıdan giriş al
user_query = st.text_area("✈️ Travel Request", 
                          "I'm planning a trip to Rome next weekend. Can you help me plan it?")

# Gönder butonu
if st.button("Generate Travel Plan"):
    if not user_query.strip():
        st.warning("Please enter a travel request.")
    else:
        with st.spinner("Planning your trip..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/plan-trip",
                    json={"query": user_query}
                )
                if response.status_code == 200:
                    result = response.json()
                    
                    st.success("Travel Plan Generated!")
                    st.subheader("📋 Travel Plan")
                    st.write(result.get("travel_plan", "No plan found."))

                    with st.expander("🏙️ City Information"):
                        st.write(result.get("city_info", {}))

                    with st.expander("🏨 Hotel Information"):
                        st.write(result.get("hotel_info", {}))

                    with st.expander("🌤️ Weather Forecast"):
                        st.write(result.get("weather_info", {}))

                    with st.expander("💱 Budget & Currency Info"):
                        st.write(result.get("budget_info", {}))

                    with st.expander("📅 Travel Date"):
                        st.write(result.get("travel_date", {}))

                else:
                    st.error(f"Error from server: {response.status_code}")
            except Exception as e:
                st.error(f"Request failed: {e}")
