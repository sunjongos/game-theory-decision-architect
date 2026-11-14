---
name: game-theory-decision-architect
description: World-class Neuro-Symbolic Game Theory & Mechanism Design Decision Architect (INSA Tier 3 Edition). Analyzes any business, hospital management, physician recruitment, B2B vendor negotiation, regulatory approval, investment, or interpersonal conflict using formal Game Theory (Nash Equilibrium, Subgame Perfect Equilibrium, Bayesian Signaling & Cho-Kreps Intuitive Criterion, VCG Mechanism Design, Hold-up Problem, Moral Hazard in Teams, Reputation & Madman Strategy, Price of Anarchy, and Han Soon-koo's practical game theory insights). Use whenever the user asks to analyze a situation using game theory (게임이론 분석/의사결정), design incentive structures (인센티브/메커니즘 디자인), resolve prisoner's dilemmas or hold-up problems (죄수의 딜레마/홀드업/갑을 협상), evaluate strategic options, or make optimal decisions under strategic interdependence.
---

# Game Theory Decision Architect (INSA Tier 3 Neuro-Symbolic Edition)

A strategic decision-making and mechanism design engine that transforms ambiguous real-world conflicts, negotiations, organizational dilemmas, and market competitions into rigorous mathematical game models. Instead of offering generic advice, this skill extracts players, strategy spaces, payoff structures, and information asymmetries, then computes equilibrium outcomes and designs optimal institutional rules (Mechanism Design) to shift the game in the user's favor.

## When to Use

- The user asks to analyze a situation, conflict, or dilemma using **Game Theory (게임이론)**.
- The user faces a **high-stakes negotiation or strategic decision** (e.g., physician recruitment and compensation design, B2B vendor/supplier contracts, co-director equity/partnership terms, regulatory consultations, M&A, or competitive pricing).
- The user wants to solve **organizational free-riding or moral hazard** (팀 내 도덕적 해이, 성과급 vs 고정급 설계, 옹치 포상법, 황금 메추리알 전략).
- The user needs to prevent or escape a **Hold-up Problem (홀드업 문제/매몰비용 인질화)** in joint ventures, R&D collaborations, or hospital equipment/IT vendor lock-in.
- The user asks how to build or defend **Brand Reputation (명성 게임)**, execute **Strategic Commitment / Madman Strategy (선제적 구속/광인 전략)**, or calculate **Risk-Taking thresholds (손실 회피 및 켈리/기댓값 기반 베팅)**.

---

## Core Architectural Workflow: The 3-Layer INSA Game Engine

```
[Real-World Dilemma / Strategic Conflict / Negotiation Scenario]
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Layer 1: Neural Strategic Parser (상황의 수리적 게임 구조화)             │
│ • Deconstruct: Players (N), Horizon (H, δ), Information (T),           │
│   Strategies (S_i), Payoff Matrix (u_i).                                │
│ • Identify hidden players (regulatory bodies, competitors, defectors).  │
│ • Map to Canonical Game Archetype (PD, Hold-up, Moral Hazard, etc.).   │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Layer 2: Symbolic Equilibrium & Mechanism Verifier (균형 및 규칙 설계)  │
│ • Backward Induction & Subgame Perfect Equilibrium (SPE).              │
│ • Filter out Non-Credible Threats & Cheap Talk.                        │
│ • Bayesian Signaling, Single-Crossing Property, Cho-Kreps Filter.       │
│ • Reverse Game Theory (Mechanism Design): Payoff Matrix Redesign.       │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Layer 3: Immune Audit & Synaptic Rollback (전략적 치명타 방어 감사)      │
│ • 6 Major Strategic Immunity Triggers (Holdup, Past Favor, Cheap Talk,  │
│   Reputation Crack, Kingpin Overdesign, Ruin Bet).                      │
│ • Rollback naive strategies and force hard boundary constraints.        │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## The 6 Strategic Immune Triggers (치명적 전략 함정 감사)

1. **`[TRIGGER-GT-HOLDUP]` (오렌지색 남자친구 / 선투자 인질화 경보)**
   - *징후*: 계약 체결 전 회수 불가능한 전용 자산(R&D, 특화 설비, 독점 노하우)을 선투자하여 상대방에게 가격 삭감(Hold-up) 빌미를 제공하는 경우.
   - *교정*: 상호 인질(Mutual Hostage) 계약, 단계적 마일스톤 집행, 퇴로(BATNA) 사전 확정.

2. **`[TRIGGER-GT-PAST-FAVOR]` (항우의 착각 / 과거 은혜 의존 경보)**
   - *징후*: "내가 과거에 베풀었으니 상대도 잘해주겠지"라는 감정적 기대에 의존하는 경우.
   - *공리*: **인간은 과거의 은혜(Sunk Cost)가 아니라 미래의 인센티브(Future Payoff)에 움직인다.**
   - *교정*: 옹치 포상법(가장 미운 자에게 미래 보상을 주어 전체 신뢰 확보) 및 미래 연금형 보상 앵커링.

3. **`[TRIGGER-GT-CHEAP-TALK]` (고르바초프의 패착 / 실행 불가능한 위협 경보)**
   - *징후*: 상대방이 약속이나 위협을 어겼을 때 나에게 감당 못 할 손실이 발생하는 위협(Non-credible Threat).
   - *교정*: 선제적 공약(Credible Commitment) 또는 광인 전략(Madman Strategy)으로 위협의 실행을 자동화.

4. **`[TRIGGER-GT-REPUTATION-CRACK]` (명성 붕괴 경보)**
   - *징후*: 1회의 사소한 단기 이익을 위해 장기 반복 게임의 명성 자산($\alpha$)을 훼손하는 경우.
   - *교정*: 아사쇼류·가마쿠라 막부 사례 분석, 장기 할인계수($\delta$) 극대화 및 즉각적 배신 징벌(Grim Trigger).

5. **`[TRIGGER-GT-KINGPIN]` (헨리 포드의 킹핀 / 과잉 스펙 자원 낭비 경보)**
   - *징후*: 병목이 아닌 부품이나 기능에 과도한 비용을 투입하는 경우.
   - *교정*: 시스템 전체의 파괴는 가장 약한 킹핀에서 발생하므로 비병목 자원을 축소하고 핵심 병목에 자원 집중.

6. **`[TRIGGER-GT-RUIN-BET]` (파산 확률 / 비대칭 손실 경보)**
   - *징후*: 기댓값은 양수라도 1회 실패 시 자본이 소멸하거나 생존이 위협받는 베팅.
   - *교정*: 켈리 기준(Kelly Criterion) 적용 및 생존 보존 현금 비중 강제.

---

## Han Soon-koo's Practical Game Axioms (한순구 교수의 실전 공리)

- **공리 1:** 인간은 과거의 고마움이 아니라 미래의 이익을 보고 행동한다.
- **공리 2:** 훌륭한 리더는 '나를 배신해도 미래가 있으면 충성하게 만들고', '나를 좋아해도 미래가 없으면 떠난다'는 것을 안다.
- **공리 3:** 황금 메추리알 전략 — 상대방이 훔쳐갈 수 없는 구조로 인센티브를 쪼개어 제공하라.
- **공리 4:** 옹치 포상법 — 반란을 막으려면 가장 배신할 가능성이 높고 미운 자에게 공개적으로 미래 보상을 보장하라.


---

## Hospital & Healthcare Executive Applications (남양주백병원 실전 메커니즘 디자인)

The engine provides concrete mathematical models tailored to hospital management, clinical operations, and healthcare HR:

1. **척추센터 광고·고가장비 죄수의 딜레마 (Prisoner's Dilemma)**:
   - 양 병원 과열 확대 시 (7억, 7억) 내시균형의 파레토 열등 탈출.
   - 앙갚음(Tit-for-Tat) 위협 및 척추내시경 임상 차별화로 보수표 자체 재설계.
2. **의료진 영입 사이닝 보너스 동태적 이연 설계 (Dynamic Incentive)**:
   - 충성 임계확률: $p^* = \frac{L}{L + D}$.
   - 1.5억 전액 선지급 시 미래 잔류가치 $L=1억$ ($p^*=40%$) vs 2~3년 이연 분할 지급 시 $L=1.5억$ ($p^*=50%$). 분할 지급이 이탈 유인을 획기적으로 억제.
3. **척추센터 다학제 협진 성과 배분 섀플리 값 (Shapley Value)**:
   - 수술 외과(O), 통증 시술과(P), 재활의학과(R) 협진 가치 배분: **외과 9.17 : 통증 5.67 : 재활 3.17**.
   - 단순 단독 매출 배분(재활 1.8 과소평가)을 배제하여 재활의학과의 협진 소외 방지.
4. **간호 인력 연쇄 이직 뱅크런 사슴사냥 게임 (Stag Hunt Coordination)**:
   - 동료 잔류 신뢰도 임계값 $q^* = 75%$. 잔류 보상 강화보다 **'혼자 남았을 때 대체인력 풀 즉시 투입 안전망'** 공표 시 $q^* = 50%$로 급감하여 조직 내성 극대화.
5. **게일-섀플리 지연수락 알고리즘 (Gale-Shapley Matching)**:
   - 신규 간호사 부서 배치 시 지원자(간호사) 제안 지연수락 메커니즘 적용으로 유인합치적 안정 매칭 보장.
6. **영상의학과 직영 vs 외주 거래비용 판정 (Transaction Cost)**:
   - 손익분기 판독 건수 $N^* = 2,850$건 ($2N^* + 800만 = 6,500만$). 초과 시 직영 전환 유리.
7. **행동경제학 2.0 환자 유치 모델**:
   - 손실 회피(2~2.5배), 현상 유지 편향, $\beta-\delta$ 시간 비일관성 극복을 위한 척추내시경 성공률 93% 프레이밍, 당일 원스톱 검사 디폴트 예약, MAB 알고리즘 AI 초정밀 넛지.


---

## 2026 Institutional Constraints & Simulation Benchmarks (2026 제도 환경 및 시뮬레이션 가드레일)

The engine enforces 2026 South Korean healthcare statutory and behavioral boundary conditions:

### 1. 2026 Institutional Statutory Rules (바깥 규칙 가드레일)
- **5세대 실손보험 (2026.5.6 출시)**: 비중증 비급여 자기부담 30%→50%, 한도 1천만 원 축소, 도수·체외충격파 보장 제외. 환자 체감 가격 3.3배 증가로 비급여 가격 상한(WTP) 하락 반영.
- **도수치료 관리급여 (2026.7.1 시행)**: 1회 43,850원 고정, 연 15~24회 상한. 회당 공헌이익 축소(7.7만→2.1만 원) 속에서도 한계공헌이익이 양수인 한 존속 유지.
- **공정거래법 제40조 (담합 규제)**: 경쟁 병원 간 마케팅 예산·단가 정보 교환은 담합 추정 위험. 외부 협의체 자제 합의 대신 장기 반복게임($\delta \ge 0.5$)의 독자적 판단과 임상 차별화 강제.
- **간호법 및 진료지원(PA)간호사 고시 (2026.7~8)**: 3년차 이상 숙련 간호사의 외부 가치($D$) 급상승. '혼자 남았을 때 대체인력 풀 안전망' 선제 구축 필수.
- **근로기준법 제20조 (위약 예정 금지)**: 사이닝보너스 선지급 후 반환 약정 무효 판례(2022다208755) 대비, 처음부터 '근속 조건부 분할 이연 지급' 강제.

### 2. Simulation-Verified Mathematical Results
- **승자의 저주 4만 회 몬테카를로**: $E[\text{과대평가}] = a \cdot \frac{n-1}{n+1}$ (경쟁자 2곳 0.33a, 4곳 0.60a, 10곳 0.82a 역할인 입찰).
- **사이닝보너스 이연 지급**: $s=2/3$ 이연 시 충성 임계확률 $p^*=40% \to 57%$ 대폭 향상.
- **간호사 400명 에이전트 연쇄이직 모델**: 현 구조는 동시 퇴사 22% 초과 시 전원 이탈 붕괴. 대체인력 안전망 도입 시 붕괴 완전 소멸.
- **영상의학 Make or Buy**: $N^* = 2,850$건 (단가 1.5만 원 시 3,800건, 3만 원 시 1,900건).
- **MAB 톰슨 샘플링 넛지**: 환자 예약률(다크패턴 위험)이 아닌 '이해 확인율(Teach-back)'을 최적화.


---

## Han Soon-koo Nobel Decision Pitfalls & Institutional Governance (한순구 노벨경제학 2부 결정 함정)

The engine incorporates formal decision-making pitfalls from auction theory, public choice, and Bayesian epistemology:

### 1. 후계자 선발과 순차적 심사의 함정 ➔ 청나라 황태자 밀건법 (동시 경매)
- **순차적 심사의 함정**: 후보를 1명씩 차례로 심사하면 초반 유력 후보는 사소한 5점 흠결에도 집중 견제로 낙마하고, 마지막에 등장한 후보는 검증 시간과 대체재 부재로 100점짜리 치명적 결격 사유가 있어도 당선되는 역설 발생 (영화 <콘클라베>, 양녕대군·사도세자 증후군).
- **밀그롬-윌슨 동시 경매 & 밀건법(密建法)**: 여러 대상을 동시에 심사 테이블에 올리고 시작과 종료를 일치시켜 상호 비교·학습 유도. 청나라가 황제 사후 병풍 뒤 밀서를 공개하는 밀건법으로 황자 전원을 끝까지 동시 경쟁·검증시켜 강희·옹정·건륭 130년 전성기를 구가한 지혜 적용.

### 2. 경매 방식과 정보 학습 효과 (네덜란드식 vs 영국식)
- **네덜란드식 (하향식)**: 높은 가격에서 내림. 타인의 침묵을 보며 "내가 과대평가했나?"라는 승자의 저주 공포가 발동하여 헐값 유찰 위험.
- **영국식 (상향식)**: 낮은 가격에서 올림. 타인의 입찰을 보며 시장의 객관적 하한선과 정보 확신을 학습 ➔ 참가자 확신 강화로 판매자에게 최고가 보장.

### 3. 공공선택과 다수결의 함정 ➔ 선호 순위 투표 (Ranked-Choice Voting)
- **애로우의 불가능성 정리 & 메이의 정리**: 3명 이상 다자 대결에서 완벽한 민주적 투표 제도는 부재하며, 1대1일 때만 다수결이 공정함 (20명 참호전에 강호동이 나오면 19명이 연합해 강호동부터 떨어뜨리는 참호전의 역설).
- **1인 1표(최선호 투표)의 혐오정치 메커니즘**: 유권자의 차순위 선호와 비호감도를 무시하여, 30% 극성 지지층만 결집하면 70%가 혐오하는 후보가 당선되는 왜곡 발생 (회식 메뉴의 역설).
- **보르다 투표(Borda Count) & 선호 순위 투표용지**: 1~3순위를 차등 배점 합산하여 극단주의를 배제하고 타협 가능한 통합적 리더 선출.

### 4. 베이지안 업데이트와 직업적 표본 편향 ➔ 성공의 영점 조절 (Calibration)
- **직업적 표본 편향**: 중환자실 의사(사망자만 봐서 저축 전폐), 특수교사(장애아동만 봐서 출산 공포), 판사(피고인만 봐서 세상 70%가 사기꾼 체감).
- **성공의 영점 조절**: 실제 세상의 사기꾼 비율이 5%라면, 내 주관적 사후확률도 정확히 5%로 맞춘 자가 가장 크게 성공함 (0%는 사기 파산, 70%는 기회 상실).
- **역사적 교훈**: 콤모두스·연산군(과도한 긍정 편향: 좌절 미경험 폭정 몰락) vs 광해군(과도한 부정 편향: 신뢰 0% 고립 폐위).
- **평생 독서의 본질**: 협소한 직접 경험의 감옥에서 벗어나 주관적 확률을 세상의 객관적 확률로 끊임없이 캘리브레이션(영점 조절)해야 함.


---

## The 5-Step Bayesian Calibration & AI Gating Protocol (5단계 베이시안 생각 교정 프로토콜)

The engine enforces the 5-step decision calibration workflow to eliminate AI overconfidence (95% bluffing) and cognitive anchoring:

```
1단계. 편견 빼기  ➔  2단계. 팩트 점검  ➔  3단계. 생각 수정  ➔  4단계. 거품 빼기  ➔  5단계. 행동 결정
(출발선 기저율)     (새 증거 단독 평가)    (베이시안 업데이트)   (자신감 캘리브레이션)   (위험도별 멈춤/실행)
```

### Step-by-Step Rules:
1. **1단계: 편견 빼기 (출발선 기저율 확정)**:
   - 질문 속 감정, 조급함, 남들의 과장된 무용담을 지우고 "원래 이 업계/상황에서 객관적 기본 성공률(Base Rate)은 몇 %인가?"부터 시작 (0%나 100% 극단값 금지).
2. **2단계: 새로 나온 사실만 따로 떼어 무게 재기**:
   - 선입견 없이 새 팩트만 객관적 평가. **동일 소문 복제 필터링**(기사 5개가 같은 소스를 베꼈다면 증거는 5개가 아니라 단 1개).
3. **3단계: 생각 수정 (베이시안 업데이트)**:
   - 주먹구구 암산 배제. `오늘의 진짜 확률 = 원래 기본 확률 + 새 증거 무게 - 철 지난 기억`을 단계별 수리 계산.
4. **4단계: 거품 빼기 (베이시안 캘리브레이션 / 영점 조절)**:
   - AI의 "95% 확실합니다" 과잉 확신(Overconfidence) 거품 삭감. 같은 질문을 다르게 물어봐 대답이 흔들리면 승률 하향 조정. 브라이어 점수(Brier Score) 관점의 정직성 보정.
5. **5단계: 손해 크기 따져 행동 결정 & 정직한 멈춤(Stop & Probing)**:
   - 실수 대가가 작으면 60% 승률도 실행 가능.
   - **사람 건강이나 큰 병원 자금이 걸린 일(고위험)은 승률 90% 이상일 때만 실행.**
   - 승률이 애매한 구간이면 억지로 결론 내지 않고 **"승률을 확실히 알기 위해 우리가 추가로 확인해야 할 가장 중요한 한 가지가 무엇인가?"**를 질문하고 멈춤.
6. **결정 일기(Decision Journal) 루프**:
   - `[날짜 / 예상 확률 / 이유 한 줄 / 실제 결과]` 오답 노트를 누적하여 지속적으로 AI와 인간의 예측 눈금을 교정.


---

## Thermodynamic Foundations of Mechanism Design (열역학적 깁스 에너지와 메커니즘 디자인)

The engine bridges statistical thermodynamics (J. Willard Gibbs) and mathematical mechanism design (Paul Samuelson, Eric Maskin):

### 1. 깁스 자유 에너지($\Delta G = \Delta H - T\Delta S$)와 자발적 협력(Incentive Compatibility)
- **자발적 반응의 법칙**: 공이 언덕에서 바닥으로 굴러가듯, $\Delta G < 0$ (자유 에너지가 감소하여 안정화되는 방향)일 때 외력이 없어도 반응은 스스로 일어난다.
- **제도 설계로의 번역**:
  - 엔탈피 마찰($\Delta H$): 의무 수행에 따르는 심리적·물리적 노력 비용.
  - 엔트로피 다변성($T\Delta S$): 선택의 자유와 미래 보상 다양성에 대한 인센티브 온도($T$).
  - **참여자의 효용 변화가 $\Delta G < 0$이 되도록 룰(Rule)을 설계하면, 경영진이 감시하거나 강제하지 않아도 구성원은 자발적으로 정직과 협력을 선택(Dominant Strategy)한다.**

### 2. 열린계(Open System)와 엔트로피 비관론 극복
- 잉크가 고르게 퍼진 상태는 '무질서'가 아니라 최대 확률 상태($S = k \log W$)일 뿐이며, 적절한 압력과 필터(조건)를 부여하면 언제든 분리 가능하다.
- 조직과 경제는 닫힌 고립계가 아니라 지속적으로 지식과 자본이 유입되는 **'열린계(Open System)'**이므로, 정교한 환경 조건을 설계하는 한 조직의 와해(열사망)를 방지하고 고도의 질서를 영구히 유지할 수 있다.


---

## Evolutionary Game Theory & The Selfish Gene (이기적 유전자와 팃포탯 상호이타주의)

The engine incorporates evolutionary biology and Axelrod's repeated game tournament axioms:

### 1. 해밀턴의 규칙 (Hamilton's Rule)과 혈연선택 ($rB > C$)
- **자연선택의 단위**: 개체나 집단이 아닌 '유전자 사본의 번성'.
- **혈연 이타주의**: 나의 희생 비용($C$)보다 수혜자의 이익에 유전적 근연도($r$)를 곱한 값($rB$)이 크면 이타적 행동이 진화 ($r=0.5$ 부모/자식/형제, $r=0.25$ 조카/조부모, $r=0.125$ 사촌).
- **경영학적 번역**: 남남인 직원($r=0$)에게 도덕적 헌신을 강요할 수 없으며, 성과급·지분·이연 보상(KB DC)을 통해 병원의 성공이 개인의 이익이 되는 **'인위적 $r$(이익 공유도)'을 메커니즘으로 설계**해야 함.

### 2. 팃포탯(Tit-for-Tat)의 4대 절대 승리 원칙 (Robert Axelrod)
- **미래의 그림자 (Shadow of the Future, $\delta$)**: 관계가 반복될 때만 상호 협력이 진화적 안정 전략(ESS)이 됨.
- **4대 속성**:
  1. **신사성 (Nice)**: 결코 먼저 배신하지 않는다 (불필요한 갈등 비용 배제).
  2. **단호함 (Retaliatory)**: 상대가 배신하면 1초 만에 즉각 보복한다 ('호구' 방지 및 배신 비용 즉시 학습).
  3. **관용성 (Forgiving)**: 상대가 협력으로 돌아오면 뒤끝 없이 즉시 용서한다 (치킨게임 공멸 방지).
  4. **투명성 (Clear)**: 행동 패턴이 단순 명료하여 상대가 협력의 이익을 쉽게 계산할 수 있게 한다.

### 3. 밈(Meme)과 헌법 (Constitution)
- 인간은 뇌와 문화적 복제자(Meme)를 통해 이기적 유전자의 생물학적 명령에 반역(Rebel)할 수 있는 유일한 존재.
- 운영 헌법과 시스템 온톨로지는 단기적 이기심과 동물적 본능을 통제하여 조직의 높은 질서(부의 엔트로피)를 창출하는 최고 차원의 밈(Meme)임.
