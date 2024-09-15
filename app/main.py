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


from answer_data import challengetest

app = FastAPI()

class Model(BaseModel):
    answer: Union[Dict, str]

@app.get("/")
def hello():
    return "Welcome to 2024 Qiskit Fall Fest at Korea University"

@app.post("/answers/{question}")
async def verify_circuit(question: Union[str, int], request: Model):
    valid: bool = False
    
    if question == "test":
        valid = challengetest(request)
        
    
    
    
    if valid:
        return {"grading_validation": "Valid"}
    else:
        return {"grading_validation": "invalid"}
    
# if __name__ == "__main__" :
# 	uvicorn.run("main:app", reload=True)