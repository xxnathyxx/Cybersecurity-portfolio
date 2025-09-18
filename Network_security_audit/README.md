# 🔐 Auditoría de Seguridad en Redes

Este repositorio contiene un proyecto práctico de **auditoría de seguridad en redes** realizado en un laboratorio controlado. Incluye escaneos, análisis de tráfico, resultados de escáner de vulnerabilidades y scripts de apoyo para automatizar partes del proceso.

---

## Estructura del repositorio

```
Auditoria-Seguridad-Redes/
│── README.md
│── notebook.ipynb
│── /docs
│    ├── informe_auditoria.pdf      # Reporte final (ejemplo/placeholder)
│    ├── checklist_auditoria.md
│── /scans
│    ├── nmap_scan.txt              # Resultados Nmap (ejemplo)
│    ├── vulnerabilidades.csv       # Export del escáner (ejemplo)
│── /scripts
│    ├── analisis_trafico.py        # Script en Python (ejemplo)
│    ├── generar_reporte.sh         # Automatización de reportes (ejemplo)
│── /lab
│    ├── docker-compose.yml         # Laboratorio de red simulado (ejemplo)
│    ├── traffic_sample.csv         # Muestra de tráfico para análisis
```

## Resumen del proyecto

- **Objetivo:** Identificar y documentar vulnerabilidades y malas configuraciones en una red simulada.
- **Metodología:** Reconocimiento (Nmap) → Escaneo de vulnerabilidades (OpenVAS/Nessus) → Captura y análisis de tráfico (Wireshark/Python) → Pruebas controladas de explotación → Informe y recomendaciones.
- **Herramientas:** Nmap, Wireshark, OpenVAS/Nessus, Metasploit (solo en entorno controlado), Docker/VirtualBox, Python.

---

## Cómo usar los archivos de ejemplo

1. Clona el repositorio.
2. Revisa los archivos en `/scans` y `/scripts` para ver ejemplos reales del trabajo realizado.
3. Abre `docs/checklist_auditoria.md` para ver la guía paso a paso usada durante la auditoría.
4. Ejecuta `python3 scripts/analisis_trafico.py --input lab/traffic_sample.csv` para obtener un análisis básico del tráfico de muestra.

---

> ⚠️ **Advertencia:** Todos los escaneos y pruebas contenidas en este repositorio fueron realizados en un entorno de laboratorio controlado. No realices pruebas de intrusión en redes ajenas sin autorización explícita.
