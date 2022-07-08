import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


def TEMIS_TOMS_TROPOMI_NO2(path_to_input):
    file = open(''+str(path_to_input)+'')
    lst = []
    for line in file:
        lst += ([line.split(" ",0)])
    a,b = [],[]
    for q in range(5, len(lst), 145):
        d = lst[q:q+144]
        for i in range(0,len(d)):
            for j in range(0,80,4):
                a.append(float(d[i][0][j:j+4]))
        b.append(np.array(a))
        a=[]
    b1 = np.array(b)
    lat = np.arange(-89.9375,89.9500,0.125)
    lon = np.arange(-179.9375,179.9500,0.125)
    xx = xr.DataArray(b1, coords=[lat,lon], dims=['lat','lon'])
    xx1 = xx.where(xx!=-999, np.nan)
    return xx1

def TEMIS_GRD_OMI_NO2(path_to_input):
    file = open(''+str(path_to_input)+'')
    lon = np.linspace(-180,180,2880)
    lat = np.linspace(90,-90,1440)
    lst = []
    for line in file:
        lst += [line.split()]
    ll = np.array(lst)
    pp = []
    for i in range(7,len(ll)):
        k = ll[i]
        pp.append(k)
    pp = xr.DataArray(pp, coords=[lat,lon], dims=['lat','lon'])
    pp1 = pp.astype(float)#.plot(cmap='jet',vmin=0, vmax=30)
    pp2 = pp1/100
    pp2 = pp2.where(pp2>0, np.nan)
    mn2 = xr.DataArray(pp2, coords=[lat,lon], dims=['lat','lon'])
    return mn2

def TEMIS_GRD_GOME2B_NO2(path_to_input):
    file = open(''+str(path_to_input)+'')
    lon = np.linspace(-180,180,1440)
    lat = np.linspace(90,-90,720)
    lst = []
    for line in file:
        lst += [line.split()]
    ll = np.array(lst)
    pp = []
    for i in range(7,len(ll)):
        k = ll[i]
        pp.append(k)
    pp = xr.DataArray(pp, coords=[lat,lon], dims=['lat','lon'])
    pp1 = pp.astype(float)#.plot(cmap='jet',vmin=0, vmax=30)
    pp2 = pp1/100
    pp2 = pp2.where(pp2>0, np.nan)
    mn2 = xr.DataArray(pp2, coords=[lat,lon], dims=['lat','lon'])
    return mn2

def TEMIS_GRD_GOME2A_NO2(path_to_input):
    file = open(''+str(path_to_input)+'')
    lon = np.linspace(-180,180,2880)
    lat = np.linspace(90,-90,1440)
    lst = []
    for line in file:
        lst += [line.split()]
    ll = np.array(lst)
    pp = []
    for i in range(7,len(ll)):
        k = ll[i]
        pp.append(k)
    pp = xr.DataArray(pp, coords=[lat,lon], dims=['lat','lon'])
    pp1 = pp.astype(float)#.plot(cmap='jet',vmin=0, vmax=30)
    pp2 = pp1/100
    pp2 = pp2.where(pp2>0, np.nan)
    mn2 = xr.DataArray(pp2, coords=[lat,lon], dims=['lat','lon'])
    return mn2

def TEMIS_GRD_SCIA_NO2(path_to_input):
    file = open(''+str(path_to_input)+'')
    lon = np.linspace(-180,180,2880)
    lat = np.linspace(90,-90,1440)
    lst = []
    for line in file:
        lst += [line.split()]
    ll = np.array(lst)
    pp = []
    for i in range(7,len(ll)):
        k = ll[i]
        pp.append(k)
    pp = xr.DataArray(pp, coords=[lat,lon], dims=['lat','lon'])
    pp1 = pp.astype(float)#.plot(cmap='jet',vmin=0, vmax=30)
    pp2 = pp1/100
    pp2 = pp2.where(pp2>0, np.nan)
    mn2 = xr.DataArray(pp2, coords=[lat,lon], dims=['lat','lon'])
    return mn2

def TEMIS_dat_OMI_HCHO(path_to_input):
    lon = np.linspace(-179.88,179.88,1440)
    lat = np.linspace(-89.88,89.88,720)
    file = open(''+str(path_to_input)+'')
    lst = []
    for line in file:
        lst += [line.split()]
    ll = np.array(lst)
    pp = []
    for i in range(7,len(lat)+7):
        k = ll[i]
        pp.append(k)
    pp = xr.DataArray(pp, coords=[lat,lon], dims=['lat','lon'])
    pp1 = pp.astype(float)
    return pp1

def TEMIS_dat_GOME2B_HCHO(path_to_input):
    lon = np.linspace(-179.88,179.88,1440)
    lat = np.linspace(-89.88,89.88,720)
    file = open(''+str(path_to_input)+'')
    lst = []
    for line in file:
        lst += [line.split()]
    ll = np.array(lst)
    pp = []
    for i in range(7,len(lat)+7):
        k = ll[i]
        pp.append(k)
    pp = xr.DataArray(pp, coords=[lat,lon], dims=['lat','lon'])
    pp1 = pp.astype(float)
    return pp1

def TEMIS_dat_GOME2A_HCHO(path_to_input):
    lon = np.linspace(-179.88,179.88,1440)
    lat = np.linspace(-89.88,89.88,720)
    file = open(''+str(path_to_input)+'')
    lst = []
    for line in file:
        lst += [line.split()]
    ll = np.array(lst)
    pp = []
    for i in range(7,len(lat)+7):
        k = ll[i]
        pp.append(k)
    pp = xr.DataArray(pp, coords=[lat,lon], dims=['lat','lon'])
    pp1 = pp.astype(float)
    return pp1

def TEMIS_dat_SCIA_HCHO(path_to_input):
    lon = np.linspace(-179.88,179.88,1440)
    lat = np.linspace(-89.88,89.88,720)
    file = open(''+str(path_to_input)+'')
    lst = []
    for line in file:
        lst += [line.split()]
    ll = np.array(lst)
    pp = []
    for i in range(7,len(lat)+7):
        k = ll[i]
        pp.append(k)
    pp = xr.DataArray(pp, coords=[lat,lon], dims=['lat','lon'])
    pp1 = pp.astype(float)
    return pp1

def TEMIS_dat_GOME_HCHO(path_to_input):
    lon = np.linspace(-179.88,179.88,720)
    lat = np.linspace(-89.88,89.88,360)
    file = open(''+str(path_to_input)+'')
    lst = []
    for line in file:
        lst += [line.split()]
    ll = np.array(lst)
    pp = []
    for i in range(7,len(lat)+7):
        k = ll[i]
        pp.append(k)
    pp = xr.DataArray(pp, coords=[lat,lon], dims=['lat','lon'])
    pp1 = pp.astype(float)
    return pp1
