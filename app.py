import streamlit as st
import pandas as pd

df = pd.read_csv("prueba.csv")
df2 = df.sample(random_state=42)

def main():
    st.header("Dataframe: ")
    st.dataframe(df.style.highlight_max(axis=0), use_container_width=True)
    
if __name__ == "__main__":
    main()