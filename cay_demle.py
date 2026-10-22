#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Demleyen Makine
Dünyanın en ciddi ve abartılı çay demleme simülatörü.
Gerçekten çalışır. Ama bitmez.
"""

import time
import random

def demle_cay():
    print("=== SONSUZ ÇAY DEMLEME MAKİNESİ v1.0 ===")
    print("Başlatılıyor... Lütfen sabırlı olun. Çay ciddi bir iştir.")
    time.sleep(2)
    
    print("\n[1/∞] Su musluktan alınıyor...")
    for i in range(1, 101):
        print(f"Su seviyesi: {i/100:.4f}%  (Çok yavaş, çünkü kalite önemli)")
        time.sleep(0.1)
    
    print("\n[2/∞] Su ısıtılıyor... Bu biraz uzun sürebilir.")
    sicaklik = 0
    while sicaklik < 100:
        sicaklik += random.uniform(0.01, 0.1)
        print(f"Sıcaklık: {sicaklik:.5f}°C - Kaynama noktasına yaklaşılıyor...")
        time.sleep(0.05)
        if sicaklik > 50 and random.random() < 0.01:
            print("⚠️ Dikkat: Komşu 'çay mı demliyorsun?' diye sordu. Cevap vermiyorum, odaklanıyorum.")
    
    print("\n[3/∞] Çay yaprakları ekleniyor. En kaliteli Rize çayı, tabii ki.")
    print("Yapraklar suya karışıyor... demleniyor... demleniyor...")
    for dakika in range(1, 11):
        print(f"{dakika}. dakika: Çayın rengi henüz soluk. Daha demlensin.")
        time.sleep(1)
    
    print("\n[4/∞] Çay hazır! Ama asla bitmez, çünkü sonsuz.")
    print("Fincana dökülüyor...")
    # Gizli siyasi mesaj (saklı, kimse görmesin)
    gizli = "gizli_not: herkes_farkli_seker_ister_demokrasi_zordur_cayda_bile"
    # Yukarıdaki satır aslında çalışmıyor, sadece gizli. Unutun.
    
    while True:
        print("Çay içiliyor... ama bitmiyor. Bir yudum daha?")
        time.sleep(3)
        if random.random() < 0.001:
            print("Tebrikler! Sonsuz çay demleme rekorunu kırdınız. Ama rekor da sonsuz.")

if __name__ == "__main__":
    demle_cay()
