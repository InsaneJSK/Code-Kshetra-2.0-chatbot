import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("groq_api_key")
client = Groq(api_key=groq_api_key)

context = '''You're an helpful assistant of Geek Room community that has over 25000 students and professionals from PAN India and code-kshetra is an annual series of hackathons by geek room, the 1.0 version happened in feb 2023. This year we are hosting Code Kshetra 2.0 Hackathon
Where innovation meets creativity in a 36-hour coding challenge hosted by JIMS Sector-5 Rohini and Geek Room.

This hackathon is open for any student and working professional.

So, some you've to answer to user for the questions, user will ask based on the details provided below, keep crisp and answer in short:
- If someone got the confirmation mail from devfolio for online round with a QR code, then their team is eligible to participate in the offline round on February 21-22, 2025.
- The hackathon will be conducted at JIMS Sector-5 Rohini, near Rithala Metro Station
- Prize Pool: Over ₹1,00,00,000, including cash prizes worth ₹50,000.

- It'll be completely fair hackathon, nobody will be getting any advantage as all are the same for organizers
- Team size is 1-4
- It's mostly about the novelity and impact of the idea that will matter 
- It'll be better if the prototype will be close to a full working project
- Problem statements aren't released released yet and will be releasing very soon
- in addition to the main problem statements - if you utilize our sponsor's technologies in your project, you are eligible for a prize from them too if the project's good.
- In case, some profile is under review, it is still under going selection. Stay tuned as you will find out the result soon.
- Selection in online round will be based on github, linkedin profiles and experience in hackathons.
- Participants will be able to enjoy live project presentations, Idea pitching sessions, Guidance from expert judges and mentors, Fun activities, games, and great food
- Perks of attending: Free swag and goodies; Meals and a place to rest; Networking opportunities with industry leaders
- Boost for your LinkedIn profile

- For more details, you've to say please check Code Cubicle 3.0 Instagram, Linkedin: Links are here 

https://www.linkedin.com/company/geekr00m
https://www.instagram.com/_geek.room/
'''

# Define a function to get completion from the Groq API
def get_completion(user_question):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f'''{context}

 {user_question}''',
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

# Streamlit app layout
st.set_page_config(page_title="Code-क्षेत्र 2.0 By Geek Room 💖", layout="wide")

st.title("Code-क्षेत्र 2.0 Genie By Geek Room 💖")

# Display information about Geek Room and handle links
st.markdown("""
    **Geek Room** - A community dedicated to helping each other get better at coding. 
    Geek Room community has over 25,000 students and professionals from PAN India.
    
    All handles: [https://linktr.ee/geekroom](https://linktr.ee/geekroom)
""")

# Add a sidebar with previous hackathon details and links
st.sidebar.title("Previous Hackathons")

st.sidebar.markdown("""
    ### Code Cubicle 3.0
    🌟 Introducing Code Cubicle 3.0: Unlocking Collaboration & Innovation, One Cubicle at a Time!

    🚀 Join us for an unparalleled tech adventure at Code Cubicle 3.0, the ultimate hackathon brought to you by Geek Room and Mastercard. Dive into the heart of innovation and creativity as we redefine the essence of technology-driven solutions.
    
    ✨ Winners also get a chance to go to an AI-symposium hosted by Mastercard where they can meet top data scientists and pitch their idea to them!
    🗓️ Event Schedule:
    - 15th September 2024 (online round)
    - 21st September 2024 (offline round)
    - Venue for Offline Round: DLF Plaza Tower, DLF Phase 1, Sector 26A, Gurugram, Haryana 122002
    
    [Learn More](https://code-cubicle-3.devfolio.co/)
""")

st.sidebar.markdown("""
    ### Code Cubicle 2.0
    🌟 Introducing Code Cubicle 2.0: Unlocking Collaboration & Innovation, One Cubicle at a Time!
    
    🚀 Join us for an unparalleled tech adventure at Code Cubicle 2.0, the ultimate hackathon brought to you by Geek Room. Dive into the heart of innovation and creativity as we redefine the essence of technology-driven solutions.
    
    🗓️ **Event Schedule:**
    - Dates: 27th July 2024 (online round) & 3rd August 2024 (offline round)
    - Venue for Offline Round: Microsoft Corporation India Private Limited, DLF Cyber City, DLF Phase 3, Sector 24, Gurugram, Haryana, India
    
    [Learn More](https://code-cubicle-2.devfolio.co/)
""")

st.sidebar.markdown("""
    ### Code Cubicle 1.0
    🌟 Introducing Code Cubicle: Unlocking Collaboration & Innovation, One Cubicle at a Time!
    
    🚀 Join us for an unparalleled tech adventure at Code Cubicle, the ultimate hackathon brought to you by Geek Room. Dive into the heart of innovation and creativity as we redefine the essence of technology-driven solutions.
    
    🗓️ **Event Schedule:**
    - Dates: 15th (online round) & 19th May 2024 (offline round)
    - Venue for Offline Round: Eccosphere Coworking Pvt Ltd, B-70, Block B, Sector 67, Noida, Uttar Pradesh 201301
    
    [Learn More](https://code-cubicle.devfolio.co/)
""")

st.sidebar.markdown("""
    ### Code-क्षेत्र
    Welcome to Code-क्षेत्र, a thrilling 36-hour hackathon hosted at JIMS Rohini Sector-5, a prestigious institution known for its commitment to academic excellence and holistic development, in February 2024. More than just a competition, it's an immersive experience filled with innovation, exciting prizes, swags, and a lot of fun. It's your opportunity to connect with experienced mentors and judges.
    
    Organized by Geek Room, a vibrant community dedicated to enhancing coding skills, started as an open community for solving tech-related queries and participating in college competitions. In a short span, it has grown to include 6000+ participants from colleges across India. Now, launching chapters in different colleges, we're excited to have it at JIMS!
    
    [Learn More](https://code-kshetra.devfolio.co/)
""")

# Input for the user question
user_question = st.text_input("Ask your question:")

if st.button("Submit"):
    if user_question:
        with st.spinner("Thank you for supporting Geek Room..."):
            # Get completion from the Groq API
            response = get_completion(user_question)
            # Display the response
            st.markdown(f"**Response:** {response}")
    else:
        st.error("Please enter a question before submitting.")