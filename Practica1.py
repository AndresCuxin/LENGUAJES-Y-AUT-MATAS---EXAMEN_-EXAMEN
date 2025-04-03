#esto_funciona
import re

# funcion que analiza un codigo fuente y genera una lista de tokens
def lexer(codigo):
    tokens = []  # lista para almacenar los tokens encontrados
    
    # definicion de patrones para reconocer diferentes tipos de tokens
    patrones = [
        (r'\bif\b', 'IF'),  # palabra clave if
        (r'\belse\b', 'ELSE'),  # palabra clave else
        (r'\bwhile\b', 'WHILE'),  # palabra clave while
        (r'\d+\.\d+', 'NUMERO_DECIMAL'),  # numero decimal
        (r'\d+', 'NUMERO_ENTERO'),  # numero entero
        (r'[a-zA-Z_]\w*', 'IDENTIFICADOR'),  # identificadores (variables, funciones)
        (r'\+', 'SUMA'),  # operador suma
        (r'\-', 'RESTA'),  # operador resta
        (r'\*', 'MULTIPLICACION'),  # operador multiplicacion
        (r'/', 'DIVISION'),  # operador division
    ]
    
    # eliminar comentarios de linea que inician con #
    codigo = re.sub(r'#.*', '', codigo)  
    
    # eliminar espacios en blanco al inicio y al final del codigo
    codigo = codigo.strip()  
    
    # recorrer la lista de patrones y buscar coincidencias en el codigo
    for patron, tipo in patrones:
        for match in re.finditer(patron, codigo):
            tokens.append((tipo, match.group()))  # agregar el token encontrado a la lista
    
    # ordenar la lista de tokens alfabeticamente por tipo de token
    tokens.sort()
    
    return tokens  # retornar la lista de tokens

#ejemplo_de_uso
codigo_prueba = "if x > 15: y = 3.14 * x # calculo"  # codigo de prueba

# ejecutar la funcion lexer e imprimir los tokens ordenados
for token in lexer(codigo_prueba):
    print(token)
