import os
print('Your windows laptop is about to shutdown. Press the power button (the top right key on the keyboard) to \npower it back on again')
import time
time.sleep(10)
os.system("shutdown /s /t 1") 