import pandas as pd
import io

df = pd.read_csv('dataset.csv')

def write_to_report(lines):
    with open ('report.txt', 'w', encoding="utf-8") as f:
        f.write(lines)

def build_report():
    lines = []
    df = pd.read_csv('dataset.csv')

    shape = df.shape
    lines.append(str(shape))

    buf = io.StringIO()
    df.info(buf=buf)
    info_str = buf.getvalue()
    lines.append(info_str)

    nulls = df.isnull().sum()
    lines.append(nulls.to_string())

    number_stats = (
        df.select_dtypes(include='number')
          .agg(['mean', 'median', 'std'])
          .T
    )
    number_stats.columns = ['среднее', 'медиана', 'отклонение']
    lines.append(number_stats.to_string())

    object_columns = df.select_dtypes(include='object').columns
    for col in object_columns:
        lines.append(df[col].value_counts().to_string())

    return "\n".join(lines).rstrip() + "\n"

all_info = build_report()
write_to_report(all_info)

if __name__ == '__main__':
    print(all_info)
