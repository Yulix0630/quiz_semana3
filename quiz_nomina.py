import pandas as pd


# 1) CLASE BASE (PADRE): datos comunes + ENCAPSULAMIENTO del salario
class EmpleadoBase:
    """Clase base: encapsula el salario y define el comportamiento comun."""

    def __init__(self, nombre, salario_base, ciudad):
        self.nombre = nombre
        self.ciudad = city = ciudad
        # Guardamos el salario usando el SETTER para asegurar la validación
        self.salario_base = salario_base

    # GETTER: leer el salario de forma segura
    @property
    def salario_base(self):
        # Devuelve el atributo privado
        return self._salario_base

    # SETTER: valida ANTES de guardar
    @salario_base.setter
    def salario_base(self, nuevo_salario):
        if int(nuevo_salario) < 0:
            raise ValueError("El salario no puede ser negativo.")
        self._salario_base = int(nuevo_salario)

    # Metodo comun que CADA HIJA sobreescribe (POLIMORFISMO)
    def calcular_pago(self):
        raise NotImplementedError("Cada tipo de empleado calcula su pago.")

    def obtener_informacion(self):
        # Devuelve el formato solicitado: "Ana | EmpleadoPlanta | Medellin | base $3000000"
        return f"{self.nombre} | {type(self).__name__} | {self.ciudad} | base ${self.salario_base}"


# 2) CLASES HIJAS (HERENCIA)
class EmpleadoPlanta(EmpleadoBase):
    def calcular_pago(self):
        # POLIMORFISMO: Recibe salario base + 30% de prestaciones
        return int(self.salario_base * 1.30)


class EmpleadoContratista(EmpleadoBase):
    def calcular_pago(self):
        # POLIMORFISMO: Recibe solo su salario base
        return self.salario_base


# 3) Crear el objeto correcto segun el TIPO
def crear_empleado(nombre, tipo, salario_base, ciudad):
    if tipo == "PLANTA":
        return EmpleadoPlanta(nombre, salario_base, ciudad)
    elif tipo == "CONTRATISTA":
        return EmpleadoContratista(nombre, salario_base, ciudad)
    else:
        raise ValueError(f"tipo desconocido '{tipo}'")


# =====================================================================
# 4) LECTURA DEL EXCEL  --  ¡YA ESTA LISTA!  (no necesitas modificarla)
# =====================================================================
def leer_empleados_excel(nombre_archivo):
    """Lee empleados desde un Excel y devuelve una lista de objetos Empleado."""
    empleados = []
    try:
        df = pd.read_excel(nombre_archivo)
    except FileNotFoundError:
        print(f"  [Error] No se encontró el archivo '{nombre_archivo}'")
        return empleados

    # Normalizamos los nombres de columna
    df.columns = [str(c).strip().lower() for c in df.columns]

    # Verificamos que existan las columnas mínimas
    columnas_necesarias = {"nombre", "tipo", "salario_base"}
    if not columnas_necesarias.issubset(df.columns):
        faltan = columnas_necesarias - set(df.columns)
        print(f"  [Error] Al Excel le faltan columnas: {faltan}")
        return empleados

    for _, fila in df.iterrows():
        if pd.isna(fila["nombre"]) or pd.isna(fila["tipo"]) or pd.isna(fila["salario_base"]):
            print("  [Aviso] Fila incompleta ignorada.")
            continue

        nombre = str(fila["nombre"]).strip()
        tipo = str(fila["tipo"]).strip().upper()
        salario = fila["salario_base"]
        ciudad = str(fila["ciudad"]).strip() if "ciudad" in df.columns and not pd.isna(fila["ciudad"]) else "Sin Ciudad"

        try:
            empleado = crear_empleado(nombre, tipo, salario, ciudad)
            if empleado is not None:
                empleados.append(empleado)
        except ValueError as error:
            print(f"  [Aviso] Se ignoro {nombre}: {error}")

    return empleados


# =====================================================================
# 5) RETO EXTRA: ¡CREA TU PROPIA FUNCION!
# =====================================================================
def empleado_mejor_pagado(empleados):
    """
    Analiza la lista de empleados y encuentra al que recibe el mayor pago neto,
    aplicando el polimorfismo mediante el método calcular_pago().
    """
    if not empleados:
        return "No hay empleados registrados."
    
    # Buscamos el empleado con el mayor calcular_pago()
    mejor_pagado = max(empleados, key=lambda emp: emp.calcular_pago())
    
    return f"{mejor_pagado.nombre} ({type(mejor_pagado).__name__}) con un pago total de ${mejor_pagado.calcular_pago()}"


# 6) Funcion principal
def ejecutar_quiz():
    # Nota: Asegúrate de tener el archivo 'empleados.xlsx' en la misma carpeta
    empleados = leer_empleados_excel("empleados.xlsx")

    print("\n--- Nomina ---")
    for empleado in empleados:
        # POLIMORFISMO: la misma llamada, distinto resultado según el tipo
        print(f"{empleado.obtener_informacion()} -> pago total: ${empleado.calcular_pago()}")

    # Reto completado:
    print("\n--- Reto Extra ---")
    print("Empleado mejor pagado:", empleado_mejor_pagado(empleados))


# Iniciar el programa
if __name__ == "__main__":
    ejecutar_quiz()