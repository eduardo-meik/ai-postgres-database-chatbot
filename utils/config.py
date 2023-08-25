import streamlit as st
import os


# Set up Postgres database credentials using st.secrets
db_credentials = {
    'dbname'    :   st.secrets["db_credentials"]["PGDATABASE"],
    'user'      :   st.secrets["db_credentials"]["PGUSER"],
    'password'  :   st.secrets["db_credentials"]["PGPASSWORD"],
    'host'      :   st.secrets["db_credentials"]["PGHOST"],
    'port'      :   st.secrets["db_credentials"]["PGPORT"]
}



# Set up OpenAI variables 
OPENAI_API_KEY  =   os.getenv("OPENAI_API_KEY")
AI_MODEL        =   'gpt-3.5-turbo-16k'
# AI_MODEL        =   'gpt-4'



# Max number of tokens permitted within a conversation exchange via OpenAI API
MAX_TOKENS_ALLOWED      =   3000


# Max number of messages to exchange with OpenAI API
MAX_MESSAGES_TO_OPENAI  =   5



# An arbitrary number to provide a buffer to avoid reaching exact token limits
TOKEN_BUFFER            =   100  
