from supabase import create_client, Client
from dotenv import load_dotenv
import os
from datetime import datetime

# -- CREATE TABLE TaskManagement (
# --     TaskId SERIAL PRIMARY KEY,
# --     GitRepositoryUrl TEXT NOT NULL,
# --     TaskStatus TEXT CHECK (TaskStatus IN ('TBD', 'Doing', 'Done')),
# --     LastUpdated TIMESTAMP NOT NULL
# -- );

# -- select * from taskmanagement;
# -- INSERT INTO TaskManagement (GitRepositoryUrl, TaskStatus, LastUpdated)
# -- VALUES ('https://example.com/repo.git', 'TBD', '2024-05-27 12:34:56');




# 加载环境变量
load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# 添加1条数据到TaskManagement表
# 假设TaskManagement表已经存在，并且有相应的字段
insert_data = {
    "gitrepositoryurl": "https://github.com/example/repo",
    "taskstatus": "TBD"
    # "lastupdated" 字段省略以使用默认当前时间戳
}

data, count = supabase.table('taskmanagement').insert(insert_data).execute()

# 查询是否存在 TaskId 为 1 的任务
task_id = 1
response = supabase.table('taskmanagement').select("*").eq('taskid', task_id).execute()

if response.data:
    # 如果存在，更新 TaskId 为 1 的任务
    update_data = {
        "taskstatus": "Doing",
        "lastupdated": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    update_response = supabase.table('taskmanagement').update(update_data).eq('taskid', task_id).execute()
    print(f"TaskId {task_id} updated.")
else:
    print(f"TaskId {task_id} not found.")

# 从TaskManagement表中读取数据
response = supabase.table('taskmanagement').select("*").execute()
for item in response.data:
    print(item)
