import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import graphviz as graphviz


st.write("Basic streamlit app")

# @st.cache is a caching mechanism that allows your app to stay performant
@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

app_mode = st.sidebar.selectbox('Select Page',['Home', 'Loan','Selectors','Inputs','Celebrate', 'Notifications', 'Data Viz']) #two pages
if app_mode=='Home':
    st.title('Home Page :')  
    st.write('Select a page from the sidebar')

elif app_mode=='Loan':
    st.title('LOAN PREDICTION :')  
    # st.image('loan_image.jpg')
    st.markdown('Dataset :')
    # data=pd.read_csv('loan_dataset.csv')
    # st.write(data.head())
    st.markdown('Applicant Income VS Loan Amount ')
    # st.bar_chart(data[['ApplicantIncome','LoanAmount']].head(20))

elif app_mode=='Selectors':
    st.checkbox('yes')
    st.button('Click')
    st.radio('Pick your gender',['Male','Female'])
    st.selectbox('Pick your gender',['Male','Female'])
    st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
    st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
    st.slider('Pick a number', 0,50)

elif app_mode=='Inputs':
    st.number_input('Pick a number', 0,10)
    st.text_input('Email address')
    st.date_input('Travelling date')
    st.time_input('School time')
    st.text_area('Description')
    st.file_uploader('Upload a photo')
    st.color_picker('Choose your favorite color')

elif app_mode=='Notifications':
    st.success("You did it !")
    st.error("Error")
    st.warning("Warning")
    st.info("It's easy to build a streamlit app")
    st.exception(RuntimeError("RuntimeError exception"))
elif app_mode=='Celebrate':
    st.markdown('Counting from 5 :')
    st.progress(5)
    with st.spinner('Wait for it...'):
        time.sleep(5)
        st.balloons()

elif app_mode=='Data Viz':
    st.write("Some charts, maps and visualisations")

    #Histograph
    hist_c = st.container()
    hist_c.write("basic histograph")
    rand=np.random.normal(1, 2, size=20)
    fig, ax = plt.subplots()
    ax.hist(rand, bins=15)
    hist_c.pyplot(fig)

    #Line chart
    line_c = st.container()
    line_c.write("basic line chart")
    line_c_df= pd.DataFrame(
        np.random.randn(10, 2),
        columns=['x', 'y'])
    line_c.line_chart(line_c_df)

    #Bar chart
    bar_c = st.container()
    bar_c.write("basic bar chart")
    bar_c_df= pd.DataFrame(
        np.random.randn(10, 2),
        columns=['x', 'y'])
    bar_c.bar_chart(bar_c_df)

    #Area chart
    area_c = st.container()
    area_c.write("basic area chart")
    area_c_df= pd.DataFrame(
        np.random.randn(10, 2),
        columns=['x', 'y'])
    area_c.area_chart(area_c_df)

    # Graph
    st.graphviz_chart('''
    digraph {
        Big_shark -> Tuna
        Tuna -> Mackerel
        Mackerel -> Small_fishes
        Small_fishes -> Shrimp
    }
''')

    #Map
    df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
    st.map(df)


    st.write("End of page")
