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
