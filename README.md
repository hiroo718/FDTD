# FDTD Sound Field Analysis

**有限差分時間領域法による音場解析 / Sound Field Analysis using Finite-Difference Time-Domain Method**

---

## 概要 / Overview

**日本語**

有限差分時間領域法（FDTD法）を用いた2次元音場シミュレーションです。
シンプルな実装を心がけており、音響工学を学ぶ方の参考になることを目的としています。

**English**

This is a 2D sound field simulation using the Finite-Difference Time-Domain (FDTD) method.
The code is intentionally kept simple and readable, making it ideal for those learning acoustics and numerical simulation.

---

## 特徴 / Features

- シンプルで読みやすいコード / Simple and readable code
- 物理の式がそのままコードに反映 / Physics equations directly mapped to code
- インピーダンス境界条件 / Impedance boundary conditions
- 音場の可視化（カラーマップ）/ Sound field visualization (colormap)

---

## 必要環境 / Requirements

```
Python 3.x
numpy
scipy
matplotlib
```

---

## 使い方 / Usage

```bash
python fdtd.py
```

---

## パラメータ / Parameters

| パラメータ | 値 | 説明 |
|---|---|---|
| `f` | 1000 Hz | 周波数 / Frequency |
| `C` | 343 m/s | 音速 / Speed of sound |
| `ro` | 1.21 kg/m³ | 空気密度 / Air density |
| `N` | 5000 | タイムステップ数 / Number of time steps |
| `X`, `Y` | 40, 30 | グリッドサイズ / Grid size |

---

## 結果例 / Result Example

音源は `P[20,15]`（グリッド中央付近）に配置。コサイン波で励振した場合の音場分布です。

The sound source is placed at `P[20,15]` (near the center of the grid), excited by a cosine wave.

![Sound field](sound_field.png)

---

## 参考 / References

- Yee, K. S. (1966). Numerical solution of initial boundary value problems involving Maxwell's equations in isotropic media. *IEEE Transactions on Antennas and Propagation*.
- Taflove, A. & Hagness, S. C. (2005). *Computational Electrodynamics: The Finite-Difference Time-Domain Method*.

---

## 作者 / Author

**Dr. H. Yamazaki**
June 7th, 2020

---

## ライセンス / License

MIT License
