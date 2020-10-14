import streamlit as st
import pickle



lin_model=pickle.load(open('lin_model.pkl','rb'))
log_model=pickle.load(open('log_model.pkl','rb'))


def classify(num):
    if num<0.5:
        return 'Setosa'
    elif num <1.5:
        return 'Versicolor'
    else:
        return 'Virginica'
def main():
    st.title("Streamlit Tutorial")
    html_temp = """
    <div style="background-color:#6bd4c8 ;padding:5px">
    <h2 style="color:blanchedalmond;text-align:center;">Sharique's Iris Classification</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    activities=['Linear Regression','Logistic Regression']
    option=st.sidebar.selectbox('Which model would you like to use?',activities)
    st.subheader(option)
    sl=st.slider('Select Sepal Length', 0.0, 10.0)
    sw=st.slider('Select Sepal Width', 0.0, 10.0)
    pl=st.slider('Select Petal Length', 0.0, 10.0)
    pw=st.slider('Select Petal Width', 0.0, 10.0)
    inputs=[[sl,sw,pl,pw]]
    if st.button('Classify'):
        if option=='Linear Regression':
            st.success(classify(lin_model.predict(inputs)))
        else:
            st.success(classify(log_model.predict(inputs))


if __name__=='__main__':
    main()