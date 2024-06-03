from supabase import create_client, Client
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

insert_data = {
    "gitrepositoryurl": "https://github.com/example/repo",
    "taskstatus": "TBD"
}

data, count = supabase.table('taskmanagement').insert(insert_data).execute()

response = supabase.table('taskmanagement').select("*").execute()
for item in response.data:
    print(item)
