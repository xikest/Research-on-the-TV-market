import os
import time
import pickle
from datetime import datetime


def makeDir(folder_path):
    # 현재 작업 디렉토리 기준으로 상대 경로 설정
    relative_path = folder_path.split("/")
    # 폴더 생성을 위해 순차적으로 경로 조합
    current_path = os.getcwd()
    for folder_name in relative_path:
        current_path = os.path.join(current_path, folder_name)
        # 폴더가 존재하지 않을 경우에만 폴더 생성
        if not os.path.exists(current_path):
            os.makedirs(current_path)
            print(f"폴더 '{folder_name}'가 생성되었습니다.")
        # else:
            # print(f"폴더 '{folder_name}'가 이미 존재합니다.")


def waitingPage(sec:int=5):
    time.sleep(sec) # 웹 페이지 대기
    return None

def backUp(data, filename:str="backup"):
    # 데이터 저장
    with open(f"{filename}.pickle", "wb") as file:
        pickle.dump(data, file)
    # 데이터 불러오기
    with open(f"{filename}.pickle", "rb") as file:
        data = pickle.load(file)
    return data

def get_time():# 현재 시간 얻기
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def get_today():
    return datetime.today().strftime("%Y-%m-%d")

def getNamefromURL(url):
    """
    마지막 / 이후 문자만 가져 옴
    """
    return url.rsplit('/', 1)[-1]




