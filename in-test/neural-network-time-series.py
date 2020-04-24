import pandas as pd
import time
v = ""
file = str(input("file: "))
file = list(file)
file.pop(0)
file.pop(-1)
file = v.join(file)
##pre
s1 = []
wotype = []
tahun = time.localtime()[0]
bulan = time.localtime()[1]
hari = time.localtime()[2]
bulannow = str(bulan)+" "+str(tahun)
harinow = str(hari)+" "+str(bulan)+" "+str(tahun)
wday = str(hari)+str(bulan)+str(tahun)
work = "WO"+wday
work1 = []
uom = []
boum = []
akl = []
ifu = []
wc = []
wob = []
slq = []
elq = []

##read
excel1 = file
writer = pd.ExcelWriter('output.xlsx')

dfx = pd.read_excel(excel1 ,"SOH")
df2 = pd.read_excel(excel1 ,"Master")


df1 = dfx.sort_values("RCVD_DTTM")

##copy

retime = df1['RCVD_DTTM']
retime = pd.Series(retime)
batch = df1['Batch']
lpn = df1['LPN']
Sku = df1['SKU']
exdate = df1['Expire Date']
acqty = df1['Actual QTY']
bqty = df1['Actual QTY']
#make
for u in range(len(df1['Warehouse'])):
    slq.append("0")
for u in range(len(df1['Warehouse'])):
    elq.append("0")
for u in range(len(df1['Warehouse'])):
    wob.append(" ")
for u in range(len(df1['Warehouse'])):
    wc.append(harinow)
for u in range(len(df1['Warehouse'])):
    ifu.append(" ")
for u in range(len(df1['Warehouse'])):
    akl.append(" ")
for u in range(len(df1['Warehouse'])):
    uom.append("EA")
for u in range(len(df1['Warehouse'])):
    boum.append("EA")
for workno in range(len(df1['Warehouse'])):
   
    Work = work+str(workno+1).zfill(5)
    work1.append(Work)
for wot in range(len(df1['Warehouse'])):
    wotype.append("Labelling")
for i in range(len(df1['Warehouse'])):
    s1.append(bulannow)

##calculate

z = []
lebel_level = []
sk =Sku.tolist()
for u in range(len(df1['Warehouse'])):
	n = df2.loc[df2['Catalogue#']==str(sk[u])].index
	z.append(n[0])
tqty = acqty.tolist()
f = []
for j in range(len(z)):
    l = z[j]
    lebel_level.append(df2['Sub-labelling UOM level'][l])	
    if (df2['Sub-labelling UOM level'][l] == 'SP'):
        f.append(df2['ea/sp'][l])
    if (df2['Sub-labelling UOM level'][l] == 'EA'):
        f.append(1)
    if (df2['Sub-labelling UOM level'][l] == 'No need to label'):
        f.append(100000000000)
    if (df2['Sub-labelling UOM level'][l] == 'CS'):
        f.append(df2['ea/cs'][l])

call  = [x/y for x, y in zip(tqty, f)]
cal = list(map(int, call))
#remake
label_level = pd.Series(lebel_level)
label_level = label_level.rename("Label_level")
retime = retime.rename('RCVD_DTTM')
acqty = pd.Series(acqty)
acqty = acqty.rename("Quantity")
##bqty = pd.Series(bqty)
##bqty = bqty.rename("Base Quantity")
##elq = pd.Series(elq)
##elq = elq.rename("Each label Qty")
##slq = pd.Series(slq)
##slq = slq.rename("Shelf label Qty")
wob = pd.Series(wob)
wob = wob.rename("WO Created By")
wc = pd.Series(wc)
wc = wc.rename("WO Created Date")
exdate = pd.Series(exdate)
exdate = exdate.rename("Expirydate")
ifu = pd.Series(ifu)
ifu = ifu.rename("IFU CODE")
akl = pd.Series(akl)
akl = akl.rename("NO AKL")
##boum = pd.Series(boum)
##boum = boum.rename("Base OUM")
uom = pd.Series(uom)
uom = uom.rename("UOM")
lpn = pd.Series(lpn)
lpn = lpn.rename("No LPN")
work1 = pd.Series(work1)
work1 = work1.rename("Work Order")
value = df1["Warehouse"]
s1 = pd.Series(s1)
s1 = s1.rename("Wo month")
wotype = pd.Series(wotype)
wotype = wotype.rename("WO TYPE")

##cq = pd.Series(cal)
##cq = cq.rename("Carton Quantity")
##cl = pd.Series(cal)
##cl = cl.rename("Case label Qty")
tl = pd.Series(cal)
tl = tl.rename("Total Label")
work1 = pd.DataFrame(work1)

#out5
esult = pd.concat([s1, wotype, Sku, batch, retime, lpn, acqty, uom,label_level,    tl, akl, ifu, exdate, wc, wob], axis=1, sort=False)
s = esult.sort_values("RCVD_DTTM")
#s = s.sort_values('Work Order')
#esult = pd.concat([s, work1], axis=1)
s.join(work1)
s = s.reset_index()
s = s.join(work1)
s = s.drop(['index'], axis=1)

s.to_excel("out.xlsx", index=False)
print("done")



##pencari index
##  a = df1.loc[df1['LPN']==lpn[u]].index

#  pencarian berdasarkan sku
## df2.loc[df2['Catalogue#']==str(sk[1])].index

## pencarian selesai sku
## for u in range(len(df1['Warehouse'])):
##	n = df2.loc[df2['Catalogue#']==str(sk[u])].index
##	z.append(n[0])

    
