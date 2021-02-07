import streamlit as st

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
)

class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })
    

    def run(self):  

        st.sidebar.title('''Football - Social Media Recruiting Assistance''')
        st.sidebar.markdown('''1. Character assessment: The stronger the character, the more attractive a prospect is as a potential candidate.''')
        st.sidebar.markdown('''2. Candidate identification: Find football recruits that GT may not be aware of. For example: athletes interested in Georgia
    Tech, football/related sports, engineering, Atlanta, etc.!''')  



        st.sidebar.title('Navigation')
        app = st.sidebar.radio(
            '',
            self.apps,
            format_func=lambda app: app['title']
        )          

        app['function']()