import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Установим стиль графиков Seaborn
sns.set(style="whitegrid")

# Создадим некоторые случайные данные
np.random.seed(42)
data_size = 100
data = {
    'x': np.random.rand(data_size),
    'y': np.random.rand(data_size),
    'category': np.random.choice(['A', 'B', 'C'], data_size)
}
df = pd.DataFrame(data)

# График рассеяния с разделением по категориям
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='x', y='y', hue='category', style='category', palette='deep')
plt.title('График рассеяния с разделением по категориям')
plt.show()

# Столбиковый график со средними значениями
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='category', y='y', estimator=np.mean, palette='muted')
plt.title('Столбиковый график: Средние значения по категориям')
plt.xlabel('Категория')
plt.ylabel('Среднее значение Y')
plt.show()

# Ящиковая диаграмма
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='category', y='y', palette='pastel')
plt.title('Ящиковая диаграмма по категориям')
plt.xlabel('Категория')
plt.ylabel('Значения Y')
plt.show()