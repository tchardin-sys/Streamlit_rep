# app.py — "Terah Interview Bot" with pre-defined Q&A about me

import streamlit as st

# -----------------------------
# 🔧 Page config
# -----------------------------
st.set_page_config(
    page_title="🎤 Terah Interview Bot",
    page_icon="🎤",
    layout="centered",
)

# -----------------------------
# ✏️ Pre-defined Interview Q&A about Terah
# -----------------------------
PREDEFINED_QA = [
    {
        "id": "about-me",
        "label": "⭐ Tell me about yourself",
        "user_text": "Tell me about yourself.",
        "bot_text": (
            "Sure! I’m Terah Hardin — I have a Bachelor’s in Data Analytics and I’m "
            "currently earning my Master’s in Artificial Intelligence for Business at ASU.\n\n"
            "I’m very hands-on with Python, SQL, and analytics tools, and I love automating "
            "repetitive work. In a previous role, I automated over 97% of daily manual processes "
            "using VBA, SQL, and scripting. I’ve also built projects like a home-sale prediction "
            "model, a nutrition analytics project, and a loan-eligibility Streamlit app.\n\n"
            "Professionally, I enjoy roles that mix problem-solving, data strategy, and intelligent "
            "automation — like Data Analyst, AI Engineer, or Product Manager roles."
        ),
    },
    {
        "id": "walk-resume",
        "label": "📄 Walk me through your resume",
        "user_text": "Walk me through your resume.",
        "bot_text": (
            "Absolutely. I started with a Bachelor’s in Data Analytics, where I built a strong "
            "foundation in statistics, SQL, and data visualization. From there, I worked in roles "
            "where I focused heavily on automation and analytics — including a position where I "
            "automated 97% of manual daily tasks using VBA, SQL, and scripting.\n\n"
            "I also gained experience at EssilorLuxottica and in other analyst-style roles where I "
            "supported reporting, process improvements, and data-driven decision-making.\n\n"
            "Right now, I’m pursuing my Master’s in Artificial Intelligence for Business at ASU, "
            "focusing on machine learning, model deployment, and using AI to solve real business problems. "
            "Across all of that, the common theme is using data and automation to make work smarter and more efficient."
        ),
    },
    {
        "id": "strengths",
        "label": "💪 What are your strengths?",
        "user_text": "What are your strengths?",
        "bot_text": (
            "Some of my biggest strengths are:\n\n"
            "• **Automating complex processes** – I’ve automated 97% of manual tasks in a prior role.\n"
            "• **Breaking down messy problems** – I’m good at taking something confusing and organizing it "
            "into a clean system or workflow.\n"
            "• **Learning quickly** – especially technical skills like Python, ML, SQL, and tools.\n"
            "• **Making data usable** – I like turning raw data into dashboards, models, or apps that people "
            "can actually use.\n\n"
            "Overall, I’m a process-minded problem solver who cares a lot about clarity and efficiency."
        ),
    },
    {
        "id": "weaknesses",
        "label": "🧱 What are your weaknesses?",
        "user_text": "What are your weaknesses?",
        "bot_text": (
            "One of my weaknesses is that I can get very deep into details when I’m trying to improve a process "
            "or debug something. I like things to be clean and well-structured, which is great for quality, but "
            "sometimes it means I spend more time than necessary polishing.\n\n"
            "I’ve been working on this by setting clearer time limits, prioritizing impact, and asking myself, "
            "“Is this good enough to deliver and iterate on?” so I don’t over-perfect things before others can use them."
        ),
    },
    {
        "id": "project",
        "label": "📊 Tell me about a project you're proud of",
        "user_text": "Tell me about a project you're proud of.",
        "bot_text": (
            "A project I’m proud of is my Home-Sale Prediction Model.\n\n"
            "I created a housing dataset, cleaned it, engineered features like land size and pool presence, "
            "and trained a logistic regression model to predict whether a house would sell within 30 days. "
            "Then I built a Streamlit app where users can enter home features and see the probability of a quick sale.\n\n"
            "That project connected data cleaning, modeling, and deployment, and it reminded me how much I enjoy building "
            "end-to-end data products, not just running models in a notebook."
        ),
    },
    {
        "id": "problem-solving",
        "label": "🧩 Describe a time you solved a problem",
        "user_text": "Describe a time you solved a difficult problem.",
        "bot_text": (
            "One example was at Edward Jones. The team had a set of repetitive, manual daily processes that took a lot of time.\n\n"
            "I mapped out each step, identified where we could standardize, and built automations using VBA, SQL, and some scripting. "
            "In the end, we reduced manual work by about 97%, improved consistency, and freed up time for more important tasks.\n\n"
            "It was a good example of how I like to think: understand the system, design a cleaner version, then automate it."
        ),
    },
    {
        "id": "future",
        "label": "🚀 Where do you see yourself in the future?",
        "user_text": "Where do you see yourself in the future?",
        "bot_text": (
            "In the next few years, I see myself in a role that blends AI, analytics, and product thinking — "
            "like AI Product Manager, data/analytics-focused Product Manager, or a Data Analyst / Engineer who specializes in automation.\n\n"
            "Long-term, I want to build intelligent tools that automate decision-making, improve workflows, and make complex processes "
            "easier for people. I’m really drawn to work that sits at the intersection of business, systems, and AI."
        ),
    },
    {
        "id": "hire-me",
        "label": "🌟 Why should we hire you?",
        "user_text": "Why should we hire you?",
        "bot_text": (
            "You should hire me because I bring both technical skills and systems thinking.\n\n"
            "I can write SQL and Python, build models, and create dashboards — but I also think about how the whole workflow fits together. "
            "I look for ways to automate repetitive work, reduce friction, and make data easier for people to use.\n\n"
            "I learn quickly, I’m comfortable diving into new tools or codebases, and I care a lot about building solutions that actually "
            "help teams work better, not just look good on paper."
        ),
    },
    {
        "id": "culture",
        "label": "🤝 What kind of work environment do you like?",
        "user_text": "What kind of work environment do you like?",
        "bot_text": (
            "I do best in an environment that’s collaborative but also gives me focused time to think and build.\n\n"
            "I like teams where people share knowledge, ask questions freely, and are comfortable saying “I don’t know yet, "
            "but I’ll figure it out.” Clear priorities, honest communication, and room to experiment and improve things really matter to me.\n\n"
            "I’m also very motivated by environments that value learning and are open to using automation and AI to work smarter."
        ),
    },
]

# -----------------------------
# 💾 Initialize session state
# -----------------------------
if "chat_history" not in st.session_state:
    # Each message: {"role": "user" | "bot", "text": "..."}
    st.session_state.chat_history = []

# -----------------------------
# 🎨 Header
# -----------------------------
st.markdown(
    """
    <h1 style="text-align:center;">🎤 Terah Interview Bot</h1>
    <p style="text-align:center; font-size:0.95rem;">
        This chatbot answers common interview questions <b>about me</b> using pre-written responses.<br>
        Click a question below to see how I might answer it in an interview.
    </p>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# 🔘 Question buttons
# -----------------------------
st.subheader("Interview questions")

cols = st.columns(2)
for i, item in enumerate(PREDEFINED_QA):
    col = cols[i % 2]
    with col:
        if st.button(item["label"], use_container_width=True):
            # Add “user” (interviewer) question
            st.session_state.chat_history.append(
                {"role": "user", "text": item["user_text"]}
            )
            # Add “bot” (you) answer
            st.session_state.chat_history.append(
                {"role": "bot", "text": item["bot_text"]}
            )

# -----------------------------
# 💬 Chat display
# -----------------------------
st.subheader("Conversation")

if not st.session_state.chat_history:
    st.info("No questions asked yet. Click one of the buttons above to start the interview.")
else:
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.markdown(msg["text"])
        else:
            with st.chat_message("assistant"):
                st.markdown(msg["text"])

# -----------------------------
# 🧹 Clear conversation
# -----------------------------
if st.button("🧹 Clear conversation"):
    st.session_state.chat_history = []
    st.rerun()
