from supabase import create_client, Client
from dotenv import load_dotenv
import os
from datetime import datetime



# 加载环境变量
load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

fff = '/Users/a0000/mywork/commonLLM/opensource/nnnew/Transcript-benchmark-quickstart/batchTranslateTosubmit/Aw6DmyhdaSs.zh-Hans.json|'
# 从TaskManagement表中读取数据
# response = supabase.table('batchtaskmanagement').select("*").execute()
response = supabase.table('batchtaskmanagement').select("*").eq('content',fff).execute()
if len(response.data) > 0:
    print("过往已经提交过:" + response.data[0]['batchid'])
