import json
import numpy

from fractions import Fraction
from io import BytesIO
from typing import Any, Union

from qiskit import QuantumCircuit, qpy
from qiskit.circuit import Parameter
from qiskit.circuit.library import TwoLocal
from qiskit.primitives import SamplerResult, EstimatorResult, PrimitiveResult
from qiskit.qobj import PulseQobj
from qiskit.quantum_info import Operator, Pauli, SparsePauliOp, Statevector
from qiskit.result import ProbDistribution, QuasiDistribution
from qiskit_aer.noise import NoiseModel

from networkx.classes import Graph

def bytes_to_circuit(circuit_str: str) -> QuantumCircuit:
    # ISO-8859-1로 인코딩된 문자열을 다시 바이트로 변환
    circuit_bytes = circuit_str.encode('ISO-8859-1')
    
    # BytesIO를 사용하여 바이트 스트림을 읽고 qpy.load로 QuantumCircuit 객체로 변환
    with BytesIO(circuit_bytes) as container:
        qc = qpy.load(container)
    
    return qc

def load_quantum_circuit(obj: json):
    load_circuit = obj
    load_circuit = load_circuit['qc']
    restored_circuit = bytes_to_circuit(load_circuit)
    return restored_circuit[0] # unlist