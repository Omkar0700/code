import torch
import numpy as np

device="cuda" if torch.cuda.is_available() else "cpu"
my_tensor=torch.tensor([[1,2,3],[2,3,4]],dtype=torch.float32,device=device,requires_grad=True)

# common initilization methods
x=torch.empty(size=(3,3))
print(x)
x=torch.zeros((3,3))
print(x)
x=torch.rand((3,3))
print(x)
x=torch.ones((3,3))
print(x)
x=torch.eye(5,5)
print(x)
x=torch.arange(start=0,end=5,step=1)
print(x)
x=torch.linspace(start=0.1,end=1,steps=10)
print(x)
x=torch.empty(size=(1,5)).normal_(mean=0,std=1)
print(x)
x=torch.empty(size=(3,3)).uniform_(0,1)
print(x)
x=torch.diag(x)
print(x)

# conversion from numpy to tensor and viceversa

n_array=np.on((5,5))
print(n_array)
ts=torch.from_numpy(n_array)
print(ts)
n_array_back=ts.numpy()
print(n_array_back)