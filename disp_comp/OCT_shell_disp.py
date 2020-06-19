#!/usr/bin/env python
# coding: utf-8

# ### Chromatic dispersion Iterative
# - read a buffer (binary file) into np.array
# - define a set of coefficients for chromatic disp comp
# - apply those to the spectra
# - FFT
# - (log scaling) optional
# - measure variance of the image (proxy for contrast)

# In[2]:


import numpy as np
import matplotlib.cbook as cbook #needed to load the binary file
import os
# get_ipython().run_line_magic('matplotlib', 'nbagg')
import matplotlib.pyplot as plt
from scipy.stats import zscore
import struct
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LightSource
import imageio
from PIL import Image
from matplotlib import cm
import tifffile
# import opencv as cv2


# In[39]:


## KEEP ONLY ONE:
# user = 'ELA'
user = 'AGI'
print(f"User {user} selected")

# file = r"C:\Users\lucab\Google Drive\01 - OCT\Axial Resolution and sampling\test_1_trLVL163_delay16_ND4_Depth_150mm.bin"
# file = r"C:\Users\lucab\Google Drive\01 - OCT\Axial Resolution and sampling\12mm"
file = r"/Users/fabioferoldi/Box/AGI/OCT data/2020.03.13_20112R_ganglion_imaging/test_03.bin"
fname = os.path.basename(file)

name_img_int = fname[:-4]+'_intensity.tif'
name_img_phase = fname[:-4]+'_phase.tif'


# In[26]:


## To read the length of the header, from
# https://books.google.nl/books?id=bIZHCgAAQBAJ&pg=PT149&lpg=PT149&dq=matplotlib+cbook+for+binary+with+header&source=bl&ots=mOirMtJP6U&sig=ACfU3U1Slj4Y2r4Xkl4sKuFsBna9Syog6A&hl=en&sa=X&ved=2ahUKEwiY34fLn9fpAhUL8KQKHaIFD-oQ6AEwBHoECAoQAQ#v=onepage&q=matplotlib%20cbook%20for%20binary%20with%20header&f=false  
with open(file, 'rb') as fp:
    img = memoryview(fp.read())
    
if user == 'AGI':
    header_size = 256
    header_length_format = '>'+str(header_size)+'c'# the first 3 blocks of 16bytes define the header's length
    header = img[:header_size] # first 256 char
    header = struct.unpack(header_length_format, header)
    #### missing: converting the separate bytes into one variable header[18:22]
    h = "".join([el.decode('utf-8') for el in header])
    print(h)
    spectrumsize = int(h[18:22])
    fftsize = int(h[32:36])
    linesize = int(3/2*fftsize)
    bscansize = int(h[49:53])
    datatype = np.dtype('>i2')
    del header
elif user == 'ELA':
    datatype = np.dtype('u2')
    header_size = 0
    linesize = 2048
    bscansize  = 256
    spectrumsize = 2048

filesize = os.path.getsize(file) - header_size  
buffersize = linesize * bscansize * datatype.itemsize
cscansize = (filesize-header_size) // buffersize


# In[38]:


## Iteration over all the frames
cscansize = 3

# the parameteres of the polynomial need to be found with the dedicated code
a3 = 0.857
a2 = 1.667
# create k-space and normalize it
k = np.arange(spectrumsize)
k = zscore(k)

curve = np.polyval([a3, a2, 0, 0], k)
disp_comp = np.exp(1j*curve, dtype='complex64').reshape(spectrumsize,1)

spectrum_size_padded = 2 # or 1, for what it matters
padding_factor = 2
while spectrumsize > spectrum_size_padded:
    spectrum_size_padded *= 2
spectrum_size_padded = spectrum_size_padded*padding_factor

print(spectrum_size_padded)
print(spectrumsize)
min_v = 110
max_v = 70
            
for i in range(cscansize):

    raw = np.frombuffer(img[header_size+i*buffersize:header_size+(i+1)*buffersize], 
                        dtype=datatype )
    raw = raw.reshape((bscansize, linesize)).T

    # AGI's A-scans have the FFT's magnitude appended - we remove it
    if user=='AGI': raw = raw[:spectrumsize, :]

    # apply Hanning window
    raw = np.multiply( 
            raw, 
            np.hanning(spectrumsize).reshape(spectrumsize,1)) # reshape is only a view, no extra memory ussage

         
    raw = np.multiply(raw, disp_comp, dtype='complex128') # apply disp compensation
    
    # zeropad (best way is to split the spectrum, invert the parts and put zeros in between)        
    raw = np.concatenate((
        raw[ int(spectrumsize/2) : , :],
        np.zeros( (spectrum_size_padded-spectrumsize, bscansize), dtype='complex128' ),
        raw[ : int(spectrumsize/2) , :]
    ))
    
    fft = np.fft.fft(raw, axis = 0)[:spectrum_size_padded//2] # extract fft
                   
    ampl = np.abs(fft).astype('float128') 
    phase = np.angle(fft).astype('float128') 
    
    #     bscan = 20*np.log10(
#                     np.abs(
#                         np.fft.fft(raw, axis = 0)[:spectrumsize//2] # this can be done on GPU! 
#                     ),
#                 dtype = np.float
#         )
    bscan_int = 20*np.log10(ampl) 
    bscan_img = (bscan_int - min_v)/(max_v-min_v)
    bscan_img[bscan_img > 1] = 1
    bscan_img[bscan_img < 0] = 0     
    bscan_img=(bscan_img*255).astype(np.uint8)
    
    phase_img= (((phase+np.pi)/(2*np.pi))*255).astype(np.uint8)
    
    if i==0:
        with tifffile.TiffWriter(name_img_int) as tif:
            tif.save(bscan_img)   
        with tifffile.TiffWriter(name_img_phase) as tif:
            tif.save(phase_img)   
    else:
        tifffile.imwrite(name_img_int, bscan_img, append=True)
        tifffile.imwrite(name_img_phase, phase_img, append=True)


# In[ ]:




