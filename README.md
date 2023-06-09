# 如何启动

## 安装redis stack及docker
我们将使用 Redis 作为文档内容和向量嵌入的数据库。您需要完整的 Redis Stack 才能启用 Redisearch，这是允许语义搜索的模块 - 更多详细信息请参阅 Redis Stack 的文档。

要在本地设置这个环境，您需要执行以下操作：

为您的操作系统安装适当版本的 Docker
确保 Docker 正在运行，例如，通过运行 docker run hello-world
运行以下命令：docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest。

## 使用venv环境启动streamlit

- Set up a virtual environment with pip by running ```virtualenv venv``` (ensure ```virtualenv``` is installed).
- Activate the environment by running ```source venv/bin/activate```.
- Install requirements by running ```pip install -r requirements.txt```.
- Run ```streamlit run chatbot.py``` to fire up the Streamlit app in your browser.

有许多未尽的说明，详情参考openai-cookbook: https://github.com/openai/openai-cookbook/tree/main/apps/enterprise-knowledge-retrieval

# 如何建索引
参见chatconfluence.ipynb notebook

# 其他问题
关于如何使用notebook，如何使用python，如何使用virtualenv 请去咨询chatgpt
