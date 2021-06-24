import numpy as np
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter

def rysujWykres():
    all_months = ["styczeń", "luty", "marzec","kwiecień","maj","czerwiec","lipiec","sierpień","wrzesień","październik","listopad","grudzień"]
    months = []
    months_str = []
    currentMonth = datetime.now().month
    sumy = []
    for i in range(int(currentMonth)-6, int(currentMonth)):
        x = currentMonth-i
        #suma = "suma" + str(x)
        months_str.append(all_months[x])
        months.append(x)
        with open("/home/dominika/Pulpit/projekt-kopia/"+str(x)+".txt", "r+") as y:
            suma = y.read().split()
            print(y.read())
        suma_temp = 0
        for i in range(0, len(suma)):
            temp = suma[i].replace(",", ".")
            suma_temp += float(temp)
        sumy.append(suma_temp)
    #sumy.reverse()
    #y.close()
    print(months)
    print(sumy)
    return (months,sumy,months_str)

rysujWykres()