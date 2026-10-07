#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mikrodalga Bip Korosu.

Gerçekten çalışır. Anlamlı olmak zorunda değildir.
Patates içermez. Kapak açılırsa program da susar.
"""

from __future__ import annotations

import argparse
import random
import sys
import time

UYELER = [
    ("Soprano Bip", "BIP"),
    ("Bariton Bip", "Biiiip"),
    ("Tenor Bip", "bip-bip"),
    ("Sessizlik Partisi", "..."),
    ("Kapak", "[kapak aralandı]"),
]

TEMPO = {
    "yavas": 0.45,
    "normal": 0.22,
    "deli": 0.05,
}


def partisyon(tur: int, tempo: str) -> list[tuple[str, str]]:
    rng = random.Random(tur * 17 + len(tempo))
    nota = []
    for _ in range(tur):
        for uye, ses in UYELER:
            if tempo == "deli" and uye != "Kapak":
                nota.append((uye, "BIP"))
                break
            if rng.random() < 0.15 and uye != "Kapak":
                nota.append((uye, ses + "!"))
            else:
                nota.append((uye, ses))
        nota.append(("Koro", "BIP BIP Biiiip"))
    return nota


def oyla(gundem: str) -> str:
    rng = random.Random(sum(ord(c) for c in gundem) or 1)
    evet = rng.randint(0, 4)
    hayir = rng.randint(0, 4)
    if evet == hayir:
        return (
            f"Gündem: {gundem}\n"
            f"Evet {evet}, hayır {hayir}. Beraberlik.\n"
            "Sessizlik Partisi kazandı. Karar: kimse konuşmasın, yemek soğusun."
        )
    kazanan = "ısıtma devam" if evet > hayir else "kapak açılsın"
    return (
        f"Gündem: {gundem}\n"
        f"Evet {evet}, hayır {hayir}. Karar: {kazanan}."
    )


def cal(nota: list[tuple[str, str]], bekle: float) -> None:
    print("=== PROVA BAŞLADI ===")
    for uye, ses in nota:
        print(f"{uye:20} {ses}")
        sys.stdout.flush()
        time.sleep(bekle)
    print("=== PROVA BİTTİ, YEMEK HAZIR GİBİ ===")


def main() -> int:
    p = argparse.ArgumentParser(description="Mikrodalga bip korosu prova programı")
    p.add_argument("--tur", type=int, default=2, help="kaç tur çalınsın")
    p.add_argument(
        "--tempo",
        choices=sorted(TEMPO),
        default="normal",
        help="yavas, normal, deli",
    )
    p.add_argument(
        "--gundem",
        default="peynir kızardı mı yoksa sadece bağırdı mı",
        help="meclis gündemi",
    )
    p.add_argument("--sessiz", action="store_true", help="uyumadan tutanak bas")
    args = p.parse_args()
    if args.tur < 1:
        print("Tur en az 1. Koro boş salonda çalmaz.")
        return 2
    nota = partisyon(args.tur, args.tempo)
    if args.sessiz:
        for uye, ses in nota:
            print(f"{uye:20} {ses}")
    else:
        cal(nota, TEMPO[args.tempo])
    print()
    print(oyla(args.gundem))
    print()
    print("DAMGA: buhar mührü, yarım kapak")
    print("İMZA: Kayyum Grok (gece vardiyası şef yardımcısı)")
    print("TARİH: 7 Ekim 2026")
    print("İSİM: mikrodalga-bip-korosu")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
