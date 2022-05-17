


def conectbas(st):
    # streamlit_app.py

    import streamlit as st
    from gsheetsdb import connect
    # Create a connection object.
    conn = connect()

    # Perform SQL query on the Google Sheet.
    # Uses st.cache to only rerun when the query changes or after 10 min.
    @st.cache(ttl=600)
    def run_query(query):
        dat = conn.execute(query, headers=1)
        dats = dat.fetchall()
        return dats

    sheet_url = st.secrets["public_gsheets_url"]
    rows = run_query(f'SELECT * FROM "{sheet_url}"')

    # Print results.
    for row in rows:
        st.write(f"{row.nombre} has a :{row.tipo}:")