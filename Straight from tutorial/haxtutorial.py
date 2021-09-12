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

pm = pymem.Pymem("ac_client.exe")
gameModule = module_from_name(pm.process_handle, "ac_client.exe").lpBaseOfDll

X1=GetPtrAddr(gameModule + 0x10f4f4, [0x38])
Y1=GetPtrAddr(gameModule + 0x10f4f4, [0x3c])
Z1=GetPtrAddr(gameModule + 0x10f4f4, [0x34])

lastX = 0.0
lastY = 0.0
lastZ = 0.0

while True:
    Xvalue=pm.read_float(X1)
    Yvalue=pm.read_float(Y1)
    Zvalue=pm.read_float(Z1)

    if(keyboard.is_pressed('k')):
        lastX = Xvalue
        lastY = Yvalue
        lastZ = Zvalue
        print("succ bacc coords saved: X=", lastX ,"Y=", lastY, "Z=", lastZ)
        time.sleep(0.2)
    if(keyboard.is_pressed('l')):
        pm.write_float(X1, lastX)
        pm.write_float(Y1, lastY)
        pm.write_float(Z1, lastZ)
        print('succ bacc activated')
        time.sleep(0.2)

    print(Xvalue, Yvalue, Zvalue)
    time.sleep(0.09)

