
import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_to_do = st.session_state['new_todo'] + '\n'
    todos.append(new_to_do)
    functions.write_todos(todos)


st.title('My todo App')
st.subheader('This is the subheader.')
st.write('With this app you can manage your todos.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='', placeholder='Add a new todo...',
              on_change=add_todo, key='new_todo')


