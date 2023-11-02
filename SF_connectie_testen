import snowflake.connector
import streamlit as st

# Streamlit-applicatie
st.title('Snowflake Connection Test')

# Verbinden met Snowflake-database
connection = snowflake.connector.connect(
    user='MOHAMED.EL.AZZATI@PGGM.NL',
    password='Voorjaar2022!',
    account='do23676.west-europe.azure',
    warehouse='__CORE'
)

# Functie om gegevens op te halen
def get_data():
    cursor = connection.cursor()
    cursor.execute('SELECT CURRENT_TIMESTAMP() AS now')
    data = cursor.fetchall()
    cursor.close()
    return data

# Voer de functie uit om gegevens op te halen
data = get_data()

# Toon de resultaten in de Streamlit-app
st.write('Query result:')
st.write(data)

# Sluit de Snowflake-verbinding bij het sluiten van de app
connection.close()
