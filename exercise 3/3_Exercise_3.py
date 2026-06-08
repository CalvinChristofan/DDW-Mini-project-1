import csv
from pathlib import Path

import streamlit as st

from library import quicksort

st.set_page_config(page_title="Exercise 3")

# country_strength.csv dataset, see on repo root
DATA_FILES = [
    Path(__file__).resolve().parent.parent / "country_strength.csv",
    Path(__file__).resolve().parent / "country_strength.csv",
    Path("country_strength.csv"),
]


def load_teams():
    for path in DATA_FILES:
        if path.exists():
            with open(path, newline="", encoding="utf-8") as f:
                teams = [
                    (float(r["squad_strength"]), r["country"], r["best_player"])
                    for r in csv.DictReader(f)
                ]
            teams.sort(key=lambda t: t[1]) 
            return teams
    return None


def reset_teams():
    base = load_teams()
    st.session_state.teams = list(base) if base else []
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

if not st.session_state.teams:
    st.error("country_strength.csv not found. Put it in your repo root, next to Home.py.")
    st.stop()

with st.expander("Add a team"):
    c1, c2, c3 = st.columns([3, 2, 1])
    c1.text_input("Country", key="new_name", placeholder="e.g. Singapore")
    c2.number_input("Strength", 0.0, 100.0, 75.0, 0.1, key="new_rating")
    c3.button("Add", on_click=add_team)

left, right = st.columns(2)
left.button("Sort", on_click=sort_teams, type="primary", use_container_width=True)
right.button("Reset", on_click=reset_teams, use_container_width=True)

label = "Ranked strongest to weakest" if st.session_state.sorted else "Unsorted (alphabetical)"
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
