import numpy as np
import matplotlib.pyplot as plt
import xlrd
from itertools import takewhile
import numpy.polynomial.polynomial as poly


def column_len(sheet, index):
    col_values = sheet.col_values(index)
    col_len = len(col_values)
    for _ in takewhile(lambda x: not x, reversed(col_values)):
        col_len -= 1
    return col_len



def read_xls_data(name):
    xls=xlrd.open_workbook(name,on_demand=True)
    sheet_names=xls.sheet_names()
    print(sheet_names)
    alldata=[]
    for i in range(len(sheet_names)):
        sheet = xls.sheet_by_name(sheet_names[i])
        print(sheet.nrows,sheet.ncols)
        data=np.zeros((sheet.nrows-1,sheet.ncols),dtype=np.float)
        print('Row Name')
        rowname=[]
        for k in range(sheet.ncols):
            rowname.append(sheet.cell(0,k).value)
        print(rowname)
        for j in range(1,sheet.nrows):
            for k in range(sheet.ncols):
                data[j-1,k]=sheet.cell(j,k).value
            #print(column_len(sheet,0))
        alldata.append(data)
    return alldata




name='Numberoftrials1%_IL.xlsx'
data=read_xls_data(name)

wavelength=[400,450,500,550,600,650,700,750,800,850]

Fiber_distance=[0.634,0.669,0.708,1.149,1.178,1.328]

distance=np.array(Fiber_distance)

mycolor=['r','b','g','k']

for i in range(len(wavelength)):
    print(wavelength[i])
    Ymin=[]
    Ymax=[]
    parameter=[]
    for j in range(len(data)):
        for k in range(len(data[j])-1):
            if ((wavelength[i] > data[j][k,0]) & (wavelength[i] < data[j][k+1,0])):
                intensity=data[j][k+1,1:]
                lambda1=data[j][k+1,0]
                intensity_multiply_distance= np.log(intensity*distance)
                Y=intensity_multiply_distance
                #print(lambda1,intensity_multiply_distance)

                plt.plot(distance,Y,mycolor[j]+'o--')

                index=[2,3,4,5]
                X=distance[index]
                Y=Y[index]
                coefs = poly.polyfit(X, Y, 1)
                ffit = poly.polyval(X, coefs)

                plt.plot(X, ffit,mycolor[j]+'-')
                parameter.append(coefs)
                Ymin.append(min(Y))
                Ymax.append(max(Y))


    y0=min(Ymin)
    y1=max(Ymax)
    for j in range(len(data)):
        coefs=parameter[j]
        plt.text(0.01,y0+j*0.05, str('%0.4f'%coefs[1]) +'*X +' + str('%0.2f'%coefs[0]),  color=mycolor[j],fontsize=12)


    plt.title('wavelength '+ str(wavelength[i]))
    plt.axis([0,1.5,y0,y1])
    plt.savefig('Wavelength'+str(wavelength[i])+'.png')
    plt.close()
