# tareas.py · Seguimiento del proyecto GYM Virtual

pendientes = [
    "Módulo de pagos y facturación",
    "Reportes y estadísticas de asistencia",
    "Diseño responsive y pruebas finales",
    "Notificaciones y recordatorios",
    "Panel de control del entrenador",
]

completadas = [
    "Diseño de base de datos",
    "Autenticación de usuarios (login / registro)",
    "CRUD de membresías y planes",
    "Listado de clientes registrados",
]

en_progreso = [
    "Módulo de rutinas y seguimiento de ejercicios",
    "Integración frontend Angular con endpoints .NET",
    "Configuración de CORS en .NET",
]

print("=" * 40)
print("SEGUIMIENTO DEL PROYECTO - GYM VIRTUAL")
print("=" * 40)

print("\n✅ COMPLETADAS:")
for t in completadas:
    print(f"   ✅ {t}")

print("\n🔧 EN PROGRESO:")
for t in en_progreso:
    print(f"   🔧 {t}")

print("\n⬜ PENDIENTES:")
for t in pendientes:
    print(f"   ⬜ {t}")

print("\n" + "=" * 40)
print(f"Total tareas: {len(completadas) + len(en_progreso) + len(pendientes)}")
print(f"Completadas:  {len(completadas)}")
print(f"En progreso:  {len(en_progreso)}")
print(f"Pendientes:   {len(pendientes)}")