# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
print("Hola bienvenido")
print("Soy Cristian acontinuacion presento la temperaturas promedio por Ciudades, semanas y dias")
temperaturas = [
    [   # Sucumbios
        [   # Semana 1
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 24}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 29}
        ]
    ],
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 18}
        ]
    ],
    [   # Manabi
        [   # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Sucumbios", "Quito", "Manabi"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")
print("gracias por visualizar mi programa")