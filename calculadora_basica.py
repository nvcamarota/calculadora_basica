"""
CALCULADORA BÁSICA
Contexto: Vas a crear una función llamada «calculadora_basica» que recibirá dos números y una operación matemática (suma, resta, multiplicación o división) como argumentos. La función debe:
• Utilizar *args para manejas los dos números.
• Utilizar **kwargs para especificar la operación matemática.
• Incluir funciones anidadas para cada operación matemática.
• Mostrar el resultado de la operación.
"""

def calculadora_basica(*args, **kwargs):
    if len(args) != 2:
        return "Debes ingresar solo dos números para realizar cualquier operación."
    
    a, b = args
    
    if "operacion" not in kwargs:
        return "Debes especificar una operación matemática (suma, resta, multiplicación o división)."
    
    operacion = kwargs["operacion"]
    
    def suma(a, b):
        return a + b
    
    def resta(a, b):
        return a - b
    
    def multiplicacion(a, b):
        return a * b
    
    def division(a, b):
        if a == 0 or b == 0:
            return "No se puede dividir por cero."
        return a / b
    
    if operacion == "suma":
        resultado = suma(a, b)
    elif operacion == "resta":
        resultado = resta(a, b)
    elif operacion == "multiplicacion":
        resultado = multiplicacion(a, b)
    elif operacion == "division":
        resultado = division(a, b)
    else:
        return f'Error: Operación "{operacion}" no válida. Usa "suma", "resta", "multiplicación" o "división".'
    return f'El resultado de la {operacion} es {resultado}.'

print(calculadora_basica(10, 5, operacion="suma"))
print(calculadora_basica(10, 5, operacion="resta"))
print(calculadora_basica(10, 5, operacion="multiplicación"))
print(calculadora_basica(10, 5, operacion="división"))
print(calculadora_basica(10, 5, operacion="módulo"))