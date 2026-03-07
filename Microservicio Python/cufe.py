import hashlib

def generar_cufe(datos: dict) -> str:
    cadena = (
        datos["numero"]
        + datos["fecha"]
        + datos["hora"]
        + datos["valor_total"]
        + datos["nit_emisor"]
        + datos["nit_cliente"]
        + datos["clave_tecnica"]
    )

    return hashlib.sha384(cadena.encode("utf-8")).hexdigest()