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
