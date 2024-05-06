import streamlit as st
import pandas as pd
import seaborn as sns
st.header("Hello Stramlit")
st.markdown('*Hello Debjyoti*')
st.markdown('''
            1. 1st item
            2. 2nd item
            3. 3rd item
            ''')
st.markdown('''
            - 1st item
            - 2nd item
            - 3rd item
            ''')
st.title('streamlit Rocks :100:')
st.code("""
        //Hello world using C
        #include<stdio.h>
        int main()
        {
        printf("Hello world")
        }""",language='c')
df=sns.load_dataset('mpg')
st.dataframe(df.style.highlight_max(axis=0,color='orange'))
st.dataframe(df.style.background_gradient(cmap='magma'))
st.table(df.head(15))
st.table(df.tail())
st.subheader('JASON STRING')
st.json(
    {
    'first_five_mpg':list(df['mpg'][:10])
    }
)

st.line_chart(df,x='weight',y='horsepower')

st.area_chart(df,x='weight',y='horsepower')

st.bar_chart(df,x='origin',y='cylinders')



if st.button('click me'):
    st.success('yahh!!!')
    
df=sns.load_dataset('tips')
st.dataframe(df)

v=df.to_csv(index=False)

st.download_button(
    label="CSV Download option",
    data=v,
    file_name='tips.csv',
    mime='text/csv'
)

mc=st.checkbox('Click me')
if mc:
    st.write('Checkbox is activate....')

rad=st.radio("Please choose hou u want to die !!",('head','baaz','jobless'))
if rad:
    st.write(f'The selection is : **{rad}**')
age=st.slider('please select age',min_value=1,max_value=100)

if age:
    st.write(f"your age is **{age}**")

from datetime import datetime,date,timedelta

cd=datetime.now()

dsc=cd+timedelta(days=7)

mc=st.date_input('What is your DOB',dsc)

if mc:
    st.write(f"Your DOB is **{mc}**")
df=st.file_uploader('Select CSV')
if df:
    a=pd.read_csv(df)
    st.write('The First 5 rows are: ')
    st.write(a.head())

st.header("Sample Video :	:coffee:")
video=open('video.mp4','rb')
v=video.read()
st.video(v)

st.header("Sample Audio ::sparkles:")
audio=open('abc.mp3','rb')
r=audio.read()
st.audio(r,format='audio/mp3')




                 
                 





