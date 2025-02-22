import streamlit as st
import tensorflow as tf
import numpy as np


#Tensorflow Model Precision
def model_prediction(test_image):
    model= tf.keras .models.load_model('trainnew_model_fixed.h5')
    image =tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr=tf.keras.preprocessing.image.img_to_array(image)
    input_arr=np.array([input_arr]) #convert single image to batch
    prediction= model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index


#sidebar
st.sidebar.title("dashboard")
app_mode= st.sidebar.selectbox("Select Page",["Home","About","Leaf Health Detection"])

#home page
if(app_mode=="Home"):
    st.header("LEAF HEALTH DETECTION")
    image_path="home_page.jpeg"
    st.image(image_path,use_column_width=True)
    st.markdown("""
# Leaf Health Detection

## Introduction

Leah Health Detection is an advanced system designed to analyze and predict health conditions using machine learning techniques. By leveraging TensorFlow and Streamlit, this project aims to provide accurate and accessible health diagnostics. 

## Features

- **Real-time Health Analysis**: Processes user input to generate insightful health predictions.
- **Machine Learning Integration**: Utilizes trained models for accurate diagnostics.
- **User-Friendly Interface**: Built with Streamlit to ensure seamless user experience.
- **Scalable and Efficient**: Designed to handle large datasets for improved accuracy.

## Technology Stack

- **Python 3.10**
- **TensorFlow (<2.11)**
- **Streamlit**
- **Protobuf**
- **NumPy (<2.0)**

## Goal

The goal of Leah Health Detection is to assist users in understanding potential health risks and conditions through data-driven analysis, ultimately contributing to proactive healthcare management.


    """)

    #About page
if app_mode == "About":
    st.header("About")
    st.markdown("""
        # About Dataset  
        
        **Acknowledgements**  
        This dataset was obtained from spMohanty's GitHub Repo.  
        
        **Inspiration**  
        This dataset was created for use in my Plant Disease Detection System.  
    """)
#prediction on page
elif app_mode == "Leaf Health Detection":
    st.header("Leaf Health Detection")
    
    # File uploader
    test_image = st.file_uploader("Choose an Image:", type=["jpg", "png", "jpeg"])
    
    # Ensure a file is uploaded before proceeding
    if test_image is not None:
        st.image(test_image, caption="Uploaded Image", use_column_width=True)

    if(st.button("Show Image")):
        st.image(test_image,use_column_width=True)

     #predict button
    if(st.button("Predict")):
       
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
       #define class
        class_name = ['healthy', 'unhealthy']
        st.success(" It is {} leaf ".format(class_name[result_index]))
