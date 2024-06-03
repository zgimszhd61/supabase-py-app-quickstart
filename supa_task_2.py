from supabase import create_client, Client
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# 检查TaskManagement表是否存在，如果不存在则创建表
create_table_sql = """
CREATE TABLE IF NOT EXISTS TaskManagement (
    TaskId SERIAL PRIMARY KEY,
    GitRepoUrl TEXT NOT NULL,
    TaskStatus TEXT CHECK (TaskStatus IN ('TBD', 'Doing', 'Done')),
    LastUpdateTime TIMESTAMP NOT NULL
);
"""
supabase.query(create_table_sql).execute()

# 添加1条数据到TaskManagement表
insert_data = {
    "GitRepoUrl": "https://github.com/example/repo",
    "TaskStatus": "TBD",
    "LastUpdateTime": "2024-05-27 19:43:00"
}
data, count = supabase.table('TaskManagement').insert(insert_data).execute()

# 从TaskManagement表中读取数据
response = supabase.table('TaskManagement').select("*").execute()
for item in response.data:
    print(item)