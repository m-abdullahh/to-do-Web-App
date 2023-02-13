import streamlit as st
import functions
import time

todos = functions.read_file()


def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo + '\n')
    functions.write_file(todos)


# st.write(time.strftime(" %b %d,%Y  -_-  %H:%M:%S"))
st.title("To-do App")
st.subheader("This is my todo Text")
st.write("This App is to increase your productivity")

for todo in todos:
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(todos.index(todo))
        functions.write_file(todos)
        del st.session_state[todo]
        st._rerun()
st.text_input('', "Add new to-do...",
              on_change=add_todo, key="new_todo")

