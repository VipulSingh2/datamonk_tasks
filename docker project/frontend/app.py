import streamlit as st
import requests
from dotenv import load_dotenv
import os


load_dotenv()

API_URL = os.getenv(
    "API_URL",
    "http://localhost:8000"
).rstrip("/")


st.set_page_config(
    page_title="Task Manager",
    page_icon="📝",
    layout="centered"
)



def create_task(title, description, is_completed):

    response = requests.post(
        f"{API_URL}/tasks/create",
        json={
            "title": title,
            "description": description,
            "is_completed": is_completed
        }
    )

    return response




def get_all_task():

    response = requests.get(
        f"{API_URL}/tasks/all_tasks"
    )

    return response


def get_one_task(task_id):

    response = requests.get(
        f"{API_URL}/tasks/one_task/{task_id}"
    )

    return response


def delete_task(task_id):

    response = requests.delete(
        f"{API_URL}/tasks/delete_task/{task_id}"
    )

    return response

def update_task(task_id,title,description,is_completed):
    response = requests.put(
        f"{API_URL}/tasks/update_task/{task_id}",
        json={
            "title":title,
            "description":description,
            "is_completed":is_completed
        }
    )
    return response

st.title("📝 Task Manager")

st.caption("Streamlit frontend powered by FastAPI")



col1,col2 = st.columns(2)
with col1:
    with st.form(key="create"):
        title = st.text_input(label="Enter your title here")
        description = st.text_input(label="Enter your description here")
        is_complted = st.checkbox(label ="completed")
        submit= st.form_submit_button(label="create_task",type="primary",use_container_width=True)
        if submit:
            response = create_task(title,description,submit)
            st.write(response)

with col2:        
    with st.form(key="update"):
        task_id = st.number_input(label="Enter the task id",step=1,value=1)
        title = st.text_input(label="Enter your title here")
        description = st.text_input(label="Enter your description here")
        is_complted = st.checkbox(label ="completed")
        submit= st.form_submit_button(label="update_task",type="primary",use_container_width=True)
        if submit:
            response = update_task(task_id,title,description,submit)
            st.write(response)
st.header("📋 All Tasks")

if st.button("Fetch All Tasks"):

    response = get_all_task()

    if response.status_code == 200:

        tasks = response.json()

        # st.json(tasks)
        for task in tasks:
            st.write(task)

    else:

        st.error(
            f"Error {response.status_code}: {response.text}"
        )


       
col1,col2 = st.columns(2)

with col1:
    st.header("🔍 Find Task")

    task_id = st.number_input(
                "Enter Task ID",
                min_value=1,
                step=1
            )

    if st.button("Fetch Task"):

        response = get_one_task(task_id)

        if response.status_code == 200:

            task = response.json()

            st.json(task)

        else:

            st.error(
                        f"Error {response.status_code}: {response.text}"
                    )


                
with col2:
    st.header("🗑️ Delete Task")

    delete_id = st.number_input(
                        "Enter Task ID to delete",
                        min_value=1,
                        step=1
                    )

    if st.button("Delete Task"):

        response = delete_task(delete_id)

        if response.status_code == 204:

            st.success("Task deleted successfully!")

        elif response.status_code == 404:

            st.warning("Task not found.")

        else:

            st.error(
                    f"Error {response.status_code}: {response.text}"
                )
