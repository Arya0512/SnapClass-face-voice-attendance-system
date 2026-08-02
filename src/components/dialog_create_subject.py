import streamlit as st
from src.database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of Subject")
    subject_code=st.text_input("Subject Code",placeholder="CS101")
    subject_name=st.text_input("Subject Name",placeholder="Enter subject name")
    section=st.text_input("Section",placeholder="Enter the section")

    st.space()
    if st.button("Create Subject Now",width="stretch"):
        if subject_code and subject_name and section:
            try:
                create_subject(subject_code,subject_name,section,teacher_id)
                st.toast("Successfully created subject")
                st.rerun()
            except Exception as e:
                st.write(f"{e}")
        else:
            st.write("Please fill all field")