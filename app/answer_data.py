import json
import numpy
from pydantic import BaseModel

from fractions import Fraction
from io import BytesIO
from typing import Any, Union, Dict

from qiskit import QuantumCircuit, qpy
from qiskit.circuit import Parameter
from qiskit.circuit.library import TwoLocal
from qiskit.primitives import SamplerResult, EstimatorResult, PrimitiveResult
from qiskit.qobj import PulseQobj
from qiskit.quantum_info import Operator, Pauli, SparsePauliOp, Statevector
from qiskit.result import ProbDistribution, QuasiDistribution
from qiskit_aer.noise import NoiseModel
from qiskit.quantum_info import Operator

from networkx.classes import Graph

from custom_decoder.deserializer import load_quantum_circuit

class Model(BaseModel):
    answer: Union[Dict, str]
    
def challengetest(candidate: Model):
    candidate = candidate.answer # qff_ku2024_grader 라이브러리에 정의된 grade 함수의 입력으로 payload가 들어감. payload = {'answer': serialized_answer} 와 같은 형식임. main.py의 verify_circuit 함수에서 Model 객체를 올바르게 처리할 수 있도록 해야함. Model 객체는 FastAPI가 자동으로 JSON 요청 본문을 파싱하여 전달해 주므로, request 매개변수를 직접 사용하면 됨.
    candidate_qc = load_quantum_circuit(candidate)
    
    answer_qc = QuantumCircuit(4,4)
    answer_qc.measure([0,1,2,3],[0,1,2,3])
    
    # op1 = Operator(candidate_qc)
    # op2 = Operator(answer_qc)

    # return op1.equiv(op2)
    
    return candidate_qc == answer_qc