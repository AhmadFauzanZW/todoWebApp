import streamlit as st
import functions

filepath = 'TodoLists.txt'

todos = functions.imporData(filepath)

def tambah_todo():
    # Check if the input is not empty
    if st.session_state['todo']:
        todo = st.session_state['todo'] + '\n'
        todos.append(todo)
        functions.eksporData(filepath, todos)
        # Clear the input field
        st.session_state['todo'] = ''

st.title("Todo List Program")
st.subheader("By Ahmad Fauzan")
st.divider()

with st.container(border=True):
    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(index)
            functions.eksporData(filepath, todos)
            del st.session_state[todo]
            st.rerun()

st.divider()

st.text_input(label='Masukkan Todo:', placeholder="Ex. Debugging Code", key='todo',
              on_change=tambah_todo)

st.warning("Harap masukkan todo yang berbeda. Jangan masukkan todo yang sama!")