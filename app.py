import streamlit as st
import pickle
import pandas as pd


pipe=pickle.load(open('pipe.pkl','rb'))


teams=['Sunrisers Hyderabad', 'Mumbai Indians','Delhi Capitals',
    'Royal Challengers Bangalore','Kolkata Knight Riders',
    'Kings XI Punjab','Chennai Super Kings', 'Rajasthan Royals',]

city=['Mumbai', 'Chandigarh', 'Kolkata', 'Hyderabad', 'Jaipur',
    'Chennai', 'Dharamsala', 'Kanpur', 'Kimberley', 'Sharjah',
    'Johannesburg', 'Bangalore', 'Kochi', 'Cuttack', 'Delhi',
    'Centurion', 'Nagpur', 'Pune', 'Ranchi', 'East London', 'Mohali',
    'Durban', 'Port Elizabeth', 'Ahmedabad', 'Abu Dhabi', 'Cape Town',
    'Bengaluru', 'Raipur', 'Visakhapatnam', 'Indore', 'Rajkot']    

st.title('IPL Winning Team Predector')

col1,col2 = st.columns(2)

with col1:
    battibg_team=st.selectbox('Select Batting Team',sorted(teams))

with col2:
    bowling_team=st.selectbox('Select Bowling Team',sorted(teams))    

city=st.selectbox('Selcet City',sorted(city))  

target=st.number_input('Target')

col3,col4,col5=st.columns(3)

with col3:
    score=st.number_input('Score')

with col4:
    wickets=st.number_input('Wickets Out')

with col5:
    overs=st.number_input('Over Completed')  

if st.button('Predict'):
    balls_left=120-(overs*6)
    runs_left=target-score
    wickets=10-wickets     
    crr=score/overs
    rrr=(runs_left*6)/balls_left 

    input=pd.DataFrame({'batting_team':[battibg_team],'bowling_team':[bowling_team],'city':[city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[score],'crr':[crr],'rrr':[rrr]})
    result=pipe.predict_proba(input)
    loss=result[0][0]
    win=result[0][1]

    st.header(battibg_team + "- "+str(round(win*100))+"%")
    st.header(bowling_team + "- "+str(round(loss*100))+"%")
