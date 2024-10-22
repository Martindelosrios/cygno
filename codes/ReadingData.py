import numpy as np
import matplotlib.pyplot as plt


import ROOT

data = ROOT.TFile.Open("../data/bkg/reco_run84603_3D.root")

nevents = len(data['Events;1']['redpix_ix'].arrays())


max_xpix = 0
max_ypix = 0

for i in np.arange(nevents):
    if len(data['Events;1']['redpix_ix'].arrays(library='np')['redpix_ix'][i]) > 0:
        aux = np.max(data['Events;1']['redpix_ix'].arrays(library='np')['redpix_ix'][i])
        max_xpix = np.max([max_xpix, aux])

    if len(data['Events;1']['redpix_iy'].arrays(library='np')['redpix_iy'][i]) > 0:
        aux = np.max(data['Events;1']['redpix_iy'].arrays(library='np')['redpix_iy'][i])
        max_ypix = np.max([max_ypix, aux])


xpix = 2295 #max_xpix
ypix = 2059 #max_ypix

i = 11
img = np.zeros((xpix, ypix))

xPix_ind = data['Events;1']['redpix_ix'].arrays(library='np')['redpix_ix'][i]
yPix_ind = data['Events;1']['redpix_iy'].arrays(library='np')['redpix_iy'][i]

img[xPix_ind, yPix_ind] = data['Events;1']['redpix_iz'].arrays(library='np')['redpix_iz'][i]

plt.imshow(img)
plt.show()

