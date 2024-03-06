import streamlit as st


class View:
    def __init__(self, repository):
        self.repo = repository

    def to_console(self):
        print(">>> data ***")
        for code, b in self.repo.bonds.items():
            print("id = {} : {}".format(code, str(b)))

    def df_to_console(self):
        print(">>> data df ***")
        print(self.repo.get_df_bonds())

    def to_streamlit(self):
        st.set_page_config(
            page_title=self.repo.config["streamlit_parameters"]["page_title"],
            layout=self.repo.config["streamlit_parameters"]["layout"],
        )

        st.header = self.repo.config["streamlit_parameters"]["header"]

        df_display = self.repo.get_df_bonds()

        st.dataframe(df_display)
