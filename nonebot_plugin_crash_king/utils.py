import aiohttp
import hashlib
import os
import zipfile

from nonebot import logger

current_directory = os.path.dirname(os.path.abspath(__file__))

async def download_file(url, filename) -> bool:
    logger.info(f'正在下载 {url} 到 {filename}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            if response.status == 200:
                with open(filename, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f.write(chunk)
                logger.info(f'文件已下载并保存为 {filename}')
                return True
            else:
                logger.error(f'下载失败，HTTP 状态码：{response.status}')
                return False

def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    logger.info(f"解压完成到 {extract_to}")

def check_files(directory):
    """List files in directory"""
    for root, dirs, files in os.walk(directory):
        for file in files:
            logger.info(f"Found file: {file}")
        for dir in dirs:
            logger.info(f"Found directory: {dir}")

def load_reply(file_path):
    reply_directory = os.path.join(current_directory, 'replies')
    reply_path = os.path.join(reply_directory, file_path)

    fileTemp = open(reply_path, mode='r', buffering=-1, encoding="utf-8")
    result = fileTemp.read()
    fileTemp.close()
    return result

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()