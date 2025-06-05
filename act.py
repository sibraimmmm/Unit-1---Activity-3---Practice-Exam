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

print(df)
