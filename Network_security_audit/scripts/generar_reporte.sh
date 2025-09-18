#!/usr/bin/env bash
# Script simple para agrupar resultados en un folder 'docs/report_<fecha>'
fecha=$(date +%F_%H%M)
out="docs/report_${fecha}"
mkdir -p "$out"
cp scans/nmap_scan.txt "$out/"
cp scans/vulnerabilidades.csv "$out/"
cp lab/traffic_sample.csv "$out/"
echo "Reporte generado en $out"
