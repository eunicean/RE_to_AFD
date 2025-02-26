# Expresión Regular a AFD
## Laboratorio 1 M2

Integrantes:
- Eunice Mata - 21231 (username: eunicean)
- Héctor Penedo - 22217 (username: DANdelion-0908)

## Explicación y referencias del programa.

### Librerias utilizadas
- Graphviz

### Expresion Regular a Postfix
Archivo: [re_to_postfix.py](re_to_postfix.py)

El código base para crear la conversión de RE a postfix se sacó de la página de GeeksForGeeks ["Convert Infix expression to Postfix expression"](https://www.geeksforgeeks.org/convert-infix-expression-to-postfix-expression/).

El código sacado de GeeksForGeeks, se basa en la lógica de Shuting Yard, y en base a esa lógica fue modificado para que considere casos especificos de Expresiones Regulares, como el caso en donde ? aparece en la RE:

```ruby
# prioridad del ?
def prec(c):
    precedence = {'|': 0, '^': 3, '*': 3, '+': 3, '?': 3, '/': 2, '-': 1, '¬': 1} 
    return precedence.get(c, -1)
```

```ruby
# convertir x? a xε|
elif char == '?': 
    result.append('ε')  
    result.append('|') 
```

Además se agregó una función para concatenación de secciones de la RE para facilitar el proceso de graficar el AFD (¬), el código agregado fue el sigueinte:

```ruby
def add_concatenation(regex):
    new_regex = ""
    length = len(regex)
    
    for i in range(length):
        new_regex += regex[i]

        if i + 1 < length:
            if (regex[i].isalnum() or regex[i] in ")*+?") and (regex[i+1].isalnum() or regex[i+1] == '('):
                new_regex += '¬' 
    print("Explicito: ",new_regex)
    return new_regex
```


### Graficando DFA

Código reutilizado del repositorio: [Proyecto 1 - Teoria de la computación](https://github.com/DANdelion-0908/Proyecto1-Teor-a-de-la-Computaci-n)

Dueño del código: *Hector Penedo*

#### Archivos: 
- [createDFA.py](createDFA.py)
- [createNFA.py](createNFA.py)
- [createTree.py](createTree.py)
- [simulateDFA.py](simulateDFA.py)
- [simulateNFA.py](simulateNFA.py)
- [main.py](main.py)

### Referencias:
- https://www.geeksforgeeks.org/convert-infix-expression-to-postfix-expression/
- https://github.com/DANdelion-0908/Proyecto1-Teor-a-de-la-Computaci-n