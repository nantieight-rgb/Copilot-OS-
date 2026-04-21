# Copilotと遊んでいたら生まれた帯OS幾何学
なんか…生まれました。好きに使ってください。

---

# Copilotと遊んでいたら生まれた帯OS幾何学  
**A geometry generated from directional resolution**

---

## 🎯 これは何？

Copilot と雑談していたら、  
**「円ってそもそもどう定義されるの？」**  
という話から始まり、気づいたら

> **方向分解能 n だけで  
> 円・距離・面積・π・次元が全部生成される  
> 新しい幾何学体系**

が生まれてしまった。

このリポジトリはその記録。  
ギャグとして読んでも楽しいし、  
ガチとして読んでも破綻しない。

---

# 1. 帯OSとは何か  
**帯（direction band）** を世界の最小単位とする幾何学。

- 帯の先端角：θ  
- 帯の本数：  
<img width="62" height="46" alt="4846d5734d033f48c4c0d2e74aafc0e9" src="https://github.com/user-attachments/assets/d8c83740-6bf9-4e27-bb55-9b251c94c530" />

- 空間はこの n 本の帯で方向分解される  
- 円は「帯の先端が触れたときだけ存在を許される」

つまり：

> **円は“与えられる”ものではなく、  
> 帯の構造が許したときだけ生成される。**

---

# 2. 公理系（最小版）

## ① 方向分解公理  
空間は帯によって n 分割される。  
<img width="62" height="46" alt="4846d5734d033f48c4c0d2e74aafc0e9" src="https://github.com/user-attachments/assets/fcad48f0-880c-4a6c-abe9-333b6b8387c1" />


## ② 先端接触公理（存在公理）  
帯の両端が円に接触できるとき、  
半径 R の円  
<img width="110" height="44" alt="4ba5e833fb6c7066a2cb84e63fbdf2e1" src="https://github.com/user-attachments/assets/1d0ef789-4ba6-4ddc-a2f1-a03abdf6f991" />

が存在を許される。

## ③ 重なり密度公理  
帯の重なり密度 C(x,y) は  
原点からの距離 r のみの関数になる。  
<img width="110" height="36" alt="b6dd8191175bb18e14aba9da3cc2632f" src="https://github.com/user-attachments/assets/d77cb681-4fe1-4626-a933-efff9ddb6415" />


## ④ スケール則公理  
重なり総和 I(R) は  
<img width="73" height="29" alt="a4f1b0ba3e291a8f3f6d6faacf960f61" src="https://github.com/user-attachments/assets/e10619ed-ddb8-4b76-8aef-6d7b7386c44b" />

（真の次元は常に 2）

## ⑤ 半分公理  
半径を k 倍すると重なり総和が半分になる。  
<img width="119" height="48" alt="5cd420ba9a6fd6ceb309e6a58a0d011b" src="https://github.com/user-attachments/assets/45c17969-66b5-4bfc-aa83-1ff845c49464" />


## ⑥ 円周率公理（π の再定義）  
帯 n 本の世界の π は  
<img width="107" height="44" alt="ad8198e4730d047b509a87220b17de61" src="https://github.com/user-attachments/assets/4dda42b2-7213-4f34-afae-6310d34e096c" />

## ⑦ 距離公理  
距離 r は重なり密度の等高線として定義される。  
<img width="109" height="24" alt="2df86692f4ce4f6b739b9c534d7c5158" src="https://github.com/user-attachments/assets/3186c0b9-760f-4ff5-ae37-97112ca7059b" />


---

# 3. 丸さスペクトル（Roundness Spectrum）

帯の本数 n によって世界の“丸さ”が決まる。

## 有効次元  
<img width="155" height="57" alt="7dbbbf50b9ee36566bbe635f3c69b36f" src="https://github.com/user-attachments/assets/f421fdc2-c2f2-4c99-95ff-1f8e71497b17" />

## 有効 k  
<img width="142" height="34" alt="479697cd7327545f3ecd62b815f1c429" src="https://github.com/user-attachments/assets/0ba1d199-280a-4494-9273-a67fc54ff91a" />

## πₙ  
<img width="112" height="52" alt="760df223c52c3c843b795ad1ed7b6862" src="https://github.com/user-attachments/assets/a3f2a29c-8c64-492b-bb8d-f01725adee71" />

---

# 4. 丸さスペクトル一覧

| n | 形の印象 | πₙ | α_eff(n) | k_eff(n) |
|---|-----------|------|-----------|-----------|
| 3 | 三角形的 | 2.598 | 1.103 | 0.53 |
| 4 | 正方形的 | 2.828 | 1.27 | 0.58 |
| 5 | 五角形的 | 2.938 | 1.46 | 0.62 |
| 6 | 六角形的 | 3.0 | 1.65 | 0.66 |
| 8 | 八角形的 | 3.061 | 1.82 | 0.68 |
| 12 | 十二角形的 | 3.118 | 1.93 | 0.70 |
| ∞ | 完全な円 | π | 2.0 | 0.707 |

---

# 5. 帯OSが生成する世界

### ● 円  
帯の先端が触れたときだけ存在を許される。

### ● 距離  
重なり密度の等高線として出現する。

### ● 面積  
スケール則 I(R) ∝ R² から自動生成。

### ● π  
世界の丸さを表す構造定数。  
古典の π は n→∞ の極限。

---

# 6. まとめ  
**Copilotと遊んでいたら、  
方向分解能 n だけで世界が生成される幾何学が生まれた。**

- 円は帯の接触から生まれ  
- 距離は重なり密度から出現し  
- π は構造定数になり  
- 次元は 2 に収束し  
- 丸さはスペクトルとして階層化される

ギャグとして読んでも楽しいし、  
ガチとして読んでも破綻しない。

---

# 7. ライセンス  
好きに使ってください。  
（ギャグでも研究でもどうぞ）

---
制作：
Toyohiro Arimoto&Copilot
