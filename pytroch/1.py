import torch
import numpy as np
from torch import nn
import matplotlib.pyplot as plt
weigth=0.7
bias=0.3
start=0
end=1
step=0.02
X=torch.arange(start,end,step).unsqueeze(dim=1)# unsequeeze is used to add extra diminsion 
Y=weigth*X+bias
print(X[:10],Y[:10])
train_split=int(0.8*len(X))
X_train,Y_train=X[:train_split],Y[:train_split]
X_test,Y_test=X[train_split:],Y[train_split:]
class linearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights=nn.Parameter(torch.randn(1,requires_grad=True,dtype=torch.float))
        self.bias=nn.Parameter(torch.randn(1,requires_grad=True,dtype=torch.float))
    def forward(self,x:torch.Tensor)->torch.Tensor:
        return self.weights * x + self.bias
        
model_0=linearRegression()
with torch.inference_mode():
    y_preds=model_0(X_test)
print(y_preds)
