from pymem import *
from pymem.process import *
import time
import keyboard

def GetPtrAddr(base, offsets): #get adress func.
    addr = pm.read_int(base)
    for i in offsets:
        if i != offsets[-1]:
            addr = pm.read_int(addr + i)
    return addr + offsets[-1]

pm = pymem.Pymem("ac_client.exe") #get game process
gameModule = module_from_name(pm.process_handle, "ac_client.exe").lpBaseOfDll #get base (process handle)

lastY = 0.0
lastX = 0.0
lastZ = 0.0

Y1=GetPtrAddr(gameModule + 0x10F4F4, [0x3C]) #find Y in memory
X1=GetPtrAddr(gameModule + 0x10F4F4, [0x38]) #find X in memory
Z1=GetPtrAddr(gameModule + 0x10F4F4, [0x34]) #find Z in memory

print('Injected!')

while True:
    try:
        Yval = pm.read_float(Y1) #read Y in memory
        Yvalp = "{:.2f}".format(Yval) #format it to show 2 decimal places (just for looks)
    except:
        Yvalp = "Not Found"
    try:
        Xval = pm.read_float(X1) #read X in memory
        Xvalp = "{:.2f}".format(Xval) #format it to show 2 decimal places (just for looks)
    except:
        Xvalp = "Not Found"
    try:
        Zval = pm.read_float(Z1) #read Z in memory
        Zvalp = "{:.2f}".format(Zval) #format it to show 2 decimal places (just for looks)
    except:
        Zvalp = "Not Found"
    if(keyboard.is_pressed('k')):
        lastY = Yval
        lastX = Xval
        lastZ = Zval
        print("succ bacc coords saved: X=", Xvalp ,"Y=", Yvalp, "Z=", Zvalp)
        time.sleep(0.2)
    if(keyboard.is_pressed('l')):
        pm.write_float(X1, lastX) #write last saved position of X
        pm.write_float(Y1, lastY) #write last saved position of Y
        pm.write_float(Z1, lastZ) #write last saved position of Z
        print('succ bacc activated')
        time.sleep(0.2)

    #print("Player0: X=", Xvalp ,"Y=", Yvalp, "Z=", Zvalp)
    time.sleep(0.09)
