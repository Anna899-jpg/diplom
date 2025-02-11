import plotly.express as px
import pandas as pd
import numpy as np

# Генерация случайных данных
np.random.seed(42)
data_size = 100
data = {
    'x': np.random.rand(data_size),
    'y': np.random.rand(data_size),
    'category': np.random.choice(['A', 'B', 'C'], data_size)
}
df = pd.DataFrame(data)

# График рассеяния
scatter_fig = px.scatter(df, x='x', y='y', color='category', title='График рассеяния',
                          labels={'x':'Значения X', 'y':'Значения Y', 'category': 'Категория'})
scatter_fig.show()

# Столбиковый график
bar_fig = px.bar(df.groupby('category')['y'].mean().reset_index(),
                  x='category', y='y', title='Столбиковый график: Средние значения по категориям',
                  labels={'y':'Среднее значение Y', 'category': 'Категория'})
bar_fig.show()

# Ящиковая диаграмма
box_fig = px.box(df, x='category', y='y', title='Ящиковая диаграмма по категориям')
box_fig.show()

