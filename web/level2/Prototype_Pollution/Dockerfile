# 使用 Python 3.6 的 Alpine 版本作为基础镜像
FROM python:3.6-alpine

# 复制 requirements.txt 文件并安装依赖
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt

# 将应用代码复制到容器
COPY . /code

# 设置工作目录
WORKDIR /code

# 启动应用
CMD ["python", "src.py"]
