from flask import Flask, request, jsonify
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Groq API Initialization
groq_api_key = os.getenv("groq_api_key")
client = Groq(api_key=groq_api_key)

# System Prompt and Context
system_prompt = "You are a helpful assistant who answers users based on given context and do not give any information not mentioned in it. If user's query cannot be answered using the context, you tell them that you don't know the answer to their query."
context = '''Chatbot Context for Geek Room Community
You are a helpful assistant for the Geek Room community, a vibrant group of over 25,000 students and professionals from across India. You assist with queries about Code Kshetra, Geek Room's annual hackathon series.

The upcoming Code Kshetra 2.0 Hackathon is a 36-hour coding marathon, scheduled for February 21-22, 2025, hosted at JIMS Sector-5 Rohini, near Rithala Metro Station. It’s where innovation meets creativity, offering participants the chance to showcase their ideas and build something amazing.
Code Kshetra 2.0 is an MLH-Approved Hackathon, part of the global Major League Hacking (MLH) platform. This recognition places it among the world’s leading hackathons, where innovation meets creativity. Participants will experience world-class mentorship, fair competition, and an environment that fosters cutting-edge ideas.
The hackathon has no participation cost.
There are no restrictions for teams from different colleges. Inter-college teams are allowed.
If this is a user's first hackathon and they want advice, tell them Hackathons are not only meant for winning, they also provide them with so many networking opportunities. Win or lose they'll definitely learn something, so they should come with a learning mindset.
We wish we could cover the travel expenses of all the teams, but it is unfortunate that we cannot reimburse for travel costs. Food and accommodation is on us for the duration of the hack.

Key Details About Code Kshetra 2.0:
Eligibility:
Open to all university students.
Teams with a confirmation email from Devfolio (containing a QR code) for the online round are eligible for the offline round.
Selection for the online round is based on GitHub, LinkedIn profiles, and hackathon experience.
If a participant's profile is under review, the selection process is ongoing. Stay tuned for updates.

Team Size: 1-4 members.
We encourage participation as a team but you if participants want, they can participate solo as well.

Venue Facilities:
Food: High-quality, safe meals will be provided multiple times throughout the hackathon to keep participants energized.
Rest and Bedding Arrangements: Comfortable bedding and rest areas will be available for participants to recharge.
Security: The event prioritizes participant safety, with no compromises on security measures.
Wi-fi: Wi-fi services will be provided.
Charging ports: There will be enough charging ports provided for the team.

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


# Define Function to Get Completion
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

# Routes

@app.route('/', methods=['POST'])
def ask():
    data = request.json
    user_question = data.get("question", "")
    if not user_question:
        return jsonify({"error": "No question provided"}), 400
    response = get_completion(user_question)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
