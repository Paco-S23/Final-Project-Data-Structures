# Example Task / Ejemplo Basado en Actividad del Curso  
(English + Español)

Este ejemplo se basa en una actividad típica del curso e ilustra cómo se justifica una estructura de datos según los requerimientos.  
/  
This example is based on a typical course activity and shows how to justify a data structure according to the requirements.

---

# 1. Problem Description / Descripción del Problema

## ENGLISH  
We want to build a simple system to manage a list of students' grades.  
The main operations required are:

1. Insert a grade  
2. Delete a grade located in the middle  
3. Traverse all grades in order  
4. Update a grade at a given position  

Because insertions and deletions in the middle are frequent, the best data structure for this case is a **Linked List**.

## ESPAÑOL  
Queremos construir un sistema para gestionar una lista de calificaciones de estudiantes.  
Las operaciones principales necesarias son:

1. Insertar una calificación  
2. Eliminar una calificación ubicada a media lista  
3. Recorrer todas las calificaciones en orden  
4. Actualizar una calificación en una posición dada  

Debido a que hay inserciones y eliminaciones frecuentes en posiciones intermedias, la mejor estructura de datos para este caso es una **Lista Ligada (Linked List)**.

---

# 2. Why This Structure? / ¿Por Qué Esta Estructura?

## ENGLISH  
- Linked Lists support **O(1)** insertions and deletions when the position is known.  
- The number of middle modifications is high.  
- Random access is *not* the main operation.  
- The size of the list grows dynamically.

## ESPAÑOL  
- Las Listas Ligadas permiten inserciones y eliminaciones en **O(1)** cuando la posición es conocida.  
- Hay muchas modificaciones en posiciones intermedias.  
- El acceso aleatorio *no* es la operación principal.  
- El tamaño de la lista crece dinámicamente.

---

# 3. Pseudocode (Aligned with app.py)  
# Pseudocódigo (Alineado con la aplicación)

---

# 4. Step-by-Step Example / Ejemplo Paso a Paso

## ENGLISH  
Initial State  

Step 1 — Insert 80  

Step 2 — Insert 95  

Step 3 — Insert 70  

Step 4 — Delete 95  

**Final Result:**  

---

## ESPAÑOL  
Estado Inicial  

Paso 1 — Insertar 80  

Paso 2 — Insertar 95  

Paso 3 — Insertar 70  

Paso 4 — Eliminar 95  

**Resultado Final:**  

---

# 5. Scaling Discussion / Discusión de Escalabilidad

## ENGLISH  
- With 1,000,000 elements, insertions remain efficient (O(1)).  
- Searching becomes O(n), which is expected for a linked list.  
- If random index access becomes necessary, switching to a Dynamic Array might be more appropriate.

## ESPAÑOL  
- Con 1,000,000 elementos, las inserciones siguen siendo eficientes (O(1)).  
- Las búsquedas se vuelven O(n), lo cual es normal en listas ligadas.  
- Si el acceso por índice fuera necesario, sería mejor usar un Arreglo Dinámico.

---
