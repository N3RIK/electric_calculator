U = 220
P = None
I = 10
R = None

def calculate_electric():
    global U, P, I, R  
    
    if P is None:
        if U is not None and I is not None:
            P = U * I
        elif R is not None and U is not None:
            P = U ** 2 / R
        elif I is not None and R is not None:
            P = I ** 2 * R
    
    if I is None:
        if P is not None and U is not None:
            I = P / U
        elif U is not None and R is not None:
            I = U / R
        elif P is not None and R is not None:
            I = (P / R) ** 0.5
    
    if U is None:
        if P is not None and I is not None:
            U = P / I
        elif I is not None and R is not None:
            U = I * R
        elif P is not None and R is not None:
            U = (P * R) ** 0.5
    
    if R is None:
        if U is not None and P is not None:
            R = U ** 2 / P
        elif U is not None and I is not None:
            R = U / I
        elif P is not None and I is not None:
            R = P / (I ** 2)
    
    return {
        'Мощность (P)': f"{P if P is not None else 'Неизвестно'} Вт",
        'Сила тока (I)': f"{I if I is not None else 'Неизвестно'} А",
        'Напряжение (U)': f"{U if U is not None else 'Неизвестно'} В",
        'Сопротивление (R)': f"{R if R is not None else 'Неизвестно'} Ом"
    }

# Вычисляем и выводим результаты
results = calculate_electric()
for param, value in results.items():
    print(f"{param}: {value}")