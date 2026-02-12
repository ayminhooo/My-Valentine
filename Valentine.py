import streamlit as st
import random

# Configuration de la page
st.set_page_config(page_title="Question importante", page_icon="❤️")

st.title("Coucou my Chocapic ! ❤️")
st.write("J'ai une question très importante à te poser...Tu veux être ma valentine ???")

# Initialisation de la position du bouton "Non" dans la session
if 'no_pos' not in st.session_state:
    st.session_state.no_pos = (0, 0)

def move_no():
    # On change aléatoirement les marges pour déplacer le bouton
    st.session_state.no_pos = (random.randint(0, 500), random.randint(0, 300))

# Création de deux colonnes
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("OUI ! ✨", type="primary"):
        st.balloons()
        st.success("YAY ! Je savais que tu dirais oui ! ❤️ On se voit le 14 hehehehe")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzRreXp4ZzRreXp4ZzRreXp4ZzRreXp4ZzRreXp4ZzRreZ&ep=v1_gifs_search&rid=giphy.gif&ct=g")

with col2:
    # On utilise du HTML/CSS pour déplacer le bouton "Non" si on clique dessus
    st.button("Non", on_click=move_no)
    
    # Petit message taquin si elle essaie de cliquer sur non
    if st.session_state.no_pos != (0, 0):
        st.write("Oups, ce bouton est en maintenance, il est indisponible pour toujours! Essayes l'autre 😉")
