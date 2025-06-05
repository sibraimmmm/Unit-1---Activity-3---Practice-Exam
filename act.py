# Importar la biblioteca pandas para manipulación de datos
import pandas as pd 

# Definir una función para cargar un archivo CSV y devolver un DataFrame
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)  # Leer el archivo CSV desde la ruta especificada
    return df  # Devolver el DataFrame

# Cargar los datos desde el archivo Libro1.csv
df = load_data("C:/Users/Sibraim/Downloads/Libro1.csv")

# Crear una columna 'sales_filled' reemplazando valores NaN en 'sales' por 0
df['sales_filled'] = df['sales'].fillna(0)

# Reemplazar valores negativos en la columna 'discount' por pd.NA
df.loc[df['discount'] < 0, 'discount'] = pd.NA

# Eliminar filas donde tanto 'sales' como 'discount' son NaN
df = df.dropna(subset=['sales', 'discount'], how='all')

# Filtrar filas donde region es 'West' y 'sales' es NaN
df = df.loc[(df['region'] == 'West') & (df['sales'].isna())]

# Rellenar valores NaN en 'discount' con el promedio de 'discount'
df['discount'] = df['discount'].fillna(df['discount'].mean())

# Calcular 'net_sales' como sales * (1 - discount/100) solo para filas donde
# tanto 'sales' como 'discount' no son NaN
df['net_sales'] = pd.NA
df.loc[(df['sales'].notna()) & (df['discount'].notna()), 'net_sales'] = df['sales'] * (1 - df['discount'] / 100)

# Filtrar filas donde 'sales' >= 200 y 'discount' <= 10
df = df[(df['sales'] >= 200) & (df['discount'] <= 10)]

# Filtrar filas donde 'sales' no es NaN y ordenar por 'order_date' en orden descendente
df = df[df['sales'].notna()].sort_values(by=['order_date'], ascending=False)

# Convertir la columna 'order_date' a formato datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Crear una columna 'weekday' con los nombres de los días de la semana
df['weekday'] = df['order_date'].dt.day_name()

# Eliminar cualquier fila con valores NaN en cualquier columna
df = df.dropna()

# Imprimir el DataFrame final
print(df)
