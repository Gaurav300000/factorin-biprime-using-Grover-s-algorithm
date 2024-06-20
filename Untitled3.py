#!/usr/bin/env python
# coding: utf-8

# In[3]:


from qiskit import *
from qiskit.circuit.library import QFT
from qiskit.quantum_info import Operator
from qiskit.circuit.library.standard_gates import *
import numpy as np
import cmath


# In[ ]:





# In[4]:


def R(i,c,control,target,qc):
    qg = QuantumCircuit(1)
    u = np.array([[1,0],[0,np.exp(1j*c*np.pi/(2**i))]])
    u = Operator(u)
    qg.append(u,[0])
    custom = qg.to_gate()
    custom.label ='R'
    custom_2 = custom.control(1)
    qc.append(custom_2,[control,target])                     
    return qc                     


# In[23]:


def FADD(c,y,z,qc,ny,nz) :
    for i in range(0,ny):
        k=i
        for j in range(0,nz-i):
            R(j,c,y[i],z[k],qc)
            k = k+1
    return qc        
def C_FADD(c,ny,nz,qc,c_ontrol,y,z) :
    y1 = QuantumRegister(ny)
    z1 = QuantumRegister(nz)
    circuit = QuantumCircuit(y1,z1)
    FADD(c,y1,z1,circuit,ny,nz)
    circuit_2 = circuit.to_gate().control(1)
    qc.append(circuit_2,[c_ontrol,y[i for i in range(0,ny)]+z[i for i in range(0,nz)]])
    return qc


# In[18]:


nx = 3
ny = 3
nz = 3
x = QuantumRegister(nx)
y= QuantumRegister(ny)
z = QuantumRegister(nz)
qc = QuantumCircuit(x,y,z)
FADD(2,ny,nz,qc)
qc.draw("mpl")


# In[21]:


C_FADD(2,ny,nz,qc,x[0],y,z)


# In[ ]:


def diff_z()


# In[ ]:




