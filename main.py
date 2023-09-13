import streamlit as st
import plotly.express as px
import backend as bk
st.header("Gaebs' Weather Forecast for the next days") 
col1,col2,col3,col4=st.columns(4)
place=st.text_input(label="Place") 
forecast_days=st.slider("Forecast Days",min_value=1,
max_value=5,help="Number of days of forecasted days") 
select=st.selectbox("Select data to view",
["Temperature","Sky Conditions"]) 
st.subheader(f"{select} for the next {forecast_days} day(s) in {place.title()}")  


if place !="":
    try:
        data=bk.Get_Data(place=place,days=forecast_days) 
        temp=data[0] 
        date=data[1]
        clouds=data[2]
        if select=="Temperature":            
            figure=px.line(x=date,y=temp,labels={"x":"Date","y":"Temperature in (C)"}) 
            st.plotly_chart(figure) 
        if select=="Sky Conditions": 
            date_index=0
            column_index=0
            cols=st.columns(8) 
            for cloud in clouds: 
                with cols[column_index]:
        #st.write(cloud) 
                    st.write(date[date_index]) 
                    if cloud=="Clouds":
                        st.image("images/cloud.png",width=120)
                    if cloud=="Clear":
                        st.image("images/clear.png",width=120) 
                    if cloud=="Rain":
                        st.image("images/rain.png",width=120) 
                    if cloud=="Snow":
                        st.image("images/snow.png",width=120) 
                date_index=date_index+1     
                column_index=column_index+1  
                if column_index==8:
                    column_index=0    
    except:
        st.error("City does not exist. Perhaps you typed it incorrectly? Pls enter a valid city name ")                
    #print(clouds)
else:
    pass
