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
