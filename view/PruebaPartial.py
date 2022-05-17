public_gsheets_url = "https://docs.google.com/spreadsheets/d/1ZfRATRYeowv__6ZL16hiiHUreFUhwQigkHosozE9hIo/edit?usp=sharing"


def conectbas(st):
    from gsheetsdb import connect

    # Create a connection object.
    conn = connect()

    # Perform SQL query on the Google Sheet.
    # Uses st.cache to only rerun when the query changes or after 10 min.
    @st.cache(ttl=600)
    def run_query(query):
        dat1 = conn.execute(query, headers=1)
        dat = dat1.fetchall()
        return dat

    sheet_url = st.secrets["public_gsheets_url"]
    rows = run_query(f'SELECT * FROM "{sheet_url}"')

    # Print results.
    for row in rows:
        st.write(f"{row.name} has a :{row.pet}:")
