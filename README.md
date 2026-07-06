# Quiz Semana 3 - Fundamentos de Programación (Pilares de POO)

Este repositorio contiene la solución al quiz de la Semana 3, enfocado en la gestión de la nómina de una empresa mediante la lectura de datos desde un archivo de Excel (`empleados.xlsx`).

## 🚀 Pilares de POO Aplicados

* **Encapsulamiento:** Control seguro del atributo `salario_base` mediante el uso de getters (`@property`) y setters con validación para impedir valores negativos.
* **Herencia:** Las clases especializadas `EmpleadoPlanta` y `EmpleadoContratista` heredan la estructura común de la clase padre `EmpleadoBase`.
* **Polimorfismo:** Sobrescritura del método `calcular_pago()` en las clases hijas para aplicar las reglas de negocio específicas de cada tipo de contratación (+30% de prestaciones para planta).

## 🛠️ Reto Extra Implementado
Se diseñó e integró la función `empleado_mejor_pagado(empleados)`, la cual recorre dinámicamente la colección empleando el método polimórfico `calcular_pago()` para determinar el colaborador con mayores ingresos netos en el periodo.

## 📦 Requisitos y Ejecución

1. Instalar las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
