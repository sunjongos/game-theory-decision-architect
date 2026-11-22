---
ontology_id: LLM-WIKI-GAME-THEORY-2026
version: 1.0.0
schema_type: Neuro-Symbolic-Ontology
total_nodes: 8
---

# Master Ontology Index (게임이론 & 메커니즘 디자인 지식 그래프)

| Node ID | Cluster | Title | Key Symbolic Variables | Linked Cascade Nodes |
| :--- | :--- | :--- | :--- | :--- |
| `[[WIKI-GT-01]]` | Social Dilemmas | Prisoner's Dilemma, Tragedy of the Commons & Repeated Games | `T, R, P, S`, `discount_delta`, `property_rights` | `[[WIKI-GT-03]]`, `[[WIKI-GT-05]]` |
| `[[WIKI-GT-02]]` | Contract & Lock-in | Hold-up Problem, Asset Specificity & Mutual Hostage Design | `sunk_cost_k`, `outside_option_v`, `binding_contract` | `[[WIKI-GT-04]]`, `[[WIKI-GT-06]]` |
| `[[WIKI-GT-03]]` | Organizational HR | Moral Hazard in Teams, Tournaments & Future Incentives | `team_size_n`, `effort_cost_c`, `future_reward_w` | `[[WIKI-GT-01]]`, `[[WIKI-GT-04]]` |
| `[[WIKI-GT-04]]` | Asymmetric Info | Adverse Selection, Signaling (Cho-Kreps) & Screening Menus | `type_theta`, `signal_cost_c`, `IC_constraint`, `IR_constraint` | `[[WIKI-GT-02]]`, `[[WIKI-GT-05]]` |
| `[[WIKI-GT-05]]` | Mechanism Design | VCG Pivot Mechanism, Auction Theory & Matching (Gale-Shapley) | `externality_payment_p`, `revelation_truth`, `deferred_acceptance` | `[[WIKI-GT-01]]`, `[[WIKI-GT-04]]` |
| `[[WIKI-GT-06]]` | Strategic Power | Reputation Game, Credible Commitment & Madman Theory | `reputation_alpha`, `irrationality_prob_p`, `backward_induction` | `[[WIKI-GT-02]]`, `[[WIKI-GT-07]]` |
| `[[WIKI-GT-07]]` | Tactical Combat | Asymmetric Mixed Strategies, Gladiator's Left Hand & Risk Control | `payoff_asymmetry`, `bankruptcy_limit`, `kingpin_overdesign` | `[[WIKI-GT-06]]`, `[[WIKI-GT-08]]` |
| `[[WIKI-GT-08]]` | Macro & AI Systems | Coordination (Stag Hunt), Global Games & Price of Anarchy (PoA) | `lambda_mu_smooth`, `poa_bound`, `signal_noise_epsilon` | `[[WIKI-GT-01]]`, `[[WIKI-GT-05]]` |

---

## Detailed Node Specifications

### [[WIKI-GT-01]]: Prisoner's Dilemma, Tragedy of the Commons & Repeated Games
- **Axioms**: $T > R > P > S$ and $2R > T + S$.
- **Finite vs Infinite**: In finite games, backward induction causes unravelling to mutual defection. In infinitely repeated games, cooperation is sustained iff $\delta \ge \frac{T - R}{T - P}$.
- **Institutional Remedy**: Enforceable property rights (철조망 설치), Grim Trigger punishment, Tit-for-Tat reciprocal strategy.

### [[WIKI-GT-02]]: Hold-up Problem & Asset Specificity
- **Axioms**: Sunk specific investment $k > 0$. Ex-post quasi-rents $R = V - c$. Without binding contract, the investor is held up and receives only $\alpha R < k$.
- **Remedy**: Vertical integration, mutual hostage exchange (상호 인질), milestone escrow payments, multi-sourcing fallback.

### [[WIKI-GT-03]]: Moral Hazard in Teams & Future Incentives
- **Axioms**: $1/N$ free-riding occurs when individual effort is unobservable.
- **Han Soon-koo Axiom**: "인간은 과거의 은혜가 아니라 미래의 인센티브를 보고 움직인다."
- **Remedy**: 옹치 포상법 (미래 배신 가능자에게 종신 연금형 보상 앵커링), 상대평가 토너먼트(Tournament Theory), 황금 메추리알 분할 제공.

### [[WIKI-GT-04]]: Adverse Selection, Signaling & Screening
- **Axioms**: Single-Crossing Property: $\frac{\partial c(s, \theta_H)}{\partial s} < \frac{\partial c(s, \theta_L)}{\partial s}$.
- **Cho-Kreps Intuitive Criterion**: Eliminates equilibria supported by unreasonable off-equilibrium beliefs.
- **Remedy**: Screening menu design (고능력자-고인센티브/저기본급 vs 저능력자-저인센티브/고기본급).

### [[WIKI-GT-05]]: Mechanism Design (Reverse Game Theory)
- **Axioms**: VCG (Vickrey-Clarke-Groves) Pivot Mechanism enforces truthful revelation as a dominant strategy.
- **Matching Theory**: Gale-Shapley Deferred Acceptance algorithm (Proposer-Optimal, Strategy-Proof for proposing side).

### [[WIKI-GT-06]]: Reputation Game & Credible Commitment
- **Axioms**: Kreps-Wilson-Milgrom-Roberts reputation model. Short-run loss for long-run monopoly rents.
- **Madman Strategy**: Deliberately projecting bounded rationality or tying one's own hands (배수진/선제적 구속) to force the opponent to yield.

### [[WIKI-GT-07]]: Asymmetric Mixed Strategies & Kingpin Risk Control
- **Axioms**: In zero-sum mixed games, changing your opponent's payoff changes your own equilibrium probability.
- **Henry Ford's Kingpin**: Over-engineering non-bottlenecks is waste. Minimize maximum damage, avoid ruin probability ($P(\text{ruin}) = 0$).

### [[WIKI-GT-08]]: Coordination & Price of Anarchy
- **Axioms**: Stag Hunt payoff dominance vs risk dominance.
- **PoA (Price of Anarchy)**: $\text{PoA} = \frac{\max_{s} W(s)}{\min_{s \in \text{NE}} W(s)}$. Measures efficiency loss of decentralized selfish behavior.


| `[[WIKI-GT-09]]` | Auction & Succession | Succession Dilemma, Milgrom Simultaneous Auction & Qing Secret Succession (밀건법) | `eval_sequence`, `n_candidates`, `info_learning` | `[[WIKI-GT-02]]`, `[[WIKI-GT-05]]` |
| `[[WIKI-GT-10]]` | Public Choice & Voting | Arrow Impossibility, May's Trench War, Condorcet vs Borda & Ranked-Choice | `plurality_bias`, `borda_points`, `veto_power` | `[[WIKI-GT-01]]`, `[[WIKI-GT-08]]` |
| `[[WIKI-GT-11]]` | Epistemology & Beliefs | Bayesian Updating, Occupational Sample Bias & Probability Calibration (영점조절) | `prior_prob`, `sample_bias`, `calibration_error` | `[[WIKI-GT-06]]`, `[[WIKI-GT-07]]` |

---

### [[WIKI-GT-09]]: Succession Dilemma & Simultaneous Auction (밀건법)
- **Axioms**: Sequential evaluation penalizes early front-runners for minor flaws while late entrants pass unvetted.
- **Remedy**: Simultaneous multi-object auction (Milgrom-Wilson) and Qing Dynasty Secret Succession System (밀건법) — evaluate all candidates concurrently at fixed deadline.

### [[WIKI-GT-10]]: Public Choice, Arrow Impossibility & Ranked-Choice Voting
- **Axioms**: Single-vote plurality creates negative campaigning and pandering to polarized minorities (회식 메뉴의 역설).
- **Remedy**: Borda Count scoring and Ranked-Choice Ballots to elect candidates with broad consensus rather than intense narrow appeal.

### [[WIKI-GT-11]]: Bayesian Updating, Sample Bias & Probability Calibration
- **Axioms**: Humans update subjective beliefs based on narrow occupational samples (중환자실 의사, 특수교사, 판사 효과).
- **Historical Contrast**: Commodus & Yeonsangun (Excessive Positive Bias) vs Gwanghaegun (Excessive Negative Bias).
- **Remedy**: Continuous calibration of subjective probabilities against objective base rates via reading and diverse indirect learning.


| `[[WIKI-GT-12]]` | Epistemology & AI | 5-Step Bayesian Calibration Pipeline, Brier Score & Decision Threshold Gating | `base_rate`, `evidence_weights`, `calibrated_confidence`, `stakes_threshold` | `[[WIKI-GT-11]]`, `[[WIKI-GT-07]]` |

---

### [[WIKI-GT-12]]: 5-Step Bayesian Calibration Pipeline & AI Gating
- **Axioms**: Uncalibrated AI bluffs 95% certainty on 50% guesses. Subjective belief must be adjusted by explicit 5-step gating.
- **Rules**:
  1. Base Rate Anchor (No 0% or 100%).
  2. Single Evidence per Root Source (De-duplicate 5 copycat articles into 1 signal).
  3. Step-by-step arithmetic updating.
  4. Brier score / Temperature scaling for confidence deflation.
  5. Asymmetric loss thresholding: High-Stakes $\ge 90\%$, Low-Stakes $\ge 60\%$. If uncertain, trigger Missing Info Probe instead of forcing a decision.


| `[[WIKI-GT-13]]` | Physical Foundations | Thermodynamic Mechanism Design, Gibbs Free Energy (ΔG < 0) & Open System Negentropy | `delta_G`, `delta_H`, `temperature_T`, `entropy_delta_S` | `[[WIKI-GT-05]]`, `[[WIKI-GT-08]]` |

---

### [[WIKI-GT-13]]: Thermodynamic Mechanism Design & Spontaneous Equilibrium
- **Axioms**: $\Delta G = \Delta H - T\Delta S < 0$ is the universal condition for spontaneous physical and economic action.
- **Samuelson Bridge**: Paul Samuelson integrated Gibbsian thermodynamics into mathematical economics.
- **Rules**: Organizations do not passively decay into disorder if modeled as Open Systems with continuous information input. Design rules such that truthful revelation and cooperation minimize systemic free energy ($\Delta G < 0$).


| `[[WIKI-GT-14]]` | Evolutionary Dynamics | The Selfish Gene, Hamilton's Rule (rB > C), Axelrod's Tournament & Tit-for-Tat 4 Axioms | `relatedness_r`, `benefit_B`, `cost_C`, `shadow_delta`, `meme_rule` | `[[WIKI-GT-01]]`, `[[WIKI-GT-06]]` |

---

### [[WIKI-GT-14]]: The Selfish Gene, Kin Selection & Tit-for-Tat ESS
- **Axioms**: Natural selection acts on genes. Altruism evolves via $rB > C$ (kin) or repeated interaction discount $\delta$ (reciprocal).
- **Tit-for-Tat ESS**:
  1. Nice: Never defect first.
  2. Retaliatory: Punish defection immediately.
  3. Forgiving: Cooperate immediately upon opponent's return to cooperation.
  4. Clear: Predictable, transparent strategy.
- **Meme Rebel**: Memetic constitutional rules override raw biological genetic optimization.


| `[[WIKI-GT-15]]` | Behavioral Axioms | Human 3-Tier Objective Function (Survival, Reproduction, Prosperity) & Selfish Gene Alignment | `u_survival`, `u_reproduction`, `u_prosperity`, `incentive_alignment` | `[[WIKI-GT-03]]`, `[[WIKI-GT-14]]` |

---

### [[WIKI-GT-15]]: Human 3-Tier Objective Function & First Principle of Governance
- **Axioms**: All human behavior maximizes $\max u_i = f(\text{Survival}, \text{Reproduction}, \text{Prosperity})$. Driven by the Selfish Gene.
- **Rule**: Eliminate moralistic disillusionment. Align individual $u_i$ with organizational goals via mechanism design.


| `[[WIKI-GT-16]]` | Executive Leadership | Platform Illusion (Self-Serving Bias), Entitlement Drift, Hold-up Mitigation & BATNA Salience | `platform_rent`, `attribution_bias`, `batna_threat`, `incentive_cycling` | `[[WIKI-GT-02]]`, `[[WIKI-GT-15]]` |

---

### [[WIKI-GT-16]]: Platform Illusion & Executive BATNA Enforcement
- **Axioms**: When basic needs are satiated, agents attribute platform rents to personal talent, resulting in hold-up demands.
- **Rule**: Never rely on past favors. Counter hold-up by making outside alternatives (BATNA) constantly visible and cycling incentives via performance pay.


---

## 2026 확장판: AI 시대 및 확장 게임이론 온톨로지 (21개 장 체계 반영)

| Node ID | Cluster | Title | Key Symbolic Variables | Linked Cascade Nodes |
| :--- | :--- | :--- | :--- | :--- |
| `[[WIKI-GT-17]]` | AI Era | Algorithmic Collusion & Autonomous Pricing Bots | `q_learning`, `tacit_collusion`, `instant_punishment`, `zero_forgiveness_trap` | `[[WIKI-GT-01]]`, `[[WIKI-GT-18]]` |
| `[[WIKI-GT-18]]` | AI Era | AI Agent Swarm Alignment & Equilibrium Design | `rlhf_reward_hack`, `agent_negotiation`, `pareto_alignment` | `[[WIKI-GT-05]]`, `[[WIKI-GT-17]]` |
| `[[WIKI-GT-19]]` | Market Structure | Oligopoly: Cournot vs Bertrand vs Stackelberg | `cournot_qty`, `bertrand_price_trap`, `stackelberg_first_mover` | `[[WIKI-GT-01]]`, `[[WIKI-GT-07]]` |
| `[[WIKI-GT-20]]` | Resource Governance | Tragedy of the Commons & Ostrom 8 Principles | `cpr_boundary`, `ostrom_monitoring`, `graduated_sanction` | `[[WIKI-GT-01]]`, `[[WIKI-GT-03]]` |
| `[[WIKI-GT-21]]` | Coordination | Common Knowledge, Schelling Focal Points & Stag Hunt | `common_knowledge_omega`, `schelling_focal_pt`, `risk_dominance` | `[[WIKI-GT-01]]`, `[[WIKI-GT-08]]` |
| `[[WIKI-GT-22]]` | Conflict & Risk | War of Attrition & Brinkmanship (확률적 파국 위협) | `attrition_decay`, `brinkmanship_prob_p`, `accidental_catastrophe` | `[[WIKI-GT-06]]`, `[[WIKI-GT-07]]` |
| `[[WIKI-GT-23]]` | Social Choice | Voting Paradox, Median Voter & Divide-and-Choose | `median_voter`, `condorcet_paradox`, `arrow_impossibility`, `divide_and_choose` | `[[WIKI-GT-05]]`, `[[WIKI-GT-08]]` |
| `[[WIKI-GT-24]]` | Dynamic Macro | Network Externalities, Critical Mass & Cascades | `two_sided_market`, `critical_mass_s`, `information_cascade` | `[[WIKI-GT-08]]`, `[[WIKI-GT-21]]` |
| `[[WIKI-GT-25]]` | Master Diagnostic | 8 Core Axioms & 7-Step Diagnostic Framework | `interdependence`, `backward_induction`, `shadow_future`, `7step_diagnostics` | All Nodes |

---

### [[WIKI-GT-17]]: Algorithmic Collusion & Autonomous Pricing (알고리즘 담합)
- **Axioms**: Q-learning autonomous pricing bots learn supra-competitive tacit collusion without direct communication (Calvano et al. 2020, Assad et al. 2024).
- **Core Mechanism**: Why bots collude better than humans:
  1. **Instant Detection**: Real-time market price monitoring eliminating detection lags.
  2. **Automated Retaliation**: Mechanical price drop without human hesitation, saving face, or blame avoidance.
  3. **Zero Forgiveness Trap**: Eliminates human soft bargaining, permanently compressing defect temptation $(T - R 	o 0)$.

### [[WIKI-GT-18]]: AI Agent Alignment & Swarm Equilibrium (AI 에이전트 정렬)
- **Axioms**: Multi-agent LLM systems and Swarm robotics require mechanism design to prevent reward hacking and toxic race-to-the-bottom dynamics.
- **Remedy**: Strategy-proof consensus protocols, automated truth-revelation audits, and verification gateways.

### [[WIKI-GT-19]]: Oligopoly Competition (과점 경쟁과 베르트랑 함정)
- **Axioms**:
  - Cournot: Simultaneous quantity choice ($P > MC$, positive economic rents).
  - Bertrand: Homogeneous price competition collapses to $P = MC$ (Bertrand Trap).
  - Stackelberg: First-mover capacity commitment yields leader advantage.
- **Remedy**: Never engage in Bertrand price wars. Shift to non-price quality differentiation, specialized niche care, and reputational capital.

### [[WIKI-GT-20]]: Tragedy of the Commons & Ostrom 8 Principles (공유자원 자치 관리)
- **Axioms**: Hard property rights or complete privatization are not the only solutions. Ostrom demonstrated sustainable community governance through 8 institutional design principles.
- **8 Principles**: Clear boundaries, local rule alignment, collective choice, mutual monitoring, graduated sanctions, low-cost conflict resolution, recognized rights to organize, and nested enterprise layers.

### [[WIKI-GT-21]]: Common Knowledge & Schelling Focal Points (공유지식과 셸링 포인트)
- **Axioms**: Mutual knowledge ("everyone knows X") vs Common knowledge ("everyone knows that everyone knows... ad infinitum").
- **Focal Point**: In coordination games with multiple equilibria, players coordinate without communication using shared cultural, salient, or psychological clues (Schelling Point).

### [[WIKI-GT-22]]: War of Attrition & Brinkmanship (소모전과 벼랑끝 전술)
- **Axioms**:
  - War of Attrition: Waiting costs accrue over time until the weaker party concedes.
  - Brinkmanship (Thomas Schelling): A credible threat created not by committing to deliberate suicide, but by deliberately relinquishing control and stepping onto a slippery slope where catastrophe occurs with probability $p > 0$.

### [[WIKI-GT-23]]: Social Choice, Voting & Fair Division (투표와 나누기)
- **Axioms**:
  - Median Voter Theorem: In single-peaked 1D political space, policy converges to the median voter.
  - Condorcet Paradox & Arrow's Impossibility: No democratic voting system can simultaneously satisfy unrestricted domain, Pareto efficiency, independence of irrelevant alternatives, and non-dictatorship.
  - Divide-and-Choose: "One cuts, the other chooses" eliminates envy and enforces Pareto fairness.

### [[WIKI-GT-24]]: Network Externality & Information Cascades (네트워크와 쏠림)
- **Axioms**: Metcalfe's Law ($V \propto N^2$). Critical mass threshold determines market tipping.
- **Information Cascade**: Rational agents ignore their private signal and imitate predecessors' public actions once the public evidence outweighs private confidence.

### [[WIKI-GT-25]]: 8 Core Axioms & 7-Step Diagnostic Framework (8대 정수 & 7대 실전 진단)
- **8 Core Axioms**:
  1. 상호의존 (결과는 나 혼자 정하지 못한다)
  2. 유인 (사람은 말이 아니라 보수에 반응한다)
  3. 균형의 함정 (각자의 최선이 모두의 최선은 아니다)
  4. 끝에서부터 (마지막 의사결정이 오늘의 행동을 규정한다)
  5. 미래의 그림자 (다시 만날 사이에서는 협력이 이득이다)
  6. 신빙성 (실행할 이유가 있는 약속과 위협만 힘이 있다)
  7. 정보 (비용이 든 신호만 믿을 수 있다)
  8. 규칙 설계 (사람을 바꾸려 하지 말고 게임의 규칙을 바꾼다)
- **7-Step Diagnostic Framework**:
  1) 누가 경기자인가?
  2) 각자 무엇을 원하는가?
  3) 동시인가 순서가 있는가?
  4) 1회인가 반복인가?
  5) 누가 무엇을 모르는가?
  6) 약속을 강제할 수 있는가?
  7) 게임의 규칙을 바꿀 수 있는가?
