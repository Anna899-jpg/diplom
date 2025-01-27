import matplotlib.pyplot as plt
import numpy as np

# Создание данных для визуализаций
x = np.linspace(0, 10, 100)
y1 = np.sin(x)  # Значения синуса
y2 = np.cos(x)  # Значения косинуса

#Линейный график для синуса и косинуса
plt.figure(figsize=(10, 5))
plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='red')
plt.title('Линейный график: sin и cos')
plt.xlabel('x')
plt.ylabel('значение')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.legend()
plt.grid()
plt.show()

# Столбиковый график
categories = ['A', 'B', 'C', 'D']
values = [23, 17, 35, 29]

plt.figure(figsize=(10, 5))
plt.bar(categories, values, color='orange')
plt.title('Столбиковый график')
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.show()

# Круговая диаграмма
sizes = [30, 20, 25, 25]
labels = ['Группа 1', 'Группа 2', 'Группа 3', 'Группа 4']

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Круговая диаграмма')
plt.axis('equal')
plt.show()