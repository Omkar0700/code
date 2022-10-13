import torch  
# batch muliplication
batch=32
n=10
m=20
p=30
t1=torch.rand((batch,n,m))
t2=torch.rand((batch,m,p))
o_b=torch.bmm(t1,t2)
print(o_b)

# Brodacasting
x1=torch.rand((5,5))
x2=torch.rand((1,5))



