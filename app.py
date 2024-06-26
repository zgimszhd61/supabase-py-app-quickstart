from supabase import create_client, Client
from dotenv import load_dotenv
import os

## 其中supabase的url和key在这里获得：项目地址如 https://supabase.com/dashboard/project/zcxjeufomtswakwdqugv -> connect -> app framework

# CREATE TABLE IF NOT EXISTS customusers (
#     id serial PRIMARY KEY,
#     username text UNIQUE NOT NULL,
#     password text NOT NULL
# );

load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

data, count = supabase.table('customusers').insert({"username": 'aa', "password": "fbbaaa"}).execute()

response = supabase.table('customusers').select("*").execute()
for item in response:
    try:
        for mmm in item[1]:
           print(mmm)
    except:
        print("ERROR")