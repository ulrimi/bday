import streamlit as st
import time
import random

# Define the prize options
PRIZES = ["Dinner in NYC", "Free back massage", "Box of chocolates", "Cat toys", "Nothing, you lose"]

def animate_happy_birthday():
    """Animates a 'Happy Birthday!' message letter by letter and releases balloons."""
    placeholder = st.empty()
    message = "Happy Birthday!"
    displayed = ""
    for char in message:
        displayed += char
        placeholder.markdown(
            f"<h1 style='text-align: center; color: #FF69B4;'>{displayed}</h1>",
            unsafe_allow_html=True,
        )
        time.sleep(0.1)
    st.balloons()  # Celebrate with balloons!

def spin_wheel():
    """Simulates a spinning prize wheel with a deceleration effect over ~5 seconds."""
    spin_placeholder = st.empty()
    spin_duration = 5  # Total spin time in seconds
    delay = 0.1         # Initial delay between updates
    elapsed = 0

    # Spin with gradual slowdown
    while elapsed < spin_duration:
        current_prize = random.choice(PRIZES)
        spin_placeholder.markdown(
            f"<h2 style='text-align: center;'>Spinning... <span style='color: #1E90FF;'>{current_prize}</span></h2>",
            unsafe_allow_html=True,
        )
        time.sleep(delay)
        elapsed += delay
        delay = min(delay + 0.05, 0.5)  # Increase delay to simulate deceleration

    # Final prize selection
    final_prize = random.choice(PRIZES)
    spin_placeholder.markdown(
        f"<h2 style='text-align: center;'>Result: <span style='color: #32CD32;'>{final_prize}</span></h2>",
        unsafe_allow_html=True,
    )
    return final_prize

def main():
    st.set_page_config(page_title="Birthday Prize Wheel", layout="centered")

    # Animate "Happy Birthday!" on first load only
    if "birthday_animated" not in st.session_state:
        animate_happy_birthday()
        st.session_state["birthday_animated"] = True

    # Initialize spin button state if not already set
    if "spin_disabled" not in st.session_state:
        st.session_state["spin_disabled"] = False

    st.markdown("<hr>", unsafe_allow_html=True)

    # Button to trigger the prize wheel spin; disabled if already clicked
    st.warning("Disclaimer: You may be liable for accepting a gift as specified by the spin result.  Spin at your own risk!")
    if st.button("Spin the Wheel!", disabled=st.session_state["spin_disabled"]):
        st.session_state["spin_disabled"] = False  # disable button immediately after click
        result = spin_wheel()
        if result.lower() == "nothing, you lose":
            st.warning("Oh no! You lose. Since it's a special occasion, we'll allow another spin. Try again!")
            st.session_state["spin_disabled"] = True  # re-enable button for another try
        else:
            st.success(f"Congratulations! You won: {result}")

if __name__ == '__main__':
    main()
