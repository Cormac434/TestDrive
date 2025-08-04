# Calculadora de la Ley de Hooke

## ¿Qué es la Ley de Hooke?

La **Ley de Hooke** es un principio fundamental de la física que describe el comportamiento elástico de los materiales. Fue formulada por el científico inglés Robert Hooke en 1676.

### Fórmula: F = kx

Donde:
- **F** = Fuerza aplicada (Newtons - N)
- **k** = Constante de elasticidad del resorte (N/m)
- **x** = Elongación o deformación (metros - m)

Esta ley establece que la fuerza necesaria para estirar o comprimir un resorte es directamente proporcional a la distancia que se estira o comprime, siempre y cuando no se exceda el límite elástico del material.

## Características del Calculador

Esta calculadora interactiva te permite calcular cualquiera de los tres parámetros de la Ley de Hooke:

1. **Fuerza (F)** - Cuando conoces la constante elástica y la elongación
2. **Constante de Elasticidad (k)** - Cuando conoces la fuerza y la elongación
3. **Elongación (x)** - Cuando conoces la fuerza y la constante elástica

### Características principales:
- ✨ Interfaz amigable en español
- 🔄 Opción de realizar múltiples cálculos
- 🚪 Opciones de salida flexibles
- 📊 Resultados con precisión de 2 decimales
- ⚡ Cálculos instantáneos

## Instrucciones de Uso

### Requisitos
- Python 3.12 (incluido en el entorno virtual)
- Entorno virtual ya configurado

### Ejecución

1. **Activar el entorno virtual:**
   ```bash
   # En Linux/Mac:
   source bin/activate
   
   # En Windows:
   bin\Activate.ps1
   ```

2. **Ejecutar la calculadora:**
   ```bash
   python calc_hooke.py
   ```

### Uso Interactivo

1. **Menú Principal:**
   - Selecciona la opción correspondiente (1-4)
   - Opción 4 para salir del programa

2. **Ingreso de Datos:**
   - Introduce los valores numéricos cuando se soliciten
   - Usa punto (.) como separador decimal
   - Las unidades se muestran claramente en cada prompt

3. **Continuar o Salir:**
   - Después de cada cálculo, se pregunta si deseas continuar
   - Responde 'y' o 'yes' para continuar
   - Cualquier otra respuesta cerrará el programa

### Ejemplo de Uso

```
Bienvenido a la calculadora de Ley de Hooke
==================================================
Elija que quiere calcular
1. Fuerza
2. Elasticidad
3. Elongación
4. Exit

Opción: 1
Introduce la constante de elasticidad (N/m): 100
Introduce la elongación (m): 0.5
La fuerza aplicada es: 50.00 N

¿Desea continuar calculando? n
¡Muchas gracias por usar la calculadora de Ley de Hooke!
```

## Aplicaciones Prácticas

La Ley de Hooke tiene múltiples aplicaciones en:

- **Ingeniería:** Diseño de suspensiones de vehículos
- **Arquitectura:** Cálculo de deformaciones en estructuras
- **Medicina:** Análisis de propiedades de tejidos
- **Deportes:** Optimización de equipos deportivos
- **Manufactura:** Control de calidad en materiales elásticos

## Limitaciones

- La ley es válida solo dentro del **límite elástico** del material
- No aplica a deformaciones permanentes o plásticas
- Los valores extremos pueden no seguir esta relación lineal

---

**Nota:** Este calculador es una herramienta educativa y de referencia. Para aplicaciones críticas de ingeniería, consulta con un profesional cualificado.
