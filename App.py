import streamlit as st
from datetime import datetime, timedelta
import json
import os
import random
import calendar
import urllib.parse

# Page Configuration - Clean & Dark Desi Aesthetic
st.set_page_config(page_title="Bande Ka Playbook", page_icon="🗿", layout="wide")

DATA_FILE = "cycle_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {
        "last_period_date": str(datetime.today().date()), 
        "cycle_length": 28,
        "devotion_points": 50,
        "city": "Bengaluru",
        "notes": "Favorite Coffee: Hazelnut Cold Coffee\nFavorite Chocolate: Dark Chocolate 70%\nShoe Size: 6\nFavorite Color: Black"
    }

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# Dark Desi Custom Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #0d090a;
        color: #f1faee;
    }
    .phase-card {
        background-color: #160b13;
        padding: 24px;
        border-radius: 16px;
        border: 2px solid #e63946;
        margin-bottom: 20px;
    }
    .action-box {
        background-color: #1a0f18;
        padding: 16px;
        border-radius: 10px;
        border-left: 4px solid #e63946;
        margin-bottom: 10px;
        font-size: 1rem;
    }
    .stButton>button {
        background-color: #e63946 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 10px 20px;
        width: 100%;
    }
    .excuse-box {
        background-color: #2b0e14;
        border: 1px dashed #ff4d6d;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
    }
    .concierge-card {
        background-color: #1f0f18;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #ff4d6d;
        margin-bottom: 15px;
    }
    .game-card {
        background-color: #180a13;
        padding: 20px;
        border-radius: 14px;
        border: 2px solid #2a9d8f;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Detailed Strategy Engine
def get_cycle_strategy(cycle_day, total_cycle):
    ovulation_day = total_cycle - 14

    if 1 <= cycle_day <= 5:
        return {
            "phase": "Periods / Sewa Mode 🩸",
            "title": "🩸 DAYS 1-5: Khatra Zone (Sewa & Care)",
            "color": "#e63946",
            "summary": "Mood swings 100%, Energy 0%. Dimaag bilkul mat chala, bass momos, chocolate aur hot water bag laa!",
            "actions": [
                "**Essential:** Hot water bag ready rakho aur uske favorite snacks/chocolate le aao.",
                "**The Vibe:** Low-key cozy home setup. Bilkul bahar ghumne ka pressure mat daalo.",
                "**Golden Rule:** Har baat pe bol: 'Haan tum bilkul sahi bol rahi ho'. Debate bilkul zero."
            ]
        }
    elif 6 <= cycle_day < ovulation_day - 3:
        return {
            "phase": "Flirt & Tease Mode 🌱",
            "title": "🌱 DAYS 6-10: Mausam Suhana (Rising Energy)",
            "color": "#2a9d8f",
            "summary": "Energy waapas aa rahi hai! Mood chill hai. Thoda romance aur hassi-mazaak pelo.",
            "actions": [
                "**Essential:** Choti-moti tareef kar do (Hair, Outfit) aur shaam ko chai/coffee date pe le jaao.",
                "**The Vibe:** Playful leg-pulling aur cute reels share karo.",
                "**Golden Rule:** Spontaneous raho, wo tumhari energy easily match karegi."
            ]
        }
    elif ovulation_day - 3 <= cycle_day <= ovulation_day + 2:
        return {
            "phase": "Ovulation Peak Window 🔥",
            "title": "🔥 OVULATION WINDOW: Full Hero Giri Zone",
            "color": "#ff4d6d",
            "summary": "PEAK OVULATION! Energy High, Confidence High, Attraction 200%. Is time full hero banna hai!",
            "actions": [
                "**Action 1 (Total Plan Ownership):** Date, location, aur food pe 100% control le lo. 'Tum batao kahan chalein' bol ke confused mat raho.",
                "**Action 2 (Grooming & Vibe):** Acche se ready ho ke milne jaao, solid perfume lagao, aur phones bilkul side me rakh do.",
                "**Action 3 (Deep Connection):** Intense eye contact, bold compliments, aur late-night drive pe 3 deep secrets share karo."
            ]
        }
    else:
        return {
            "phase": "Pamper & Reassurance Zone 🌙",
            "title": "🌙 DAYS 17-28: Careful Reassurance Zone",
            "color": "#f4a261",
            "summary": "Hormones shifting. Energy dip ho sakti hai, emotional support aur extra warmth do.",
            "actions": [
                "**Essential:** Apni oversized hoodie usko de do aur comfort food order kar do.",
                "**The Vibe:** Bina kisi wajah ke usko batao ki wo kitni cute hai.",
                "**Golden Rule:** Akele feel mat hone do, choti-moti frustration smile ke saath absorb kar lo."
            ]
        }

# Data lists
EXCUSES = [
    "“Baby sorry, mera dimaag 0% pe kaam kar raha tha kyunki tum paas nahi ho. Direct Zomato se pasand ka khana bhej raha hoon!” 🍕",
    "“Mera intention bilkul galat nahi tha jaan, mera network aur brain dono weak chal rahe hain aajj. Maaf kar do na?” 🥺",
    "“Galti ho gayi maharani ji. Saza ke taur pe aaj shaam ko tumhari favorite boba tea meri taraf se.” 🧋",
    "“Mera irada tumhein irritate karne ka nahi tha... tum gusse me bhi itni cute lagti ho ki dimaag kaam karna band kar deta hai!” 🍫"
]

SNACKS = [
    "🧋 Unannounced Boba / Cold Coffee drop-off at her place.",
    "🍫 Dark Chocolate (70%+) + Sweet handwritten note.",
    "🥟 Momos / Favorite street food evening delivery.",
    "🍦 Midnight Ice Cream run."
]

MOOD_DATABASE = {
    "🩸 Cramps & Low Energy (Sewa Mode)": {
        "food": "Hot Momos, Cheesy Pizza or Dal Khichdi + Dark Chocolate Brownie 🍫",
        "food_query": "Momos Pizza Brownie",
        "movie": "Yeh Jawaani Hai Deewani / 3 Idiots (Pure comfort feel-good comedies) 🍿",
        "movie_query": "Yeh Jawaani Hai Deewani movie",
        "ott": "Netflix / Prime Video"
    },
    "🌱 Chill & Cozy (Follicular Vibe)": {
        "food": "Cold Coffee, Peri Peri Fries & White Sauce Pasta 🍝",
        "food_query": "Cold Coffee Pasta Fries",
        "movie": "Modern Love / Brooklyn / Light Romantic Comedy ✨",
        "movie_query": "Modern Love series",
        "ott": "Netflix / Hotstar"
    },
    "🔥 High Energy / Date Night (Ovulation Mode)": {
        "food": "Sizzlers, Fine Dine Italian (Pasta/Tacos) or Sushi + Mocktails 🍷",
        "food_query": "Italian Sushi Sizzlers",
        "movie": "Interstellar / Gone Girl / Thriller or Date Night Romance 🎬",
        "movie_query": "Interstellar movie",
        "ott": "Netflix / Apple TV"
    },
    "🌙 Emotional / PMS Cushioning": {
        "food": "Extra Cheese Burger, Ice Cream tub & Her Favorite Milkshake 🍔",
        "food_query": "Burger Ice Cream Milkshake",
        "movie": "The Fault in Our Stars / Titanic / Comfort Animation (Disney/Pixar) 🧸",
        "movie_query": "The Fault in Our Stars movie",
        "ott": "Disney+ Hotstar / Netflix"
    }
}

TRUTHS = [
    "Pehli baar jab mujhe dekha tha, sach me kya laga tha?",
    "Meri sabse cute aur sabse irritating habit batao?",
    "Konsi ek aisi date hai jo tum dobara recreate karna chahogi?",
    "Koinse outfit me main sabse zyada achha lagta hoon?"
]

DARES = [
    "Mujhe direct 10 seconds tak eye-contact karke ek bold compliment do.",
    "Mere phone pe apni favorite selfie khich ke wallpaper set kar do.",
    "Mera favorite song 2 lines sing karke sunao.",
    "Aaj raat ke dinner ka location aur menu tum decide karo!"
]

# App Header With Custom Tagline
st.title("🗿 Bande Ka Playbook")
st.markdown("##### *\"Banda joru ka gulaam nahi, toh dur se salaam!\"* 😎🔥")
st.caption("Daily intelligence report + Live Food, Movie & Mood-Based Mini Games.")

stored = load_data()

# Settings Expander
with st.expander("⚙️ Bandi Ki Settings & City Set Karo", expanded=False):
    with st.form("settings_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            p_date = st.date_input("Last Period Start Date", value=datetime.strptime(stored["last_period_date"], "%Y-%m-%d").date())
        with col2:
            c_len = st.number_input("Cycle Length", min_value=20, max_value=45, value=stored.get("cycle_length", 28))
        with col3:
            city_val = st.text_input("Your City (e.g. Bengaluru, Mumbai)", value=stored.get("city", "Bengaluru"))
            
        if st.form_submit_button("Data Save Karo 🔒"):
            stored["last_period_date"] = str(p_date)
            stored["cycle_length"] = int(c_len)
            stored["city"] = city_val
            save_data(stored)
            st.success("Target set ho gaya bhai!")
            st.rerun()

# Date Math
start_dt = datetime.strptime(stored["last_period_date"], "%Y-%m-%d").date()
today = datetime.today().date()
cycle_len = stored.get("cycle_length", 28)
user_city = stored.get("city", "Bengaluru")

day_in_cycle = ((today - start_dt).days % cycle_len) + 1
strategy = get_cycle_strategy(day_in_cycle, cycle_len)
ovulation_target = start_dt + timedelta(days=cycle_len - 14)

# Top Metrics & Gamification Score
st.markdown("---")
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("Cycle Day", f"Day {day_in_cycle} / {cycle_len}")
with m2:
    st.metric("Aaj Ka Mode", strategy["phase"])
with m3:
    st.metric("Peak Ovulation Date", ovulation_target.strftime("%b %d"))
with m4:
    pts = stored.get("devotion_points", 50)
    st.metric("Devotion Points ⭐", f"{pts} Pts")

level = "Level 1: Novice Boyfriend 🐣" if pts < 50 else ("Level 2: Certified Caretaker 🍫" if pts < 100 else "Level 3: Ultimate Dark Romance Master 👑")
st.caption(f"**Current Rank:** {level}")

# Main Card
st.markdown(f"""
    <div class="phase-card">
        <h2 style="color: {strategy['color']}; margin-top: 0;">{strategy['title']}</h2>
        <p style="font-size: 1.1rem; color: #ffb703; margin-bottom: 20px;"><em>"{strategy['summary']}"</em></p>
        <hr style="border-color: #e63946; margin-bottom: 20px;">
        <h3 style="color: #f1faee; font-size: 1.2rem; margin-bottom: 15px;">📌 Aaj Ka Action Plan:</h3>
    </div>
""", unsafe_allow_html=True)

for act in strategy["actions"]:
    st.markdown(f"""
        <div class="action-box">
            {act}
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🗓️ Calendar", "🍕 Food & Movies", "🎮 Mood Games", "🚨 Emergency Excuse", "🎁 Snack Roulette", "📝 Her Cheatsheet"])

# TAB 1: CALENDAR
with tab1:
    st.subheader("🗓️ Boyfriend Master Clearance Calendar")
    now = datetime.today()
    cal = calendar.monthcalendar(now.year, now.month)
    
    cols = st.columns(7)
    days_abbr = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for idx, col in enumerate(cols):
        col.write(f"**{days_abbr[idx]}**")
        
    for week in cal:
        cols = st.columns(7)
        for idx, day_num in enumerate(week):
            if day_num == 0:
                cols[idx].write(" ")
            else:
                date_obj = datetime(now.year, now.month, day_num).date()
                d_c = ((date_obj - start_dt).days % cycle_len) + 1
                strat = get_cycle_strategy(d_c, cycle_len)
                
                is_today = " (AAJ)" if date_obj == today else ""
                cols[idx].markdown(f"""
                    <div style="background-color: #160b13; padding: 10px; border-radius: 8px; border-left: 3px solid {strat['color']}; margin-bottom: 6px;">
                        <strong style="color: #ffffff;">{day_num}</strong><small>{is_today}</small><br>
                        <span style="font-size: 0.75rem; color: {strat['color']};">{strat['phase'].split(' ')[0]}</span>
                    </div>
                """, unsafe_allow_html=True)

# TAB 2: LIVE FOOD & MOVIE CONCIERGE
with tab2:
    st.subheader("🍕 Live Food & Movie Smart Concierge")
    st.write(f"Current Location: **{user_city}** 📍 | Select mood to fetch live delivery & streaming options:")
    
    selected_mood = st.selectbox("Select Current Vibe / Phase:", list(MOOD_DATABASE.keys()))
    rec = MOOD_DATABASE[selected_mood]
    
    food_q = urllib.parse.quote(f"{rec['food_query']} near me")
    zomato_url = f"https://www.zomato.com/{user_city.lower()}/restaurants?q={food_q}"
    swiggy_url = f"https://www.swiggy.com/search?query={food_q}"
    
    movie_q = urllib.parse.quote(rec['movie_query'])
    netflix_url = f"https://www.netflix.com/search?q={movie_q}"
    youtube_url = f"https://www.youtube.com/results?search_query={movie_q}"
    
    st.markdown(f"""
        <div class="concierge-card">
            <h3>🍽️ Recommended Food Pairing:</h3>
            <p style="font-size: 1.1rem; color: #ffb703; margin-bottom: 15px;">{rec['food']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_z, col_s = st.columns(2)
    with col_z:
        st.markdown(f'<a href="{zomato_url}" target="_blank"><button style="background-color: #cb202d; color: white; border: none; padding: 10px 15px; border-radius: 6px; font-weight: bold; width: 100%; cursor: pointer;">🔍 Search Live on Zomato</button></a>', unsafe_allow_html=True)
    with col_s:
        st.markdown(f'<a href="{swiggy_url}" target="_blank"><button style="background-color: #fc8019; color: white; border: none; padding: 10px 15px; border-radius: 6px; font-weight: bold; width: 100%; cursor: pointer;">🔍 Search Live on Swiggy</button></a>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"""
        <div class="concierge-card">
            <h3>🍿 Recommended Movie / Show ({rec['ott']}):</h3>
            <p style="font-size: 1.1rem; color: #48cae4; margin-bottom: 15px;">{rec['movie']}</p>
        </div>
    """, unsafe_allow_html=True)

    col_n, col_y = st.columns(2)
    with col_n:
        st.markdown(f'<a href="{netflix_url}" target="_blank"><button style="background-color: #e50914; color: white; border: none; padding: 10px 15px; border-radius: 6px; font-weight: bold; width: 100%; cursor: pointer;">🎬 Search on Netflix / OTT</button></a>', unsafe_allow_html=True)
    with col_y:
        st.markdown(f'<a href="{youtube_url}" target="_blank"><button style="background-color: #ff0000; color: white; border: none; padding: 10px 15px; border-radius: 6px; font-weight: bold; width: 100%; cursor: pointer;">▶️ Watch Trailer on YouTube</button></a>', unsafe_allow_html=True)

# TAB 3: MOOD-BASED GAME HUB
with tab3:
    st.subheader("🎮 Mood-Based Interactive Mini Games")
    st.write("Aaj ke mood ke hisab se game chunno aur sath me khelo!")
    
    game_mode = st.radio("Choose Game Arena:", ["🩸 Cramp Relief Tapper (Periods)", "🌱 Couple Decision Spinner (Chill Mode)", "🔥 Truth or Dare (Ovulation / Date Night)"])
    
    if "Cramp Relief" in game_mode:
        st.markdown("""
            <div class="game-card">
                <h3 style="color: #e63946;">🩸 Cramp Relief Tapper Game</h3>
                <p>Tap the buttons to deliver care and reduce her Cramp Bar to 0%!</p>
            </div>
        """, unsafe_allow_html=True)
        
        if "cramp_level" not in st.session_state:
            st.session_state["cramp_level"] = 100
            
        st.progress(st.session_state["cramp_level"] / 100)
        st.caption(f"**Current Cramp Bar:** {st.session_state['cramp_level']}%")
        
        g1, g2, g3 = st.columns(3)
        with g1:
            if st.button("🧸 Offer Hot Water Bag (-20%)"):
                st.session_state["cramp_level"] = max(0, st.session_state["cramp_level"] - 20)
                st.rerun()
        with g2:
            if st.button("🍫 Feed Dark Chocolate (-25%)"):
                st.session_state["cramp_level"] = max(0, st.session_state["cramp_level"] - 25)
                st.rerun()
        with g3:
            if st.button("🥟 Order Hot Momos (-30%)"):
                st.session_state["cramp_level"] = max(0, st.session_state["cramp_level"] - 30)
                st.rerun()
                
        if st.session_state["cramp_level"] == 0:
            st.balloons()
            st.success("🎉 CRAMP BAR CLEARED! You earned +20 Devotion Points!")
            if st.button("Reset Cramp Bar 🔄"):
                st.session_state["cramp_level"] = 100
                stored["devotion_points"] = stored.get("devotion_points", 50) + 20
                save_data(stored)
                st.rerun()

    elif "Decision Spinner" in game_mode:
        st.markdown("""
            <div class="game-card">
                <h3 style="color: #2a9d8f;">🌱 Couple Decision Wheel</h3>
                <p>Confusion hai ki aaj raat kya karna hai? Wheel spin karo!</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎲 Spin Decision Wheel"):
            decisions = [
                "🍕 Decision: Today HE orders his choice of food, SHE chooses the movie!",
                "🍿 Decision: Late night drive + Ice Cream run!",
                "🍔 Decision: SHE orders her absolute favorite comfort meal!",
                "🛋️ Decision: No phone evening, 1 hour pure pillow talk!"
            ]
            st.info(random.choice(decisions))

    elif "Truth or Dare" in game_mode:
        st.markdown("""
            <div class="game-card">
                <h3 style="color: #ff4d6d;">🔥 Dark Romance Truth or Dare</h3>
                <p>High-energy date night game to spark romance!</p>
            </div>
        """, unsafe_allow_html=True)
        
        td_col1, td_col2 = st.columns(2)
        with td_col1:
            if st.button("🔍 Draw Truth Question"):
                st.session_state["td_res"] = f"**TRUTH:** {random.choice(TRUTHS)}"
        with td_col2:
            if st.button("🔥 Draw Dare Mission"):
                st.session_state["td_res"] = f"**DARE:** {random.choice(DARES)}"
                
        if "td_res" in st.session_state:
            st.warning(st.session_state["td_res"])

# TAB 4: EMERGENCY EXCUSE GENERATOR
with tab4:
    st.subheader("🚨 Emergency Apology / Excuse Generator")
    if st.button("🔥 Generate Emergency Text"):
        excuse = random.choice(EXCUSES)
        st.markdown(f"""
            <div class="excuse-box">
                <p style="font-size: 1.1rem; color: #ff4d6d; margin: 0;">{excuse}</p>
            </div>
        """, unsafe_allow_html=True)

# TAB 5: SNACK ROULETTE & DEVOTION SCORE
with tab5:
    st.subheader("🎁 Surprise Snack Roulette")
    c_btn1, c_btn2 = st.columns(2)
    with c_btn1:
        if st.button("🎲 Spin Snack Idea"):
            st.session_state["snack"] = random.choice(SNACKS)
    with c_btn2:
        if st.button("✅ Executed Mission (+10 Devotion Points)"):
            stored["devotion_points"] = stored.get("devotion_points", 50) + 10
            save_data(stored)
            st.success("Points Added! Rank Upgrade Progressed ⭐")
            st.rerun()
            
    if "snack" in st.session_state:
        st.info(f"### 💡 Recommended Surprise:\n{st.session_state['snack']}")

# TAB 6: HER CHEATSHEET / NOTES
with tab6:
    st.subheader("📝 Her Secret Preferences & Notes")
    current_notes = stored.get("notes", "")
    updated_notes = st.text_area("Her Favorites / Sizes / Cravings", value=current_notes, height=200)
    
    if st.button("Save Cheatsheet 💾"):
        stored["notes"] = updated_notes
        save_data(stored)
        st.success("Cheatsheet updated successfully!")
        
