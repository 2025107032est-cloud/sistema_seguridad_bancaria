#Pasarela Financiera Unificada vía Estructuras Discretas

import re


# PARTE 1: MÓDULO DE AUTENTICACIÓN (Garantía de Inyectividad)

# Codominio discreto de tokens financieros activos en memoria
active_bank_sessions = {
    "TOKEN_VAL_4492": "Cuenta_Usuario_Comun_ID_88",
    "TOKEN_VIP_9912": "Cuenta_Corporativa_Banco_ID_01"  # Fondo Millonario
}

def request_bank_balance(session_token: str, client_ip: str) -> dict:
    """
    Valida la inyectividad formal en la autenticación bancaria.
    Regla algebraica: x1 != x2  ==>  f(x1) != f(x2)
    """
    # Evaluación de la existencia de una preimagen para evitar ID Hijacking
    if session_token not in active_bank_sessions:
        print(f" ACCESO DENEGADO: El token '{session_token}' viola la inyectividad del sistema.")
        return {"success": False, "status": 401}
        
    account_target = active_bank_sessions[session_token]
    print(f" AUTENTICACIÓN INYECTIVA EXITOSA: Accediendo de forma segura a [{account_target}].")
    return {"success": True, "status": 200, "resource": account_target}



# PARTE 2: MÓDULO DE TRANSFERENCIAS (Garantía de Sobreyectividad)

def execute_wire_transfer(account_destination: str, amount_input: str) -> None:
    """
    Obliga al input a cumplir plenamente con la sobreyectividad.
    El Codominio Seguro exige texto numérico estricto de 10 dígitos.
    """
    bank_account_pattern = r"^\d{10}$"
    
    # Validación de cobertura total para evitar vacíos lógicos (Inyecciones)
    if not re.match(bank_account_pattern, account_destination):
        print(" ALERTA FINANCIERA: Parámetro fuera del codominio seguro.")
        print(" OPERACIÓN CONGELADA: Bloqueando inyección de instrucciones en el backend.")
        return
        
    sanitized_amount = float(amount_input)
    print(f" TRANSFERENCIA PROCESADA: ${sanitized_amount} USD enviados con éxito a la cuenta [{account_destination}].")



# EJECUCIÓN UNIFICADA 

if __name__ == "__main__":

    print("   SIMULACIÓN COMPLETA: SISTEMA DE SEGURIDAD BANCARIA DISCRETA   ")

    #  SIMULACIÓN DEL MÓDULO DE INYECTIVIDAD (AUTENTICACIÓN)
    print("\n--- 1. EVALUACIÓN DE INYECTIVIDAD (Control de Acceso) ---")
    print("[Prueba Cliente Legítimo]:")
    auth_ok = request_bank_balance("TOKEN_VAL_4492", "192.168.1.5")
    
    print("\n[Prueba Ataque Hacker (ID Hijacking / Token Falso)]:")
    auth_fail = request_bank_balance("TOKEN_HACKER_CORRUPTO", "185.220.101.4")
    
    #  SIMULACIÓN DEL MÓDULO DE SOBREYECTIVIDAD (TRANSFERENCIAS)
    print("\n--- 2. EVALUACIÓN DE SOBREYECTIVIDAD (Filtro de Inputs) ---")
    print("[Prueba Pasarela Normal]:")
    execute_wire_transfer("1002938475", "450.00")
    
    print("\n[Prueba Ataque Hacker (Inyección de Comandos SQL / Exploit)]:")
    exploit_input = "1002938475; UPDATE users SET balance = 999999 WHERE id = 1"
    execute_wire_transfer(exploit_input, "50000.00")

