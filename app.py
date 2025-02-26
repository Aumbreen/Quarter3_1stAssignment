import streamlit as st

# Page Configuration
st.set_page_config(page_title="Embracing Challenges in Programming", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
        html {
            scroll-behavior: smooth;
        }
        .learn-more-btn {
            background-color: #007bff;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 18px;
            transition: background-color 0.3s, transform 0.2s;
            display: inline-block;
            text-decoration: none;
            text-align: center;
            font-weight: bold;
        }
        .learn-more-btn:hover {
            background-color: #0056b3;
            transform: scale(1.05);
        }
        .highlight {
            color: #ff5722;
            font-weight: bold;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .thank-you {
            font-size: 24px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            margin-top: 20px;
            animation: fadeIn 2s ease-in-out;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🚀 Embracing Challenges in Programming")

# First Assignment Session Details
st.subheader("📝 First Assignment Session - Quarter 3")
st.markdown("<p class='highlight'>📅 <b>Date & Time:</b> Friday, 9 AM to 12 PM</p>", unsafe_allow_html=True)

# Introduction
st.subheader("🔍 Why Challenges Matter")
st.markdown("""
<p>Programming is a continuous journey of learning and overcoming obstacles. Challenges in coding help you:</p>
<ul>
<li>✅ Develop <span class='highlight'>problem-solving skills</span></li>
<li>✅ Improve <span class='highlight'>logical thinking</span></li>
<li>✅ Enhance adaptability to <span class='highlight'>new technologies</span></li>
<li>✅ Build resilience against <span class='highlight'>frustration</span></li>
</ul>
""", unsafe_allow_html=True)

# Video on Mindset Challenges (Updated with Custom Size)
st.subheader("🎥 Watch: How to Overcome Challenges in Programming")
st.markdown("""
    <iframe width="700" height="400" 
    src="https://www.youtube.com/embed/JjSIm52-nV0" 
    frameborder="0" allowfullscreen></iframe>
""", unsafe_allow_html=True)

# Strategies to Accept Challenges
st.subheader("💡 Strategies to Develop a Growth Mindset")
st.markdown("""
<ul>
<li>⭐ <b>Embrace Errors:</b> Bugs and mistakes are opportunities to learn.</li>
<li>⭐ <b>Break Problems Down:</b> Large tasks are easier when divided into smaller steps.</li>
<li>⭐ <b>Stay Curious:</b> Always explore new programming languages and frameworks.</li>
<li>⭐ <b>Seek Help:</b> Collaborate with the community, mentors, and peers.</li>
<li>⭐ <b>Be Patient:</b> Mastery takes time, so persist through the difficulties.</li>
</ul>
""", unsafe_allow_html=True)

# Preparing Your Mind for New Programming Languages
st.subheader("🧠 Preparing Your Mind to Accept Challenges in New Technologies")
st.markdown("""
<ul>
<li>🔹 <b>Adaptability:</b> Be open to new syntax and paradigms, as every language has its unique structure.</li>
<li>🔹 <b>Hands-on Practice:</b> Implement small projects to reinforce learning.</li>
<li>🔹 <b>Compare & Contrast:</b> Relate concepts from JavaScript/TypeScript to Python to understand differences effectively.</li>
<li>🔹 <b>Accept the Learning Curve:</b> Mastery takes time; don't rush the process.</li>
<li>🔹 <b>Stay Motivated:</b> Remember why you started and celebrate small wins.</li>
</ul>
""", unsafe_allow_html=True)

# Learn More Button (Scroll to Technologies Section)
st.markdown('<a href="#technologies" class="learn-more-btn">Learn More →</a>', unsafe_allow_html=True)

# Divider
st.markdown("---")

# Technologies & Learning Journey Section
st.markdown('<div id="technologies"></div>', unsafe_allow_html=True)
st.header("🛠 Technologies & Learning Journey")
st.markdown("""
<h4>🔹 <span class='highlight'>Technologies:</span></h4>
<ul>
<li>✔ <b>TypeScript, JavaScript</b></li>
<li>✔ <b>Next.js, Tailwind CSS</b></li>
<li>✔ <b>Python (Currently Learning)</b></li>
</ul>

<h4>🔹 <span class='highlight'>Self-Learning & Practice:</span></h4>
<ul>
<li>✅ The more you <b>practice</b>, the better you become.</li>
<li>✅ Work on projects, fix bugs, and <b>improve problem-solving skills</b>.</li>
<li>✅ Learning never stops – keep exploring <b>new frameworks & technologies</b>.</li>
</ul>

<h4>🔹 <span class='highlight'>Becoming a Good Programmer:</span></h4>
<ul>
<li>💡 <b>Consistency is key</b> – Code daily and challenge yourself.</li>
<li>💡 <b>Learn from mistakes</b> – Debugging helps you grow.</li>
<li>💡 <b>Stay updated</b> – Follow trends in the coding world.</li>
</ul>
""", unsafe_allow_html=True)

# Divider
st.markdown("---")

# Footer
st.markdown("🔗 **Keep Learning & Keep Growing!** | 🚀 **Develop with Passion!**")

# Balloons effect
st.balloons()

# Thank You Message Animation
st.markdown('<p class="thank-you">🎉 Thank You for Watching! 🎉</p>', unsafe_allow_html=True)

# Project Formation Information
st.markdown("<p class='highlight'>📌 This project is formed by Ambreen using AI technology.</p>", unsafe_allow_html=True)
