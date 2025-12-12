import pandas as pd

df = pd.read_csv('dataset.csv')
shape = df.shape
dtypes = df.dtypes
nulls = df.isnull().sum()

number_stats = (
    df.select_dtypes(include='number')
      .agg(['mean', 'median', 'std'])
      .T
)
number_stats.columns = ['среднее', 'медиана', 'отклонение']  # переименуем столбцы


object_columns = df.select_dtypes(include='object').columns
object_stats = []
for col in object_columns:
    object_stats.append(df[col].value_counts())

all_info = [shape, dtypes, nulls, number_stats, object_stats]


with open ('report.txt', 'w') as f:
    for row in all_info:
        f.write(str(row)+'\n\n')

if __name__ == '__main__':
    for row in all_info:
        print(row)
