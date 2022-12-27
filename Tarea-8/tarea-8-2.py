import time

hora_actual = int(time.strftime('%H'))
if hora_actual > 7:
    print("Es hora de ir a casa")
else:
    print("Quedan",hora_actual-7,"para ir a casa")

