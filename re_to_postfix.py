def prec(c):
    precedence = {'|': 0, '^': 3, '*': 3, '+': 3, '?': 3, '/': 2, '-': 1, '¬': 1} 
    return precedence.get(c, -1)

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

def to_postfix(regex):
    regex = add_concatenation(regex)
    stack = []
    result = []

    for char in regex:
        if char.isalnum():  # letra o número o epsilon
            if( char == 'E'): result.append('ε')
            else: result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            if stack:
                stack.pop()
        elif char == '?':  # Manejo especial para ?
            result.append('ε')  # Agregar epsilon
            result.append('|')  
        else:  # Operador
            while stack and prec(char) <= prec(stack[-1]) and stack[-1] != '(':
                result.append(stack.pop())
            stack.append(char)

    while stack:
        if stack[-1] == '(':
            stack.pop()
        else:
            result.append(stack.pop())

    return ''.join(result)

fixedlines = []
for line in open("regular_expressions.txt"):
    fixedlines.append(line.replace(" ", "").replace("\n", ""))

for line in fixedlines:
    print("-----------------------------\nRegular Expresion:", line)
    print("Postfix: ",to_postfix(line))



#código base y referencia de: https://www.geeksforgeeks.org/convert-infix-expression-to-postfix-expression/