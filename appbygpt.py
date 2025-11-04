import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
st.set_page_config(page_title="EdTech Simulation", page_icon="🎓", layout="centered")





# --- Initialize session state ---
if "coins" not in st.session_state:
    st.session_state.coins = 0
    st.session_state.level = 1
    st.session_state.modules = 0
    st.session_state.notes = ""

# --- Header ---
st.title("🎓 EdTech Learning Simulator")
st.write("Welcome to your personalized AI Learning Platform!")

# --- Name Input ---
name = st.text_input("Enter your name:", placeholder="Student Name")

if name:
    st.success(f"Welcome, {name}! Let's start learning 🚀")

    # --- Sidebar Menu ---
    menu = st.sidebar.radio(
        "Select an Option:",
        [
            "Time Table",
            "Teacher",
            "Student",
            "Exit",
        ],
    )
    if menu == "Time Table":
        st.title(f"This is {name}'s time table")
        st.image('timetable.jpg')
    if menu == "Student":
        topic = st.selectbox("Select Topic:",['Complete Modules','VR Lab','Mentor Bot','Micro Learning','Notes Canvas','Smart Tech Reader','Concept Chain','Growth Dashboard','Attendence'])
        if topic == "Complete Modules":
            if st.button("Complete Modules"):
                st.session_state.modules += 1
                st.session_state.coins += 10
                st.success(f"🎉 {name} completed a module!")
                st.info(
                    f"Modules: {st.session_state.modules} | Coins: {st.session_state.coins} | Level: {st.session_state.level}"
            )

                if st.session_state.coins % 50 == 0:
                    st.session_state.level += 1
                    st.balloons()
                    st.success(f"🌟 Congratulations! You’ve reached Level {st.session_state.level}!")

    # 2️⃣ VR Lab
        elif topic == "VR Lab":
                subject = st.selectbox("Select Subject:", ["Physics", "Chemistry"])
                if subject == "Physics":
                    topic = st.selectbox("Select Topic:", ["Kinematics", "Rotation", "Waves"])
                    if st.button("Explore"):
                        if topic == "Kinematics":
                            st.write("📘 Explaining motion in 1D and 2D...")
                        elif topic == "Rotation":
                            st.write("📘 Explaining UCM and VCM...")
                        elif topic == "Waves":
                            st.write("📘 Explaining wave motion...")
                elif subject == "Chemistry":
                    topic = st.selectbox("Select Topic:", ["Kinetics", "Equilibrium", "Mole Concept"])
                    if st.button("Explore"):
                        if topic == "Kinetics":
                            st.write("🧪 Explaining first and second order kinetics...")
                        elif topic == "Equilibrium":
                            st.write("🧪 Explaining chemical equilibrium and alpha calculation...")
                        elif topic == "Mole Concept":
                            st.write("🧪 Explaining mole theory and limiting reagents...")

    # 3️⃣ Mentor Bot
        elif topic == "Mentor Bot":
                question = st.selectbox(
                    "Ask a Question:",
                    ["Gravity", "Atom", "Photosynthesis"],
        )
                if st.button("Ask"):
                    if question == "Gravity":
                        st.write("🌍 Gravity is the force of attraction between objects with mass (9.8 m/s² on Earth).")
                    elif question == "Atom":
                        st.write("⚛️ An atom is the smallest unit of matter, with a nucleus and orbiting electrons.")
                    elif question == "Photosynthesis":
                        st.write("🌿 Photosynthesis converts sunlight, CO₂, and water into glucose and oxygen.")

            # 4️⃣ Micro Learning
        elif topic == "Micro Learning":
                topic = st.text_input("Enter topic for quick 2-minute lesson:")
                if st.button("Start Lesson"):
                    st.write(f"🎥 Playing micro-lesson on **{topic}**")
                    st.progress(25)
                    st.write("1️⃣ Introduction")
                    st.progress(50)
                    st.write("2️⃣ Core Concepts")
                    st.progress(75)
                    st.write("3️⃣ Question Practice")
                    st.progress(100)
                    st.success("Lesson Completed ✅")

    # 5️⃣ Notes Canvas
        elif topic == "Notes Canvas":
                new_note = st.text_area("Write your notes below:")
                if st.button("Save Note"):
                    st.session_state.notes += "\n" + new_note
                    st.success("🗒️ Note saved successfully!")
                if st.session_state.notes.strip():
                    st.write("### Saved Notes:")
                    st.info(st.session_state.notes)

    # 6️⃣ Smart Text Reader
        elif topic == "Smart Text Reader":
                text = st.text_area("Enter text to read:")
                if st.button("Read Text"):
                    st.write("🗣️", text)

    # 7️⃣ Concept Chain
        elif topic == "Concept Chain":
                topic = st.selectbox("Select Topic:", ["Photosynthesis", "Programming"])
                if topic == "Photosynthesis":
                    st.write("🌱 Photosynthesis → Light Reaction → ATP Production")
                elif topic == "Programming":
                    st.write("💻 Problem Analysis → Algorithm → Coding → Debugging → Documentation")

    # 8️⃣ Growth Dashboard
        elif topic == "Growth Dashboard":
                creativity, curiosity, consistency = 80, 75, 90
                st.header(f"Personal Growth of {name}")
                st.metric("Creativity", f"{creativity}%")
                st.metric("Curiosity", f"{curiosity}%")
                st.metric("Consistency", f"{consistency}%")
                st.progress((creativity + curiosity + consistency) // 3 / 100)

        elif topic == "Attendence":
                attendence = 79
                st.header(f"Attencence of {name}")
                st.metric("Attendence ", f"{attendence}")
                st.progress((attendence)/100)    


    # 9️⃣ Exit
    elif menu == "🚪 Exit":
        st.warning("Thanks for using the EdTech Simulation! 👋")
else:
    st.info("👆 Please enter your name to start.")

