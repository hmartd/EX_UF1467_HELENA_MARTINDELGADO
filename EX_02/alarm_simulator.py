def alarm_simulator(total_time):
    """
    Simula una alarma que cuenta los segundos hasta llegar al segundo total_time. La alarma se pausa cada 10 segundos.
    """
    current_second = 0
    contador = 0

    while current_second <= total_time:
        current_second += 1
        if current_second == total_time:
            print(f"La alarma ha sido desactivada. Ha estado {contador} segundos activa")
            break
        if current_second % 10 == 0:
            print(f"La alarma se ha pausado. Se ha omitido el segundo {current_second}")
            continue
        else:
            print(f'La alarma está activada. Segundo actual: {current_second}')
            contador += 1

alarm_simulator(24)