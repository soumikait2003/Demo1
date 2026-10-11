import streamlit as st
from datetime import datetime, timedelta
import json
import os
import random
import calendar

# Page Configuration - Desi Vibe
st.set_page_config(page_title="Bande Ka Playbook 🗿", page_icon="🔥", layout="wide")

DATA_FILE = "bandi_cycle.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"last_period_date": str(datetime.today().date()), "cycle_length": 28}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# Dark Desi Custom Styling (Corrected CSS parameter)
st.markdown("""
    <style>
    .stApp {
        background-color: #0d090a;
        color: #f1faee;
    }
    .meme-card {
        background-color: #160b13;
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #e63946;
        margin-bottom: 15px;
    }
    .stButton>button {
        background-color: #e63946 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# Desi Meme Logic Engine
def get_desi_strategy(cycle_day):
    if 1 <= cycle_day <= 5:
        return {
            "title": "🩸 DAYS 1-5: Khatra Hai Bhai! (Periods)",
            "clearance": "SERVICE & SEWA MODE 🙇‍♂️",
            "color": "#e63946",
            "vibe": "Mood swings 100%, Energy 0%. Dimaag mat chala, bass momos aur hot water bag laa!",
            "dos": ["Hot water bag ready rakho", "Bina mange uske fav snacks/chocolate le aao", "Har baat me bol: 'Haan tum bilkul sahi bol rahi ho'"],
            "donts": ["Yeh mat poocho: 'Tum gussa kyun ho?'", "Galti se bhi debate mat jeetne ki koshish karna", "Dost ke saath shaam ko gayab mat hona"],
            "meme": "“Bhai shaant reh... zinda bachna hai toh aage se bina bole snacks khila de!” 🍫"
        }
    elif 6 <= cycle_day <= 10:
        return {
            "title": "🌱 DAYS 6-10: Mausam Suhana Hai (Follicular)",
            "clearance": "FLIRT & TEASE MODE 😉",
            "color": "#2a9d8f",
            "vibe": "Energy waapas aa rahi hai! Bandi ka mood chill hai. Flirting chalu kar do.",
            "dos": ["Choti-moti tareef kar do (Hair, Outfit)", "Shaam ko chai/coffee date pe le jaao", "Thoda playful leg-pulling chalta hai"],
            "donts": ["Boriyat mat dikhao", "Old boring baatein mat karo"],
            "meme": "“Abhi mahaul tight nahi hai, thoda romance aur hassi-mzak pelo!” ✨"
        }
    elif 11 <= cycle_day <= 16:
        return {
            "title": "🔥 DAYS 11-16: FULL HERO GIRI & NEXT LEVEL (Ovulation Window)",
            "clearance": "MAXIMUM ATTRACTION & FLIRT 🔥",
            "color": "#ff4d6d",
            "vibe": "PEAK OVULATION ZONE! Energy High, Confidence High, Romance 200%. Full Hero Banna Hai!",
            "dos": ["Thoda ready ho ke milne jaao (Perfume maar ke)", "Late night drive ya romantic date plan karo", "Bold flirt aur eye contact maintain karo"],
            "donts": ["CONFUSED mat raho ('Tum batao kahan chalein?')", "Ghar pe aalas mat maro"],
            "meme": "“Bhai yeh waqt hai tera! Full Dark Romance aur Hero Giri dikha de!” 😎🍷"
        }
    else:
        return {
            "title": "🌙 DAYS 17-28: Careful Reassurance Zone (Luteal/PMS)",
            "clearance": "PAMPER & CUDDLE MODE 🧸",
            "color": "#f4a261",
            "vibe": "Progesterone high hai. Kabhi pyara mood, kabhi choti baat pe emotional. Reassurance do!",
            "dos": ["Apni oversized hoodie usko de do", "Bina wajah batao ki wo kitni cute hai", "Uski pasand ka khana order kar do"],
            "donts": ["Baat-baat pe irritate mat ho", "Usko Akela feel mat hone do"],
            "meme": "“Thoda sabr rakho bhai... bas pyaar se suno aur pampers baanto!” ☕"
        }

# Random Desi Roleplay Generator
DESI_ROLEPLAYS = [
    {
        "title": "🍸 'Anjaani Raatein' (Stranger at the Cafe)",
        "setup": "Ek hi cafe/lounge me alag alag jaao. 10 min baad acting karo ki pehli baar mile ho aur best/worst line se pick up karo."
    },
    {
        "title": "💼 'Strict Boss & Personal Assistant'",
        "setup": "Aaj raat saare decisions tum loge (Khana, location, timing). Usko bas tumhari baat sunni hai aur tumhein full royal feel deni hai."
    },
    {
        "title": "🚗 'Late Night Drive & Secret Talks'",
        "setup": "Gadi/Bike nikalo, slow dark-romance songs lagao, aur direct kisi shaant jagah jaake 3 deep secrets share karo."
    }
]

# App Layout
st.title("🗿 BANDE KA PLAYBOOK: Bandi Ka Cycle Tracker")
st.caption("Tere liye daily intelligence report ki kab Pamper karna hai, kab Flirt aur kab Next Level jana hai!")

stored = load_data()

# Secret Setup
with st.expander("⚙️ Secret Entry: Bandi ki Dates Set Karo", expanded=False):
    with st.form("set_dates"):
        c1, c2 = st.columns(2)
        with c1:
            p_date = st.date_input("Bandi ki last period date kab thi?", value=datetime.strptime(stored["last_period_date"], "%Y-%m-%d").date())
        with c2:
            c_len = st.number_input("Uska cycle kitne din ka hai? (Default: 28)", min_value=20, max_value=45, value=stored.get("cycle_length", 28))
        if st.form_submit_button("Data Save Karo 🔒"):
            save_data({"last_period_date": str(p_date), "cycle_length": int(c_len)})
            st.success("Target set ho gaya bhai! Calculation updated.")
            st.rerun()

# Date Math
start_dt = datetime.strptime(stored["last_period_date"], "%Y-%m-%d").date()
today = datetime.today().date()
cycle_len = stored.get("cycle_length", 28)

day_in_cycle = ((today - start_dt).days % cycle_len) + 1
strat = get_desi_strategy(day_in_cycle)

st.markdown("---")
st.subheader("📍 Aaj Ka Daily Briefing (Tere Liye Directive)")

m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Cycle Day", f"Day {day_in_cycle} / {cycle_len}")
with m2:
    st.metric("Aaj Ka Mode", strat["clearance"])
with m3:
    ovulation_day = start_dt + timedelta(days=cycle_len - 14)
    st.metric("Peak Ovulation Date", ovulation_day.strftime("%b %d"))

# Main Banner Card
st.markdown(f"""
    <div class="meme-card">
        <h2 style="color: {strat['color']};">{strat['title']}</h2>
        <p style="font-size: 1.2rem; color: #ffb703;">{strat['meme']}</p>
        <p style="font-size: 1rem;"><strong>Vibe Report:</strong> {strat['vibe']}</p>
    </div>
""", unsafe_allow_html=True)

# Do's and Don'ts
col_a, col_b = st.columns(2)
with col_a:
    st.success("### ✅ YE WALI CHEEZEN KARO")
    for d in strat["dos"]:
        st.write(f"• {d}")

with col_b:
    st.error("### ❌ YE GALTI BHI MAT KARNA")
    for d in strat["donts"]:
        st.write(f"• {d}")

st.markdown("---")

# TABS
tab1, tab2 = st.tabs(["🗓️ Pura Mahine Ka Master Calendar", "🔥 Next-Level Ovulation Hub"])

# TAB 1: CALENDAR
with tab1:
    st.subheader("🗓️ Boyfriend Master Clearance Calendar")
    st.caption("Rang dekho aur samajh jaao kab kya karna hai!")
    
    now = datetime.today()
    cal = calendar.monthcalendar(now.year, now.month)
    
    # Legend
    l1, l2, l3, l4 = st.columns(4)
    l1.markdown("🔴 **Days 1-5:** Sewa Mode")
    l2.markdown("🟢 **Days 6-10:** Flirt Mode")
    l3.markdown("🔥 **Days 11-16:** Next Level")
    l4.markdown("🌙 **Days 17-28:** Pamper Mode")
    
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
                day_c = ((date_obj - start_dt).days % cycle_len) + 1
                s = get_desi_strategy(day_c)
                
                is_today = " (AAJ)" if date_obj == today else ""
                cols[idx].markdown(f"""
                    <div style="background-color: #1a0f18; padding: 8px; border-radius: 6px; border-left: 4px solid {s['color']}; margin-bottom: 5px;">
                        <strong style="color: #ffffff;">{day_num}</strong>{is_today}<br>
                        <small style="color: {s['color']};">{s['clearance'].split(' ')[0]}</small>
                    </div>
                """, unsafe_allow_html=True)

# TAB 2: OVULATION GAME HUB
with tab2:
    st.subheader("🔥 Ovulation Special: Hero Giri & Roleplay")
    if 11 <= day_in_cycle <= 16:
        st.success("🔥 **NEXT-LEVEL CLEARANCE ACTIVE!** Bandi Ovulation Phase me hai, energy full hai!")
        
        if st.button("🎲 Aaj Raat Ka Secret Roleplay Mission Draw Karo"):
            st.session_state["desi_roleplay"] = random.choice(DESI_ROLEPLAYS)
            
        if "desi_roleplay" in st.session_state:
            card = st.session_state["desi_roleplay"]
            st.info(f"### 🍷 {card['title']}\n\nMission Rule:")
    else:
        st.warning(f"🔒 Abhi Next-Level locked hai bhai! Current Mode: **{strat['clearance']}**. Days 11-16 me automatic unlock ho jayega!")
