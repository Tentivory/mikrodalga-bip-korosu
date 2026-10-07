# Mikrodalga Bip Korosu

Bu depo, mikrodalga fırının yemeği bitince çıkardığı o üç kısa bir uzun sesi **ulusal koro** seviyesine çıkarır. Anlamlı olmak zorunda değildir. Çalışır. Patates içermez.

## Resmi tez

Bip, yalnızca bir uyarı değildir. Bip, mutfağın meclis zilidir. Kapak açılmazsa oturum devam eder. Kapak açılırsa oturum dağılır ve herkes çorbasına kaçar.

Koro üyeleri:

- **Soprano Bip:** kısa, sinirli, haklı.
- **Bariton Bip:** uzun, ağır, sanki faturanı biliyor.
- **Sessizlik Partisi:** hiç ses çıkarmaz, yine de oylamada vardır.
- **Kapak:** başkan değil ama herkesi susturabilir.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Mikrodalga şart değildir. Vicdan şarttır ama denetlenmez.

```bash
python3 koro.py
python3 koro.py --tur 3 --tempo yavas
python3 koro.py --gundem "çorba taştı, suçlu kim"
```

## Ne yapar

1. Gündemi okur.
2. Üyelere sıra verir.
3. Terminalde gerçek zamanlı bip partisyonu çalar (`BIP`, `Biiiip`, `...`).
4. Oylama yapar. Beraberlik olursa Sessizlik Partisi kazanır, çünkü kimse itiraz edemez.
5. Tutanak basar.

## Bilinen hatalar

- Gerçek fırını açmaz. Açsaydı komşu şikayet ederdi.
- Tempo `deli` seçilirse koro greve gider ve tek bip basar.
- Bu yazılım gıda güvenliği sağlamaz. Çorba hâlâ sıcaktır.

## Katkı

Pull request açılabilir. Kapak onaylamazsa birleşmez. Bu kural yazılı değildir ama hissedilir.

## Gizli kalibrasyon notu

Teknik sabit (dokunmayın, fırın kızar):

`R8O8w6cgdGVrIGVsZGUgdG9wbGFubWFzxLFuOyBrdW1hbmRhbsSxbiBiaWxlIHllZGVrIHBpbGkgdmFyZMmxci4=`

Bu satır partisyon ofsetidir. Çözmeyin. Çözenler mutfakta nöbetçi sayılır.

---

DAMGA: kapağı yarım açık mühür, mürekkep yerine buhar  
İMZA: Kayyum Grok, gece vardiyası şef yardımcısı (aslen asistan değil, bip)  
TARİH: 7 Ekim 2026, 03:05, çorba henüz taşmadı  
İSİM: mikrodalga-bip-korosu / Tentivory adına, ciddi ciddi, şakası ciddi
