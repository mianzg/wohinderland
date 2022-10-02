import streamlit as st
import numpy as np
from model import get_destination, sort_confidence

def generate(button_resp, user_input, form):
    if button_resp:
        if user_input == "":
            st.write("Please write down something to find your destination!")
        else:
            cohere_resp = get_destination(user_input)
            sorted_conf = cohere_resp.confidence
            sort_confidence(sorted_conf)
            with form:
            #show our classification results
                col1, col2 = st.columns(2)
                for no, con in enumerate(sorted_conf):              #display likelihood for each label
                    if no % 2 == 0:                                     # in two columns
                        col1.write(f"{con.label}: {np.round(con.confidence*100, 2)}%")
                        col1.progress(con.confidence)
                    else:
                        col2.write(f"{con.label}: {np.round(con.confidence * 100, 2)}%")
                        col2.progress(con.confidence)
                st.write("How about going to **{}** for your next vacation?".format(sorted_conf[0].label))
                st.image("imgs/{}.jpg".format(sorted_conf[0].label))

def make_prompt(prompt, form):
    k = prompt.split("/n")[0]
    c = st.sidebar.container()
    with c:
        c.write(prompt)
        button = c.button("Try me!", key=k)
        generate(button, prompt, form)

st.title("Wohinderland 🌍")
st.subheader("Destination Finder powered by co:here AI")
form = st.form(key="user_settings")
with form:
    user_input = st.text_area(label="Describe your travel wishes", key="user_input")
    generate_button = form.form_submit_button("Unlock your next wonderland 🚄")
    generate(generate_button, user_input, form)


st.sidebar.header("Demo Prompts 📒")
st.sidebar.caption("Still lost about your next destination? Checkout our prompts to get inspired!")
prompts = ["Prompt 1:\n Buckingham palace",
           "Prompt 2:\n I want to organize a retreat for my student club! Our budget is limited. We are a group of young people loving nature and sustanability. It would also be fun to go somewhere with nice hikes!",
           "Prompt 3:\n Wine, beach, party!"]
for p in prompts:
    make_prompt(p, form)

