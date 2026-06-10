import csv
import random

import streamlit as st

from library import quicksort

st.set_page_config(page_title="Exercise 3")

# the app is run from the repo root (streamlit run Home.py), so the CSV is right there
CSV_FILE = "country_strength.csv"


def load_teams():
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        teams = [
            (float(r["squad_strength"]), r["country"], r["best_player"])
            for r in csv.DictReader(f)
        ]
    random.shuffle(teams)  # CSV is pre-ranked, scramble it so Sort has work to do
    return teams


def reset_teams():
    st.session_state.teams = load_teams()
    st.session_state.sorted = False


def sort_teams():
    quicksort(st.session_state.teams)  # ascending, in place
    st.session_state.teams.reverse()   # flip to strongest first
    st.session_state.sorted = True


def add_team():
    name = st.session_state.new_name.strip()
    if name:
        st.session_state.teams.append((float(st.session_state.new_rating), name, "(custom)"))
        st.session_state.sorted = False
        st.session_state.new_name = ""


if "teams" not in st.session_state:
    reset_teams()

st.header("Exercise 3")
st.subheader("World Cup Power Ranking")
st.caption("National teams ranked by the average overall of their top 23 FIFA 23 players, sorted with quicksort.")

with st.expander("Add a team"):
    c1, c2, c3 = st.columns([3, 2, 1])
    c1.text_input("Country", key="new_name", placeholder="e.g. Singapore")
    c2.number_input("Strength", 0.0, 100.0, 75.0, 0.1, key="new_rating")
    c3.button("Add", on_click=add_team)

left, right = st.columns(2)
left.button("Sort", on_click=sort_teams, type="primary", use_container_width=True)
right.button("Reset", on_click=reset_teams, use_container_width=True)

label = "Ranked strongest to weakest" if st.session_state.sorted else "Unsorted (shuffled)"
st.markdown(f"**{label}** · {len(st.session_state.teams)} teams")

rows = ""
for i, (strength, country, star) in enumerate(st.session_state.teams, start=1):
    pos = i if st.session_state.sorted else "&ndash;"
    rows += f"<tr><td class='rk'>{pos}</td><td class='ct'>{country}</td><td class='sc'>{strength:.2f}</td><td class='bp'>{star}</td></tr>"

st.markdown(f"""
<style>
.t {{ width:100%; border-collapse:collapse; font-family:'Inter',system-ui,sans-serif; }}
.t th {{ text-align:left; font-size:.7rem; letter-spacing:.09em; text-transform:uppercase; color:#9a9a9a; padding:8px 12px; border-bottom:1px solid #e6e6e6; }}
.t td {{ padding:10px 12px; border-bottom:1px solid #f1f1f1; font-size:.92rem; }}
.t .rk {{ width:46px; color:#b3b3b3; }}
.t .ct {{ font-weight:600; }}
.t .sc {{ width:84px; color:#00a35c; font-weight:600; }}
.t .bp {{ color:#8c8c8c; font-size:.85rem; }}
</style>
<table class="t"><thead><tr><th>#</th><th>Country</th><th>Strength</th><th>Star</th></tr></thead><tbody>{rows}</tbody></table>
""", unsafe_allow_html=True)
