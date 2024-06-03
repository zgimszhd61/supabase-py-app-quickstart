from supabase import create_client, Client
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# 插入一条数据到 TaskManagement 表
task_data = {
    "GitRepositoryUrl": "https://github.com/example/repo",
    "TaskStatus": "TBD",
}

data, count = supabase.table('TaskManagement').insert(task_data).execute()

# 从 TaskManagement 表中读取数据
response = supabase.table('TaskManagement').select("*").execute()
for item in response.data:
    try:
        print(item)
    except Exception as e:
        print("ERROR:", e)
