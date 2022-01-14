import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import base64
import algos

algorithms=["FCFS - First come first serve","SJF - Shortest Job First", "SRTF - Shortest Remaining Time First"]

def input_form():
    with st.form('input form'):
        algo=st.selectbox('Select Algorithm',algorithms)
        at=st.text_input('Arrival Time')
        bt=st.text_input('Burst Time')
        res=st.form_submit_button('Calculate')

    if at==''and  res:
        st.error("Input cannot be empty")

    elif bt=='' and res:
        st.error("Input cannot be empty")
    
    elif bt.split(" ").count('0')>0 and res:
        st.warning("Burst time cannot be zero")

    elif len(bt)!=len(at) and res:
        st.warning("Number of arrival times and burst times do not match")

    elif res==False:
        file_ = open("maths.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="">',unsafe_allow_html=True,)

    elif at!='' and bt!='' and res:
        at_list=list(map(int,at.split(" ")))
        bt_list=list(map(int,bt.split(" ")))
        st.header('Result : ')
        if algo=="FCFS - First come first serve":
            result,wt,tat,ct=algos.fcfs(at_list,bt_list,len(at_list))
            df=pd.DataFrame(result,columns=["AT","BT","CT","WT","TAT"],index=[i for i in range(1,len(at_list)+1)])
            st.table(df)
            col1,col2=st.columns(2)
            col1.success("Average Waiting Time = "+str(wt)+" / " +str(len(at_list))+" = "+str(round(wt/len(at_list),4)))
            col2.info("Average TurnAround Time = "+str(tat)+" / " +str(len(at_list))+" = "+str(round(tat/len(at_list),4)))
