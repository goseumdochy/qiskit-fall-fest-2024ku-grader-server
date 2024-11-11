import json
import numpy
from pydantic import BaseModel

from fractions import Fraction
from io import BytesIO
from typing import Any, Union, Dict

from qiskit import QuantumCircuit, qpy, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter
from qiskit.circuit.library import TwoLocal
from qiskit.primitives import SamplerResult, EstimatorResult, PrimitiveResult
from qiskit.qobj import PulseQobj
from qiskit.quantum_info import Operator, Pauli, SparsePauliOp, Statevector
from qiskit.result import ProbDistribution, QuasiDistribution
from qiskit_aer.noise import NoiseModel
from qiskit.quantum_info import Operator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime.fake_provider import FakeTorino

from networkx.classes import Graph

from custom_decoder.deserializer import load_quantum_circuit

from custom_encoder.json_encoder import to_json


class Model(BaseModel):
    answer: Union[Dict, str]
    username: str
    
def challengetest(candidate: Model):
    candidate = json.loads(candidate.answer) # qff_ku2024_grader 라이브러리에 정의된 grade 함수의 입력으로 payload가 들어감. payload = {'answer': serialized_answer} 와 같은 형식임. main.py의 verify_circuit 함수에서 Model 객체를 올바르게 처리할 수 있도록 해야함. Model 객체는 FastAPI가 자동으로 JSON 요청 본문을 파싱하여 전달해 주므로, request 매개변수를 직접 사용하면 됨.
    candidate_qc = load_quantum_circuit(candidate)
    
    answer_qc = QuantumCircuit(4,4)
    answer_qc.measure([0,1,2,3],[0,1,2,3])
    
    # op1 = Operator(candidate_qc)
    # op2 = Operator(answer_qc)

    # return op1.equiv(op2)
    
    return candidate_qc == answer_qc

def challenge1a(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    
    return candidate.__class__==str, username


def challenge1b(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    candidate_qc = load_quantum_circuit(candidate)
    
    answer_qc = QuantumCircuit(2)
    answer_qc.h(0)
    answer_qc.cx(0, 1)
    
    sv_candidate = Statevector(candidate_qc)
    sv_answer = Statevector(answer_qc)
    
    return sv_candidate.equiv(sv_answer), username
    
    
def challenge1c(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    
    ZZ = SparsePauliOp('ZZ')
    ZI = SparsePauliOp('ZI')
    IX = SparsePauliOp('IX')
    IZ = SparsePauliOp('IZ')
    XX = SparsePauliOp('XX')
    XI = SparsePauliOp('XI')
    
    answer = [IZ, IX, ZI, XI, ZZ, XX]
    answer = json.loads(to_json(answer)) # candidate가 참가자들 grader에서 to_json을 거친 후 여기 위에서 json.loads를 거쳤기에 똑같이 맞춰줌
    return answer == candidate, username


def challenge1d(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)

    # candidate[0] 인 QuantumCircuit 부터 확인
    candidate_qc = load_quantum_circuit(candidate[0])
    
    answer_qc = QuantumCircuit(2)
    answer_qc.h(0)
    answer_qc.cx(0, 1)
    
    op_candidate = Operator(candidate_qc)
    op_answer = Operator(answer_qc)
    
    check1 = op_candidate.equiv(op_answer)
    
    # candidate[1] 은 observable
    
    ZZ = SparsePauliOp('ZZ')
    ZI = SparsePauliOp('ZI')
    IX = SparsePauliOp('IX')
    IZ = SparsePauliOp('IZ')
    XX = SparsePauliOp('XX')
    XI = SparsePauliOp('XI')
    
    answer_obs = [IZ, IX, ZI, XI, ZZ, XX]
    answer_obs = json.loads(to_json(answer_obs))
    
    check2 = answer_obs == candidate[1]
    
    return check1 and check2, username
    

### challenge2 ###

def challenge2a(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    candidate_qc = load_quantum_circuit(candidate)
    
    answer_qc = QuantumCircuit(2)
    answer_qc.h(0)
    answer_qc.cx(0, 1)
    answer_qc.x(1)
    answer_qc.z(1)
    
    sv_candidate = Statevector(candidate_qc)
    sv_answer = Statevector(answer_qc)
    
    return sv_candidate.equiv(sv_answer), username
    

def challenge2b(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    
    check1 = candidate['metadata']['shots'] == 10000
    check2 = set(candidate['counts'].keys()) == {'10', '01'}
    
    return check1 and check2, username

def challenge2c(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    candidate_qc = load_quantum_circuit(candidate)
    
    answer_qc = QuantumCircuit(3)
    answer_qc.ry(1.91063324, 0)
    answer_qc.ch(0, 1)
    answer_qc.cx(1, 2)
    answer_qc.cx(0, 1)
    answer_qc.x(0)
    
    sv_candidate = Statevector(candidate_qc)
    sv_answer = Statevector(answer_qc)
    
    return sv_candidate.equiv(sv_answer, rtol=1e-10), username
    
def challenge2d(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    
    check1 = candidate['metadata']['shots'] == 10000
    check2 = set(candidate['counts'].keys()) == {'100', '010', '001'}
    
    return check1 and check2, username

### challenge3 ###

def challenge3a(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    
    answer = {}
    answer["init"] = "C"
    answer["layout"] = "D"
    answer["routing"] = "B"
    answer["translation"] = "F"
    answer["optimization"] = "A"
    answer["scheduling"] = "E"
    
    return answer == candidate, username

def challenge3b(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)

    answer = [21, 3, 5, 3]
    
    return answer == candidate, username

def challenge3c(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)

    answer = [29, 4, 5, 5]
    
    return answer == candidate, username

def challenge3d(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    
    answer = [37, 10, 4, 5]
    
    return answer == candidate, username

def challenge3e(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    seed = 10000
    backend = FakeTorino()

    answer = [33, 10, 4, 5]
    
    return answer == candidate, username

def challenge3f(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    
    circuit_depths = {
        'opt_lv_0': 327,
        'opt_lv_1': 205,
        'opt_lv_2': 157,
        'opt_lv_3': 157,
    }
    gate_counts = {
        'opt_lv_0': 566,
        'opt_lv_1': 303,
        'opt_lv_2': 251,
        'opt_lv_3': 251,
    }

    scores = {
        'opt_lv_0': 1547,
        'opt_lv_1': 933,
        'opt_lv_2': 806,
        'opt_lv_3': 806,
    }
    
    answer = [circuit_depths, gate_counts, scores]
    
    return answer == candidate, username

### challenge4 ###

def challenge4a(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    candidate_qc = load_quantum_circuit(candidate)
    
    qr = QuantumRegister(2, name = "q")
    cr = ClassicalRegister(2, name = "b")
    qc = QuantumCircuit(qr, cr)

    q0, q1 = qr
    b0, b1 = cr

    qc.h(q0)
    qc.measure(q0, b0)


    ### Write your code below this line ### 
    with qc.if_test((b0, 0)) as else_:
        # if the condition is satisfied (b0 == 1), then flip the bit back to 0
        qc.x(q1)

    with else_:
        # if the condition is satisfied (b0 != 1), then apply identity operator to 0
        qc.h(q1)
    ### Do not change the code below this line ###


    qc.measure(q1, b1)
    answer = qc
    
    return candidate_qc == answer, username

def challenge4b(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    answer = {'00': 0, '01': 1/4, '10': 1/2, '11': 1/4}
    
    return answer == candidate, username

def challenge4c(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    candidate_qc = load_quantum_circuit(candidate)
        
    qubits = QuantumRegister(3, name='Keep')
    clbits = ClassicalRegister(3, name='Going')
    circuit = QuantumCircuit(qubits, clbits)
    
    q0, q1, q2 = qubits
    c0, c1, c2 = clbits

    ### Write your code below this line ### 

    circuit.h([q0, q1])
    circuit.measure(q0, c0)
    circuit.measure(q1, c1)
    with circuit.while_loop((clbits, 0b11)):
        circuit.h([q0, q1])
        circuit.measure(q0, c0)
        circuit.measure(q1, c1)

    with circuit.switch(clbits) as case:
        with case(0b000, 0b010):
            circuit.h(q2)
            with circuit.for_loop(range(10)) as i:
                circuit.x(q2)
                circuit.measure(q2, c2)
                with circuit.if_test((c2, 1)):
                    circuit.break_loop()
        with case(0b001):
            circuit.y(q2)
        with case(case.DEFAULT):
            circuit.x(q2)
    
    circuit.measure(q2, c2)
 
    answer = circuit.copy()
    
    return answer == candidate_qc, username

def challenge4d(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    
    answer = {'000': 0, '001': 0, '010': 0, '011': 0, '100': 1/3, '101': 1/3, '110': 1/3, '111': 0}

    return candidate == answer, username

def challenge4e(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    candidate_qc = load_quantum_circuit(candidate)
    
    controls = QuantumRegister(2, name="control")
    target = QuantumRegister(1, name="target")

    mid_measure = ClassicalRegister(2, name="mid")
    final_measure = ClassicalRegister(1, name="final")

    base = QuantumCircuit(controls, target, mid_measure, final_measure)
    
    answer_qc = base.copy_empty_like()
    answer_qc.h([0,1,2])
    answer_qc.ccx(0,1,2)
    answer_qc.s(2)
    answer_qc.ccx(0,1,2)
    answer_qc.h([0,1,2])
    answer_qc.measure([0,1],[0,1])
    
    return answer_qc == candidate_qc, username
    

def challenge4f(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    canddiate_qc = load_quantum_circuit(candidate)
    
    controls = QuantumRegister(2, name="control")
    target = QuantumRegister(1, name="target")

    mid_measure = ClassicalRegister(2, name="mid")
    final_measure = ClassicalRegister(1, name="final")

    base = QuantumCircuit(controls, target, mid_measure, final_measure)
    
    answer_qc = base.copy_empty_like()
    answer_qc.h([0,1,2])
    answer_qc.ccx(0,1,2)
    answer_qc.s(2)
    answer_qc.ccx(0,1,2)
    answer_qc.h([0,1,2])
    answer_qc.measure([0,1],[0,1])
    
    with answer_qc.if_test((mid_measure[0], 0b1)):
        answer_qc.x(0)
    with answer_qc.if_test((mid_measure[1], 0b1)):
        answer_qc.x(1)
    
    return answer_qc == canddiate_qc, username
    

def challenge4g(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    candidate_qc = load_quantum_circuit(candidate)
    
    controls = QuantumRegister(2, name="control")
    target = QuantumRegister(1, name="target")

    mid_measure = ClassicalRegister(2, name="mid")
    final_measure = ClassicalRegister(1, name="final")

    base = QuantumCircuit(controls, target, mid_measure, final_measure)
    
    answer_qc = base.copy_empty_like()
    
    answer_qc.h([0,1,2])
    answer_qc.ccx(0,1,2)
    answer_qc.s(2)
    answer_qc.ccx(0,1,2)
    answer_qc.h([0,1,2])
    answer_qc.measure([0,1],[0,1])
    
    with answer_qc.if_test((mid_measure[0], 0b1)):
        answer_qc.x(0)
    with answer_qc.if_test((mid_measure[1], 0b1)):
        answer_qc.x(1)
        
    with answer_qc.while_loop(([final_measure, 0b0])):
        with answer_qc.if_test((mid_measure, 0b00)):
            answer_qc.break_loop()
        answer_qc.x(target)
        
        answer_qc.h([0,1,2])
        answer_qc.ccx(0,1,2)
        answer_qc.s(2)
        answer_qc.ccx(0,1,2)
        answer_qc.h([0,1,2])
        answer_qc.measure([0,1],[0,1])
        
        with answer_qc.if_test((mid_measure[0], 0b1)):
            answer_qc.x(0)
        with answer_qc.if_test((mid_measure[1], 0b1)):
            answer_qc.x(1)
            
    answer_qc.measure(controls, mid_measure)
    answer_qc.measure(target, final_measure)
    
    return candidate_qc == answer_qc, username
    

def challenge4h(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    
    answer = {'0': 4/5, '1': 1/5}
    
    return answer == candidate, username

### challenge5 ###

def challenge5a(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    candidate_qc = load_quantum_circuit(candidate)
    
    qubit_A = QuantumRegister(1, name="A")
    qubit_B = QuantumRegister(1, name="B")

    final_measure = ClassicalRegister(2, name="final")

    base = QuantumCircuit(qubit_A, qubit_B, final_measure)
    
    answer_qc = base.copy_empty_like()
    answer_qc.h(0)
    answer_qc.cx(0, 1)
    
    sv_candidate = Statevector(candidate_qc)
    sv_answer = Statevector(answer_qc)
    
    return sv_candidate.equiv(sv_answer), username

def challenge5b(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    candidate_list = [load_quantum_circuit(candidate[i]) for i in range(4)]
    
    qubit_A = QuantumRegister(1, name="A")
    qubit_B = QuantumRegister(1, name="B")

    final_measure = ClassicalRegister(2, name="final")

    base = QuantumCircuit(qubit_A, qubit_B, final_measure)
    
    qc00 = base.copy_empty_like()
    qc01 = base.copy_empty_like()
    qc10 = base.copy_empty_like()
    qc11 = base.copy_empty_like()
    
    qc01.x(0)
    qc10.z(0)
    qc11.x(0)
    qc11.z(0)
    
    answer_list = [qc00, qc01, qc10, qc11]
    
    return answer_list == candidate_list, username
    

def challenge5c(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    candidate_qc = load_quantum_circuit(candidate)
    
    qubit_A = QuantumRegister(1, name="A")
    qubit_B = QuantumRegister(1, name="B")

    final_measure = ClassicalRegister(2, name="final")

    base = QuantumCircuit(qubit_A, qubit_B, final_measure)
    
    answer_qc = base.copy_empty_like()
    
    answer_qc.cx(0, 1)
    answer_qc.h(0)
    
    answer_qc.measure([0,1], [1,0])
    
    return answer_qc == candidate_qc, username
    

def challenge5d(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    
    answer = {'00': 'Y', '01': 'Z', '10': 'X', '11': 'I'}
    
    return candidate == answer, username

### challenge6 ###

def challenge6a(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    candidate_qc = load_quantum_circuit(candidate)
    
    q = QuantumRegister(4, name = "q")
    base = QuantumCircuit(q)
    
    answer_qc = base.copy_empty_like()
    
    answer_qc.h([0,1,2,3])
    
    sv_candidate = Statevector(candidate_qc)
    sv_answer = Statevector(answer_qc)
    
    return sv_candidate.equiv(sv_answer), username

def challenge6b(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    candidate_qc = load_quantum_circuit(candidate)
    
    def cnz(n: int) -> QuantumCircuit:
        circuit = QuantumCircuit(n)
        circuit.h(n-1)
        circuit.mcx([i for i in range(n-1)], n-1)
        circuit.h(n-1)
        return circuit
    
    q = QuantumRegister(4, name = "q")
    base = QuantumCircuit(q)
    
    answer_qc = base.copy_empty_like()
    
    answer_qc.h([0,1,2,3])
    answer_qc.x([1,3])
    answer_qc.compose(cnz(4), inplace=True)
    answer_qc.x([1,3])
    
    sv_candidate = Statevector(candidate_qc)
    sv_answer = Statevector(answer_qc)
    
    return sv_candidate.equiv(sv_answer), username

def challenge6c(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    candidate_qc = load_quantum_circuit(candidate)
    
    def cnz(n: int) -> QuantumCircuit:
        circuit = QuantumCircuit(n)
        circuit.h(n-1)
        circuit.mcx([i for i in range(n-1)], n-1)
        circuit.h(n-1)
        return circuit
    
    q = QuantumRegister(4, name = "q")
    base = QuantumCircuit(q)
    
    answer_qc = base.copy_empty_like()
    
    answer_qc.h([0,1,2,3])
    answer_qc.x([0,1,2,3])
    answer_qc.compose(cnz(4), inplace=True)
    answer_qc.x([0,1,2,3])
    answer_qc.h([0,1,2,3])
    
    sv_candidate = Statevector(candidate_qc)
    sv_answer = Statevector(answer_qc)
    
    return sv_candidate.equiv(sv_answer), username

def challenge6d(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    
    return candidate == 3, username

def challenge6e(candidate: Model):
    username = candidate.username
    candidate = json.loads(candidate.answer)
    
    return candidate == 0.961319, username