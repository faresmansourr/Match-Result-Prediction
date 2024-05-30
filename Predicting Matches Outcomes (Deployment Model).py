import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load(open("Match_Outcomes",'rb'))

# Define the team names with their corresponding indexes
teams = {
    "Sheffield United": 0,
    "Arsenal": 1,
    "Everton": 2,
    "Newcastle United": 3,
    "Portsmouth": 4,
    "Reading": 5,
    "West Ham United": 6,
    "Bolton Wanderers": 7,
    "Manchester United": 8,
    "Chelsea": 9,
    "Watford": 10,
    "Tottenham Hotspur": 11,
    "Aston Villa": 12,
    "Manchester City": 13,
    "Blackburn Rovers": 14,
    "Charlton Athletic": 15,
    "Fulham": 16,
    "Middlesbrough": 17,
    "Liverpool": 18,
    "Wigan Athletic": 19,
    "Sunderland": 20,
    "Derby County": 21,
    "Birmingham City": 22,
    "Hull City": 23,
    "Stoke City": 24,
    "West Bromwich Albion": 25,
    "Wolverhampton Wanderers": 26,
    "Burnley": 27,
    "Queens Park Rangers": 28,
    "Norwich City": 29,
    "Swansea City": 30,
    "Southampton": 31,
    "Crystal Palace": 32,
    "Cardiff City": 33,
    "Leicester City": 34,
    "AFC Bournemouth": 35,
    "Brighton and Hove Albion": 36,
    "Huddersfield Town": 37
}

# Define the prediction function
def predict_match_outcome(home_team, away_team, season, home_goals, away_goals, wins_home, losses_home, goals_home, total_yel_card_home, total_red_card_home, clean_sheet_home, goals_conceded_home, wins_away, losses_away, goals_away, total_yel_card_away, total_red_card_away, clean_sheet_away, goals_conceded_away):
    # Create a DataFrame with the input values
    input_data = pd.DataFrame({
        'home_team': [teams[home_team]],
        'away_team': [teams[away_team]],
        'season': [season],
        'home_goals': [home_goals],
        'away_goals': [away_goals],
        'wins_home': [wins_home],
        'losses_home': [losses_home],
        'goals_home': [goals_home],
        'total_yel_card_home': [total_yel_card_home],
        'total_red_card_home': [total_red_card_home],
        'clean_sheet_home': [clean_sheet_home],
        'goals_conceded_home': [goals_conceded_home],
        'wins_away': [wins_away],
        'losses_away': [losses_away],
        'goals_away': [goals_away],
        'total_yel_card_away': [total_yel_card_away],
        'total_red_card_away': [total_red_card_away],
        'clean_sheet_away': [clean_sheet_away],
        'goals_conceded_away': [goals_conceded_away]
    })

    # Make the prediction
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        return f"{home_team} wins"
    elif prediction[0] == 2:
        return f"{away_team} wins"
    else:
        return "Draw"

# Streamlit app
st.title('Match Outcome Predictor')

# Dropdown for selecting home team
home_team = st.selectbox('Select Home Team', list(teams.keys()))

# Dropdown for selecting away team
away_team = st.selectbox('Select Away Team', list(teams.keys()))

season = st.text_input('Season', '2018')
home_goals = st.number_input('Home Goals', min_value=0, value=20)
away_goals = st.number_input('Away Goals', min_value=0, value=10)
wins_home = st.number_input('Wins Home', min_value=0, value=30)
losses_home = st.number_input('Losses Home', min_value=0, value=5)
goals_home = st.number_input('Goals Home', min_value=0, value=30)
total_yel_card_home = st.number_input('Total Yellow Cards Home', min_value=0, value=15)
total_red_card_home = st.number_input('Total Red Cards Home', min_value=0, value=1)
clean_sheet_home = st.number_input('Clean Sheets Home', min_value=0, value=8)
goals_conceded_home = st.number_input('Goals Conceded Home', min_value=0, value=20)
wins_away = st.number_input('Wins Away', min_value=0, value=12)
losses_away = st.number_input('Losses Away', min_value=0, value=7)
goals_away = st.number_input('Goals Away', min_value=0, value=25)
total_yel_card_away = st.number_input('Total Yellow Cards Away', min_value=0, value=25)
total_red_card_away = st.number_input('Total Red Cards Away', min_value=0, value=2)
clean_sheet_away = st.number_input('Clean Sheets Away', min_value=0, value=5)
goals_conceded_away = st.number_input('Goals Conceded Away', min_value=0, value=30)

if st.button('Predict'):
    result = predict_match_outcome(
        home_team, away_team, season, home_goals, away_goals, wins_home, losses_home, goals_home, total_yel_card_home, total_red_card_home, clean_sheet_home, goals_conceded_home,
        wins_away, losses_away, goals_away, total_yel_card_away, total_red_card_away, clean_sheet_away, goals_conceded_away
    )
    st.write(f"{result}")
