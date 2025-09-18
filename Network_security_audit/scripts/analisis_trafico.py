#!/usr/bin/env python3
"""
analisis_trafico.py

Script de ejemplo para analizar un CSV simplificado de tráfico de red.
Genera:

- Top 5 de IPs fuente (top talkers)
- Distribución por protocolo
- Eventos sospechosos simples (p.ej., paquetes ICMP inusuales o tamaños muy grandes repetidos)
"""

import argparse
import pandas as pd

def load_data(path):
    df = pd.read_csv(path, parse_dates=["timestamp"])
    return df

def top_talkers(df, n=5):
    counts = df['src_ip'].value_counts().head(n)
    return counts

def protocol_distribution(df):
    return df['protocol'].value_counts(normalize=True) * 100

def suspicious_events(df):
    events = []
    # ICMP packets (could indicate ping sweeps)
    icmp = df[df['protocol'].str.upper()=='ICMP']
    if len(icmp) > 5:
        events.append(f"High number of ICMP packets: {len(icmp)}")
    # Large repeated TCP packets (simple heuristic)
    large_tcp = df[(df['protocol'].str.upper()=='TCP') & (df['length']>1400)]
    ip_counts = large_tcp['src_ip'].value_counts()
    for ip, cnt in ip_counts.items():
        if cnt > 1:
            events.append(f"Host {ip} sent {cnt} large TCP packets (>1400 bytes) — investigate for possible exfiltration or transfer")
    return events

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="CSV de tráfico (lab/traffic_sample.csv)")
    args = parser.parse_args()

    df = load_data(args.input)
    print("Top talkers (top 5):")
    print(top_talkers(df))
    print("\nDistribución por protocolo (%):")
    print(protocol_distribution(df))
    print("\nEventos sospechosos detectados:")
    for e in suspicious_events(df):
        print("- " + e)

if __name__ == "__main__":
    main()

