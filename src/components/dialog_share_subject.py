import streamlit as st
import segno
import io


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name,subject_code):
    app_domain  = "snap2attend-main.streamlit.app"
    join_url   = f"{app_domain}/?join-code={subject_code}"

    st.header("Scan to Join")

    qr = segno.make(join_url)    # make the qr for the given link

    out = io.BytesIO()           # make the temporry file in the RAM, not on disk
    qr.save(out , kind ='png' , scale = 10 , border = 1)    # saving the qr in that temporary file

    col1,col2 = st.columns(2)

    with col1:
        st.markdown("### Copy Link")
        st.code(join_url, language='text')                   # Display the given url or string in copy style
        st.code(subject_code, language='text')    
        st.info('Copy this link to share on Whatsapp or email')

    with col2:
        st.markdown('### Scan to join')
        st.image(out.getvalue() , caption="QRCode for class joining")    