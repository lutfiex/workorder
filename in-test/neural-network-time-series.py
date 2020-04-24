import numpy as np
import pandas as pd
df = pd.read_excel('100003509.xlsx')
out1 = df['outb']
out2 = df['inb']
out2.values.tolist()
out1.values.tolist()
out = out1
x = []
y = []
n=[]
t_out = []
y_out = []
f = []
list(t_out)
print("pembuatan fit")
################################### data untuk prediksi

for i in range(len(out)-4):
    print(str(i) +" " + str(i+4))
    n.append(out[i])
    n.append(out[i+1])
    n.append(out[i+2])
    n.append(out[i+3])
    n.append(out[i+4])
    n.append(out2[i+4])
    t_out.append(n)
    n = []
#n = np.array(t_out)
for i in range(len(out)-5):
    y.append(out[i+5])
x= np.array(t_out[:-1])
y= np.array(y)
y = y.reshape(x.shape[0],1)
#####normalisasi####
##tempx = str(np.amax(x))
##tempx = len(tempx)
vv = np.amax(x)
x = np.divide(x,vv)
y = np.divide(y,vv)


#######################
final = out.tail(5)
final = np.array(final)
final2 = out2.tail(1)
final2 = np.array(final2)
final = np.append(final,final2)
final = np.divide(final,vv)
###################################

np.random.seed(42)
z = np.random.random_integers(vv,size=(6,1))
weights = z/vv
zb = np.random.random_integers(vv,size=(1,1))
bias = zb/vv
lr = 0.0001

def hasil(k):
    result = sigmoid(np.dot(k, weights) + bias)
    return result[0]

def sigmoid(n):
    return 1/(1+np.exp(-n))

def sigmoid_der(n):
    return sigmoid(n)*(1-sigmoid(n))
print("mulai training")
############################################
for epoch in range(10000):
    print(epoch)
    inputs = x

    # feedforward step1
    XW = np.dot(x, weights) + bias

    #feedforward step2
    z = sigmoid(XW)


    # backpropagation step 1
    error = z - y

    #print(error.sum())

    # backpropagation step 2
    dcost_dpred = error
    dpred_dz = sigmoid_der(z)

    z_delta = dcost_dpred * dpred_dz

    inputs = x.T
    weights -= lr * np.dot(inputs, z_delta)

    for num in z_delta:
        bias -= lr * num


####################cetak hasil###########
print("pembuatan file excel")
for i in range(len(x)):
    f.append(hasil(x[i]))
y = y*vv
f = np.array(f)
f = f*vv
f = f.astype(int)
f = pd.DataFrame(f)
y = pd.DataFrame(y)
esult = pd.concat([y,f], axis=1)
esult.to_excel("hasil.xlsx")
