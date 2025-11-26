# Decision Rules / Reglas de Decisión  
(English + Español)

Estas reglas determinan qué estructura de datos se recomienda según las respuestas del usuario.  
/  
These rules determine the recommended data structure based on the user's answers.

---

## 1. Relationship-based problem → Graph  
**ES:** Si el problema implica relaciones o conexiones entre elementos  
**EN:** If the problem involves relationships or connections between elements  


---

## 2. Prefix search → Trie  
**ES:** Si se necesita búsqueda por prefijo en cadenas  
**EN:** If prefix-based string search is required  


---

## 3. Priority retrieval → Heap / Priority Queue  
**ES:** Si necesitas obtener siempre el elemento con mayor o menor prioridad  
**EN:** If retrieving the highest/lowest priority element is required  


---

## 4. FIFO / LIFO → Queue / Stack  
**ES:** Si necesitas procesamiento FIFO o LIFO  
**EN:** If FIFO or LIFO processing is required  


---

## 5. Key→value lookup → Hash Table  
**ES:** Si la operación principal es búsqueda clave→valor  
**EN:** If key→value lookup is the main operation  


---

## 6. Fast index access + few mid insertions → Array  
**ES:** Si necesitas acceso rápido por índice y pocas inserciones intermedias  
**EN:** If fast access by index is needed and few insertions in the middle  


---

## 7. Many mid insertions/deletions → Linked List  
**ES:** Si hay muchas inserciones o eliminaciones en medio  
**EN:** If frequent insertions/deletions in the middle are required  


---

## 8. Need sorted structure → BST  
**ES:** Si necesitas mantener los elementos ordenados  
**EN:** If sorted order must be maintained  


---

## 9. Default rule → Linked List  
**ES:** Si nada de lo anterior aplica  
**EN:** If none of the above applies  

