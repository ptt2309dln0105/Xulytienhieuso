from scipy.io import wavfile
import matplotlib.pyplot as plt 
import numpy as np
import math

samplerate, data = wavfile.read('Audio/studio_male.wav')
times = np.arange(len(data))/float(samplerate)
dt = 1/samplerate

frames = (float)((len(data) / samplerate))
fig, ax = plt.subplots(3)
ax[0].set_title("Tín hiệu Studio Male")
ax[0].set_xlabel('time')
ax[0].set_ylabel('amplitude') 
ax[0].plot(times,data)
arr = [0,0.67,2.986,3.276,4.482,4.793,5.70,5.970,7.283]
print(arr)

k = 1
frames = (int)(frames*100)
for i in arr:
    ax[0].axvline(i, ymin = 0, ymax = 1, linewidth = 2, linestyle = "-.", color = 'orange')
    
data0 = [i**2 for i in data] # tính dãy data

E = np.empty(1, dtype=np.int64)

samplein10 = int(samplerate * 0.01)
for i in range(frames):
    c = np.empty(1, dtype=np.int64)
    for j in range(samplein10):
        c = np.append(c, data0[i * samplein10 + j])
    c = np.delete(c, 0) # xoa junk value
    d = np.sum(c)
    E = np.append(E, d)
E = np.delete(E, 0) # xoa junk value

max = np.max(E)
min = np.min(E)
print(np.log10(max))
print(np.log10(min))
xnorm = [((val - np.amin(np.log10(E))) / (np.amax(np.log10(E)) - np.amin(np.log10(E)))) for val in np.log10(E)]


ax[1].set_xlabel('index of frames')
ax[1].set_ylabel('amplitude')         
ax[1].plot(E[0:frames])
ax[1].set_title('Năng lượng')

draw = []
m = 0
nguong_y = 0.6
check = 0
while (m < len(xnorm)):
    if(xnorm[m] > nguong_y and check==0) :
        a = True
        for i in range(m,m+5) :
            if (xnorm[i] < nguong_y) :
                a = False
                break
        if (a == True) :
            draw.append(m)
            check=1
    if(xnorm[m] < nguong_y and check==1) :
        a=True
        for i in range(m,m+20):
            if (xnorm[i] > nguong_y):
                a=False
                break
        if(a==True):
            draw.append(m-1)
            check=0
    m=m+1
for i in draw:
     ax[2].axvline(i, ymin = 0, ymax = 1, linewidth = 2, linestyle = "-.", color = 'orange')  

print(draw)
ax[2].axhline(y=nguong_y, color='r', linestyle='--')  
ax[2].set_xlabel('index of frames')
ax[2].set_ylabel('amplitude') 
ax[2].set_title('Năng lượng Chuẩn hóa')
ax[2].plot(xnorm)
plt.show()