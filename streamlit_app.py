import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))

st.title("Tipping Predictor for Airbnb Listings")
st.markdown(
    "The dataset contains modifications with regards to the original for illustrative & learning purposes"
)
st.text("This widget can be used by Airbnb hosts to check their expected tips for a listing.")

# review_scores_rating: 0 to 5
review_scores_rating = st.slider('What is the listing rating?', 0.00, 5.00, 4.50)
# room_type: ['Shared room', 'Private room', 'Hotel room', 'Entire home/apt']
room_type = st.radio(
    "What is the room type of your listing?",
    ('Shared room', 'Private room', 'Hotel room', 'Entire home/apt'))
# service_cost: ['$0.99', '$4.99', '$2.99', '$10.99']
service_cost = st.radio(
    "What will be the service cost of your listing?",
    ('$0.99', '$2.99', '$4.99', '$10.99'))
# instant_bookable: 0, 1
instant_bookable = st.radio(
    "Is the listing instantly bookable?",
    ("True", "False"))
instant_bookable = 1 if instant_bookable == "True" else 0

example = pd.DataFrame({
    "review_scores_rating": [review_scores_rating],
    "room_type": [room_type],
    "service_cost": [service_cost],
    "instant_bookable": [instant_bookable]
    })

if st.button('Predict?'):
    st.write("The model predicts that the tipping for this listing is:", model.predict(example)[0])
