# import json
# import numpy

# from fastapi import FastAPI
# import uvicorn
# from pydantic import BaseModel

# from fractions import Fraction
# from io import BytesIO
# from typing import Any, Callable, Dict, List, Optional, Tuple, Union

# from qiskit import QuantumCircuit, qpy
# from qiskit.circuit import Parameter
# from qiskit.circuit.library import TwoLocal
# from qiskit.primitives import SamplerResult, EstimatorResult, PrimitiveResult
# from qiskit.qobj import PulseQobj
# from qiskit.quantum_info import Operator, Pauli, SparsePauliOp, Statevector
# from qiskit.result import ProbDistribution, QuasiDistribution
# from qiskit_aer.noise import NoiseModel

# from networkx.classes import Graph


# from answer_data import (
#     challengetest,
    
#     challenge1a,
#     challenge1b,
#     challenge1c,
#     challenge1d,
    
#     challenge2a,
#     challenge2b,
#     challenge2c,
#     challenge2d,
    
#     challenge3a,
#     challenge3b,
#     challenge3c,
#     challenge3d,
#     challenge3e,
#     challenge3f,
    
#     challenge4a,
#     challenge4b,
#     challenge4c,
#     challenge4d,
#     challenge4e,
#     challenge4f,
#     challenge4g,
#     challenge4h,
    
#     challenge5a,
#     challenge5c,
#     challenge5b,
#     challenge5d,
    
#     challenge6a,
#     challenge6b,
#     challenge6c,
#     challenge6d,
#     challenge6e,
# )

# app = FastAPI()

# class Model(BaseModel):
#     answer: Union[Dict, str]
#     username: str

# @app.get("/")
# def hello():
#     return "Welcome to 2024 Qiskit Fall Fest at Korea University"

# @app.post("/answers/{question}")
# async def verify_circuit(question: Union[str, int], request: Model):
#     valid: bool = False
    
#     match question:
#         case "test":
#             valid = challengetest(request)
            
#         case "1a":
#             valid, username = challenge1a(request)
#         case "1b":
#             valid, username = challenge1b(request)
#         case "1c":
#             valid, username = challenge1c(request)
#         case "1d":
#             valid, username = challenge1d(request)

#         case "2a":
#             valid, username = challenge2a(request)
#         case "2b":
#             valid, username = challenge2b(request)
#         case "2c":
#             valid, username = challenge2c(request)
#         case "2d":
#             valid, username = challenge2d(request)

#         case "3a":
#             valid, username = challenge3a(request)
#         case "3b":
#             valid, username = challenge3b(request)
#         case "3c":
#             valid, username = challenge3c(request)
#         case "3d":
#             valid, username = challenge3d(request)
#         case "3e":
#             valid, username = challenge3e(request)
#         case "3f":
#             valid, username = challenge3f(request)
        
#         case "4a":
#             valid, username = challenge4a(request)
#         case "4b":
#             valid, username = challenge4b(request)
#         case "4c":
#             valid, username = challenge4c(request)
#         case "4d":
#             valid, username = challenge4d(request)
#         case "4e":
#             valid, username = challenge4e(request)
#         case "4f":
#             valid, username = challenge4f(request)
#         case "4g":
#             valid, username = challenge4g(request)
#         case "4h":
#             valid, username = challenge4h(request)
            
#         case "5a":
#             valid, username = challenge5a(request)
#         case "5b":
#             valid, username = challenge5b(request)
#         case "5c":
#             valid, username = challenge5c(request)
#         case "5d":
#             valid, username = challenge5d(request)
        
#         case "6a":
#             valid, username = challenge6a(request)
#         case "6b":
#             valid, username = challenge6b(request)
#         case "6c":
#             valid, username = challenge6c(request)
#         case "6d":
#             valid, username = challenge6d(request)
#         case "6e":
#             valid, username = challenge6e(request)
#     print(username)
            
#     if valid:
#         return {"grading_validation": "Valid"}
#     else:
#         return {"grading_validation": "invalid"}
    
# # if __name__ == "__main__" :
# # 	uvicorn.run("main:app", reload=True)

import json
import numpy

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from fractions import Fraction
from io import BytesIO
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from qiskit import QuantumCircuit, qpy
from qiskit.circuit import Parameter
from qiskit.circuit.library import TwoLocal
from qiskit.primitives import SamplerResult, EstimatorResult, PrimitiveResult
from qiskit.qobj import PulseQobj
from qiskit.quantum_info import Operator, Pauli, SparsePauliOp, Statevector
from qiskit.result import ProbDistribution, QuasiDistribution
from qiskit_aer.noise import NoiseModel

from networkx.classes import Graph

import httpx


from answer_data import (
    challengetest,
    
    challenge1a,
    challenge1b,
    challenge1c,
    challenge1d,
    
    challenge2a,
    challenge2b,
    challenge2c,
    challenge2d,
    
    challenge3a,
    challenge3b,
    challenge3c,
    challenge3d,
    challenge3e,
    challenge3f,
    
    challenge4a,
    challenge4b,
    challenge4c,
    challenge4d,
    challenge4e,
    challenge4f,
    challenge4g,
    challenge4h,
    
    challenge5a,
    challenge5c,
    challenge5b,
    challenge5d,
    
    challenge6a,
    challenge6b,
    challenge6c,
    challenge6d,
    challenge6e,
)

import requests
import asyncio
import time


app = FastAPI()
# cache_data = {}

class Model(BaseModel):
    answer: Union[Dict, str]
    username: str

@app.get("/")
def hello():
    return "Welcome to 2024 Qiskit Fall Fest at Korea University"

@app.post("/answers/{question}")
async def verify_circuit(question: Union[str, int], request: Model):
    valid: bool = False
    
    match question:
        case "test":
            valid = challengetest(request)
            
        case "1a":
            valid, username = challenge1a(request)
        case "1b":
            valid, username = challenge1b(request)
        case "1c":
            valid, username = challenge1c(request)
        case "1d":
            valid, username = challenge1d(request)

        case "2a":
            valid, username = challenge2a(request)
        case "2b":
            valid, username = challenge2b(request)
        case "2c":
            valid, username = challenge2c(request)
        case "2d":
            valid, username = challenge2d(request)

        case "3a":
            valid, username = challenge3a(request)
        case "3b":
            valid, username = challenge3b(request)
        case "3c":
            valid, username = challenge3c(request)
        case "3d":
            valid, username = challenge3d(request)
        case "3e":
            valid, username = challenge3e(request)
        case "3f":
            valid, username = challenge3f(request)
        
        case "4a":
            valid, username = challenge4a(request)
        case "4b":
            valid, username = challenge4b(request)
        case "4c":
            valid, username = challenge4c(request)
        case "4d":
            valid, username = challenge4d(request)
        case "4e":
            valid, username = challenge4e(request)
        case "4f":
            valid, username = challenge4f(request)
        case "4g":
            valid, username = challenge4g(request)
        case "4h":
            valid, username = challenge4h(request)
            
        case "5a":
            valid, username = challenge5a(request)
        case "5b":
            valid, username = challenge5b(request)
        case "5c":
            valid, username = challenge5c(request)
        case "5d":
            valid, username = challenge5d(request)
        
        case "6a":
            valid, username = challenge6a(request)
        case "6b":
            valid, username = challenge6b(request)
        case "6c":
            valid, username = challenge6c(request)
        case "6d":
            valid, username = challenge6d(request)
        case "6e":
            valid, username = challenge6e(request)
        
            
     # 채점 결과 계산
    grading_status = "Valid" if valid else "invalid"
    answer = True if valid else False
    
    # #채점 후 결과를 외부 서버로 전송
    # async with httpx.AsyncClient() as client:
    #    response = await client.post(
    #        "https://qff24quick.vercel.app/recieve-data",  # 외부 서버의 엔드포인트 URL
    #        json={"username": username, "question":question ,"grading_validation": grading_status}
    #    )

    flask_url = 'https://qff24quick.vercel.app/receive-data'
    async with httpx.AsyncClient() as client:
        try:
            json_data = {
                "username": username,
                "question": question,
                "answer": answer
            }
            print("Payload:", json_data)  # 요청 데이터 확인
            response = await client.post(
                flask_url,
                json=json_data
            )
            print(f"Response Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")
            print(f"Successed sending data: {response.status_code}")
        except httpx.RequestError as e:
            print(f"Failed sending data: {e}")
    # async with httpx.AsyncClient() as client:
    #     try:
    #         response = await client.post(
    #             flask_url,
    #             json={"username":username, "question":question, "answer": answer}
    #         )
    #         print(response)
    #         print(f"successed sending data: {response.status_code}")
    #     except httpx.RequestError as e:
    #         print(f"failed sending data: {e}")

    #외부 서버 응답 처리
    # if response.status_code == 200:
    #    return {"grading_validation": grading_status}
    # else:
    #    return {"grading_validation": grading_status}
    return {"grading_validation": grading_status}
    
    # if valid:
    #     global cache_data
    #     cache_data = {"username": username, 
    #                   "question": question, 
    #                   "answer": grading_status}
    #     print(cache_data)

    #     return {"grading_validation": "Valid"}
    # else:
    #     return {"grading_validation": "invalid"}
    
# @app.post("/send-data/")
# # 캐시된 데이터를 외부 서버로 보내는 함수
# async def send_data():
#     flask_url = 'https://qff24quick.vercel.app/receive-data'  # Flask 서버의 공용 URL
    
#     while True:
#         # 여기에 캐시된 데이터 (예시: `cache_data`)를 보내는 로직 추가
#         global cache_data
#         async with httpx.AsyncClient() as client:
#             try:
#                 response = await client.post(
#                     flask_url,
#                     json=cache_data
#                 )
#                 print(cache_data)
#                 print(f"데이터 전송 완료: {response.status_code}")
#             except httpx.RequestError as e:
#                 print(f"데이터 전송 실패: {e}")
        
#         # 20초 후에 다시 전송
#         await asyncio.sleep(60)

# 애플리케이션 시작 시 주기적인 작업을 시작하도록 설정
# async def start_sending_data():
#     # 데이터 전송을 주기적으로 시작
#     await send_data()
    

# @app.get("/get")
# async def get_data():
#     if(cache_data == {}):
#         return {"status": "error", "message": "preparing data"}
#     return cache_data
    
if __name__ == "__main__" :
    uvicorn.run("main:app", reload=True)
    # asyncio.run(start_sending_data())