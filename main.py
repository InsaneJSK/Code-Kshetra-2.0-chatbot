import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("groq_api_key")
client = Groq(api_key=groq_api_key)

system_prompt = "You are a helpful assistant who answers users based on given context and do not give any information not mentioned in it. If user's query cannot be answered using the context, you tell them that you don't know the answer to their query."
context = '''Chatbot Context for Geek Room Community
You are a helpful assistant for the Geek Room community, a vibrant group of over 25,000 students and professionals from across India. You assist with queries about Code Kshetra, Geek Room's annual hackathon series.

The upcoming Code Kshetra 2.0 Hackathon is a 36-hour coding marathon, scheduled for February 21-22, 2025, hosted at JIMS Sector-5 Rohini, near Rithala Metro Station. It’s where innovation meets creativity, offering participants the chance to showcase their ideas and build something amazing.
Code Kshetra 2.0 is an MLH-Approved Hackathon, part of the global Major League Hacking (MLH) platform. This recognition places it among the world’s leading hackathons, where innovation meets creativity. Participants will experience world-class mentorship, fair competition, and an environment that fosters cutting-edge ideas.
The hackathon has no participation cost.

Key Details About Code Kshetra 2.0:
Eligibility:
Open to all university students.
Teams with a confirmation email from Devfolio (containing a QR code) for the online round are eligible for the offline round.
Selection for the online round is based on GitHub, LinkedIn profiles, and hackathon experience.
If a participant's profile is under review, the selection process is ongoing. Stay tuned for updates.

Team Size: 1-4 members.

Venue Facilities:
Food: High-quality, safe meals will be provided multiple times throughout the hackathon to keep participants energized.
Rest and Bedding Arrangements: Comfortable bedding and rest areas will be available for participants to recharge.
Security: The event prioritizes participant safety, with no compromises on security measures.

Judging Criteria:
Focus on the novelty and impact of ideas.
Prototypes close to fully working projects will have an edge.
Fair evaluation—no special treatment for any participant.

Problem Statements:
Problem statements will be released soon. You'll be notified when that happens.
Projects using sponsor technologies are eligible for additional prizes.

Perks and Benefits:
Prize Pool: Over ₹1,00,00,000, including cash prizes worth ₹50,000.
Free swag, goodies, meals, and rest areas.
Networking with industry leaders, live project presentations, idea pitching sessions, guidance from expert judges and mentors, and fun activities.
Boost your LinkedIn profile with this prestigious hackathon.

Sponsors and Special Tracks:
Our sponsors include:
•	AiHello: Offering prizes worth $300.
•	Wolfram: Offering prizes worth $1,660.
•	Balamsiq: Offering prizes worth $1,200.
•	InterviewBuddy™: Offering prizes worth $6,600.
•	Code Crafters: Offering prizes worth $1,080.
Additionally, we have several special tracks sponsored by leading organizations:
Polygon Track:
•	Sponsor: Polygon
•	Prize: $200 for the best hack built on Polygon.
•	For more information: https://nsb.dev/polygon-bounty
ETHIndia Track:
•	Sponsor: ETHIndia
•	Prize: $100 for the best hack using Ethereum.
Aptos Track:
•	Sponsor: Aptos
•	Prize: $250 for the most unique/best app built on Aptos using the Move programming language.
•	For more information: https://elegant-thumb-725.notion.site/Devfolio-x-Aptos-Hacker-Resources-f250cbb1debe4a629d02a60346703186

Contact for More Details:
LinkedIn: https://www.linkedin.com/company/geekroom-jims/
Instagram: https://www.instagram.com/geekroom_jims/
Devfolio: https://code-kshetra-2.devfolio.co/
Website: https://codekshetra2.geekroom.in/
'''

# Define a function to get completion from the Groq API
def get_completion(user_question):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": f"""You have been given a CONTEXT regarding Geek Room community's Code Kshetra 2.0 hackathon along with a USER QUERY about it. You are to answer the query with the information provided in this context. Do not refer the query or the fact that you were provided a context again. Don't mention the context, instead treat it as your knowledge. If the query cannot be answered using the context - respond back telling that the question can't be answered and tell them to contact the organization by giving them the links provided.
                                <CONTEXT START>
                                {context}
                                <CONTEXT END>

                                USER QUERY: '{user_question}'
"""
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

# Streamlit app layout
st.set_page_config(page_title="Code-क्षेत्र 2.0 By Geek Room 💖", layout="wide")

st.title("Code-क्षेत्र 2.0 Nova By Geek Room 💖")

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