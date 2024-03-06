from repository import Repository
import view


def main():
    repo = Repository()
    v = view.View(repo)
    v.to_console()
    v.df_to_console()
    v.to_streamlit()


if __name__ == "__main__":
    main()
