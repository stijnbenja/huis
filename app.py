import streamlit as st 
import pararius, huurwoningen

st.title('Huizen zoektocht')

para = pararius.haal_op()
huur = huurwoningen.haal_op()

for it in para:
    it['site'] = "Pararius"
    
for it in huur:
    it['site'] = "Huurwoningen"    
    
print(para)

allebei = para + huur

for item in allebei:
    with st.container(border=True):
        cols = st.columns([2,3])
        with cols[0]:
            st.image(item['image_url'])
        with cols[1]:
            st.subheader(item['title'])
            st.write(item['location'])
            st.caption(item['prijs'])
            st.link_button(item['site'],url=item['url'])