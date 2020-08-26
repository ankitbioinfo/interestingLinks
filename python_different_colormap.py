



import numpy as np
import matplotlib.pyplot as plt
import xlrd
import seaborn as sns
from colour import Color
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap




def print_sheet_name(name):
    xls=xlrd.open_workbook(name,on_demand=True)
    sheet_names=xls.sheet_names()
    #print(sheet_names)
    alldata=[]
    for i in range(len(sheet_names)):
		print(i,sheet_names[i])

def read_xls_data(name,sheetid):
	xls=xlrd.open_workbook(name,on_demand=True)
	sheet_names=xls.sheet_names()
	sheet = xls.sheet_by_name(sheet_names[sheetid])
	print(sheet.nrows,sheet.ncols)
	data=np.zeros((sheet.nrows-1,sheet.ncols),dtype=np.float)
	print('Row Name')
	rowname=[]
	for k in range(sheet.ncols):
		rowname.append(sheet.cell(0,k).value)
		print(k,rowname[k])

	for k in range(sheet.ncols):
		for j in range(1,sheet.nrows):
			#print(sheet.cell(j,k).value)
			data[j-1,k]=sheet.cell(j,k).value
            #print(column_len(sheet,0))

	return data





name='ScatteringCoefficientIntralipidwavelength.xlsx'
print_sheet_name(name)
data=read_xls_data(name,6)#put sheet id to read
#f=open(name)

size=data.shape
print(size)
#data = np.loadtxt(name, delimiter="\t", skiprows=0)
fig, axs = plt.subplots( nrows=1, ncols=1 )

legend=['IL:0.75%','IL:1%','IL:1.25%','IL:1.5%','IL:1.75%','IL:2%']
indigo=list(np.array([75,0,130])/255.0)
maroon=[0.5,0,0]
slategray=list(np.array([112,128,144])/255.0)
chocolate=list(np.array([210,105,30])/255.0)
rosybrown=list(np.array([188,143,143])/255.0)
deeppink=list(np.array([255,20,147])/255.0)
darkslateblue=list(np.array([72,61,139])/255.0)
catawba=list(np.array([110,49,68])/255.0)
MediumCarmine=list(np.array([176,59,55])/255.0)
CedarChest=list(np.array([199,90,72])/255.0)
JasperOrange=list(np.array([235,137,71])/255.0)
YellowOrange=list(np.array([251,171,52])/255.0)
Sunglow=list(np.array([253,197,52])/255.0)
Sandstorm=list(np.array([242,224,63])/255.0)
Saffron=list(np.array([239,192,58])/255.0)
Marigold=list(np.array([236,160,53])/255.0)
CadmiumOrange=list(np.array([232,129,47])/255.0)
Vivid=list(np.array([229,97,42])/255.0)
CGRed=list(np.array([226,65,37])/255.0)
Yellow=list(np.array([255,254,0])/255.0)
BitterLemon=list(np.array([211,229,2])/255.0)
Limerick=list(np.array([155,192,4])/255.0)
Avocado=list(np.array([93,154,5])/255.0)
MetallicGreen=list(np.array([39,121,3])/255.0)
EmeraldGreen=list(np.array([3,100,6])/255.0)

#gradientColor=sns.color_palette("Blues",len(legend))
#gradientColor=sns.dark_palette("purple",len(legend),reverse=True)
#gradientColor=sns.color_palette("husl", len(legend))
#gradientColor2=sns.light_palette("yellow",len(legend),reverse=False)
#bottom=cm.get_cmap('Blues',m)
#newcolors=np.vstack((top(np.linspace(0.5,0,m)),bottom(np.linspace(0.5,0,m))))


n=len(legend)
top=cm.get_cmap('Oranges_r',n)
newcmp=ListedColormap(top(np.linspace(0.5,0,n)),name="OrangeBlue")
gradientColor=newcmp.colors

top=cm.get_cmap('winter',n)
newcmp=ListedColormap(top(np.linspace(1,0,n)),name="OrangeBlue")
gradientColor=newcmp.colors



#gradientColor=[Yellow,BitterLemon,Limerick,Avocado,MetallicGreen,EmeraldGreen,Sandstorm,Saffron,Marigold,CadmiumOrange,Vivid,CGRed,Sunglow,YellowOrange,JasperOrange,CedarChest,MediumCarmine,catawba]
markerdes=[list(gradientColor[0]),list(gradientColor[1]),list(gradientColor[2]),list(gradientColor[3]),list(gradientColor[4]),list(gradientColor[5]),'none','none','none','none','none',Sandstorm,Saffron,'none',CadmiumOrange,'none',CGRed,Sunglow,rosybrown,deeppink,darkslateblue]
#markerdes=gradientColor

ExpSymbol=['v','*','o','x','^','.']
TheorySymbol=['-','-','-','-','-','-']



#label=legend[count],
count=0
index=0
for i in range(1,size[1],3):
			axs.errorbar(data[:,0],data[:,i],yerr=0.8*data[:,i+1],fmt=ExpSymbol[count],color=gradientColor[count],mfc=markerdes[count],ms=8,solid_capstyle='projecting',capsize=3)
			#axs.plot(data[:,0],data[:,i],ExpSymbol[count],color=,mfc=,ms=7)
			axs.plot(data[:,0],data[:,i+2],TheorySymbol[count],color=gradientColor[count],lw=0.5)
			#axs[i,j].set_title(tname[index])

			count=count+1

#axs.legend(legend,prop={'size': 8},frameon=False)

#for ax in axs.flat:
#axs.legend()
axs.axis([440,875,0.6,3.6])
axs.set(xlabel='Wavelength [nm]', ylabel='Reduced Scattering Coefficient $[mm^{-1}]$')

#for ax in axs.flat:
#    ax.label_outer()
axs.arrow(865, 0.7, 0, 1.3, head_width=5, lw=0.6,head_length=0.1, fc='k', ec='k')
axs.text(875,1.5,'$\mu_s^\prime$')

axs.spines['right'].set_visible(False)
axs.spines['top'].set_visible(False)
axs.get_xaxis().tick_bottom()
axs.get_yaxis().tick_left()
fig = plt.gcf()
#fig.set_size_inches(10, 7,forward=True)


plt.show()
fig.savefig('reduced_scattering_coefficient_plot.png',dpi=100)
