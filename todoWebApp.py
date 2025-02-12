import streamlit as st
import functions

filepath = 'TodoLists.txt'
todos = functions.imporData(filepath)

def tambah_todo():
    if st.session_state['todo']:
        todo = st.session_state['todo'] + '\n'
        # Check if todo already exists (ignoring newlines and spaces)
        if todo.strip() in [existing.strip() for existing in todos]:
            st.error("Todo ini sudah ada dalam daftar! Silakan masukkan todo yang berbeda.")
        else:
            todos.append(todo)
            functions.eksporData(filepath, todos)
            st.session_state['todo'] = ''

st.title("Todo List Program")
st.subheader("By Ahmad Fauzan")
st.divider()

with st.container(border=True):
    for index, todo in enumerate(todos):
        # Use index as part of the key to ensure uniqueness
        checkbox = st.checkbox(todo, key=f"todo_{index}")
        if checkbox:
            todos.pop(index)
            functions.eksporData(filepath, todos)
            # Use the same key format when deleting from session state
            del st.session_state[f"todo_{index}"]
            st.rerun()

st.divider()

st.text_input(label='Masukkan Todo:', placeholder="Ex. Debugging Code", key='todo',
              on_change=tambah_todo)