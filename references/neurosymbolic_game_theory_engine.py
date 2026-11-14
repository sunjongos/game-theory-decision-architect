#!/usr/bin/env python3
"""
Neuro-Symbolic Game Theory & Mechanism Design Deterministic Engine
INSA Tier 3 Implementation
0-Dependency Python 3 CLI
"""

import sys
import json
import argparse
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional


@dataclass
class StrategicDecisionPayload:
    scenario_name: str
    requires_unilateral_sunk_cost: bool = False
    has_binding_mutual_hostage: bool = False
    relies_on_past_favors_or_loyalty: bool = False
    has_vested_future_incentives: bool = False
    team_size_n: int = 1
    individual_effort_observable: bool = True
    uses_unbacked_threat_or_bluff: bool = False
    exposes_core_reputation_to_stalemate: bool = False
    over_engineers_non_bottleneck: bool = False
    downside_loss_exceeds_safe_capital: bool = False


class GameTheoryImmuneAuditor:
    """
    INSA Tier 3 Immune Layer Audit Engine for Strategic Traps
    """
    @staticmethod
    def audit(payload: StrategicDecisionPayload) -> Dict[str, Any]:
        triggers = []
        recommendations = []
        severity = "STABLE"

        # 1. Holdup check
        if payload.requires_unilateral_sunk_cost and not payload.has_binding_mutual_hostage:
            triggers.append({
                "code": "[TRIGGER-GT-HOLDUP]",
                "severity": "CRITICAL",
                "name": "오렌지색 남자친구 / 선투자 인질화 경보",
                "diagnosis": "회수 불가능한 전용 자산(R&D, 특화 설비, 전문 노하우)을 선투자했으나 상호 인질(Mutual Hostage)이나 구속력 있는 계약이 부재함.",
                "remedy": "상호 인질(Mutual Hostage) 계약 체결, 마일스톤 분할 지급 에스크로 구축, 또는 대체 퇴로(BATNA) 사전 확보."
            })
            severity = "CRITICAL"

        # 2. Past favor check
        if payload.relies_on_past_favors_or_loyalty and not payload.has_vested_future_incentives:
            triggers.append({
                "code": "[TRIGGER-GT-PAST-FAVOR]",
                "severity": "HIGH",
                "name": "항우의 착각 / 과거 은혜 의존 경보",
                "diagnosis": "상대방의 미래 행동을 유도함에 있어 과거의 은혜(Sunk Cost)에 의존하고 있으며, 상대방에게 미래의 실질적 인센티브가 부재함.",
                "remedy": "한순구 공리: '인간은 과거의 고마움이 아니라 미래의 이익에 움직인다.' 옹치 포상법(미래 보상 앵커링) 및 황금 메추리알 분할 보상 구조 적용."
            })
            if severity != "CRITICAL":
                severity = "HIGH"

        # 3. Cheap talk check
        if payload.uses_unbacked_threat_or_bluff:
            triggers.append({
                "code": "[TRIGGER-GT-CHEAP-TALK]",
                "severity": "HIGH",
                "name": "고르바초프의 패착 / 실행 불가능한 공갈 위협 경보",
                "diagnosis": "상대방이 불응했을 때 위협을 실행하면 자신도 치명상을 입어 실행할 수 없는 '신뢰성 없는 위협(Non-credible Threat)'임.",
                "remedy": "선제적 구속(Credible Commitment) 구축 또는 위협 실행의 자동화(스마트 컨트랙트, 평판 걸람, 배수진)."
            })
            if severity != "CRITICAL":
                severity = "HIGH"

        # 4. Reputation crack check
        if payload.exposes_core_reputation_to_stalemate:
            triggers.append({
                "code": "[TRIGGER-GT-REPUTATION-CRACK]",
                "severity": "CRITICAL",
                "name": "아사쇼류·가마쿠라 명성 붕괴 경보",
                "diagnosis": "단기 1회의 소액 이익을 위해 장기 반복 게임의 핵심 명성 자산(Reputation Capital)을 소모할 위험에 노출됨.",
                "remedy": "장기 반복 게임 할인계수(delta) 재평가, 명성 손실 가중치 반영 후 단기 양보 또는 명성 보존 퇴로 선택."
            })
            severity = "CRITICAL"

        # 5. Team moral hazard check
        if payload.team_size_n > 1 and not payload.individual_effort_observable:
            triggers.append({
                "code": "[TRIGGER-GT-FREE-RIDER]",
                "severity": "HIGH",
                "name": "팀 내 도덕적 해이 / 1/N 무임승차 경보",
                "diagnosis": f"팀 규모 {payload.team_size_n}명에서 개인 기여도가 관측되지 않아 1/N 무임승차 유인이 지배전략이 됨.",
                "remedy": "토너먼트형 상대평가 보상, 개인 기여 모듈 원자화, VCG 피벗 메커니즘을 통한 외부효과 내부화."
            })
            if severity != "CRITICAL":
                severity = "HIGH"

        # 6. Kingpin check
        if payload.over_engineers_non_bottleneck:
            triggers.append({
                "code": "[TRIGGER-GT-KINGPIN]",
                "severity": "MEDIUM",
                "name": "헨리 포드의 킹핀 / 과잉 스펙 자원 낭비 경보",
                "diagnosis": "시스템 전체의 붕괴를 결정하는 핵심 병목(Kingpin)이 아닌 비병목 요소에 과도한 자본과 스펙을 투입하고 있음.",
                "remedy": "비병목 자원을 적정 수준으로 감축(Down-spec)하고 절감된 자원을 핵심 킹핀 강화에 재배치."
            })

        # 7. Ruin bet check
        if payload.downside_loss_exceeds_safe_capital:
            triggers.append({
                "code": "[TRIGGER-GT-RUIN-BET]",
                "severity": "FATAL",
                "name": "파산 확률 노출 / 비대칭 파멸 경보",
                "diagnosis": "아무리 승률이나 기댓값이 높아도 1회 실패 시 생존이 불가능한 파산 위험(Ruin Risk)을 안고 있음.",
                "remedy": "E-Stop 즉시 발동: 켈리 기준(Kelly Criterion) 재산정, 베팅 규모 축소, 생존 현금 완충선 절대 확보."
            })
            severity = "FATAL"

        
        # 8. Fair Trade Art 40 collusion check
        if getattr(payload, "exchanges_competitor_price_info", False):
            triggers.append({
                "code": "[TRIGGER-GT-FAIR-TRADE-40]",
                "severity": "CRITICAL",
                "name": "공정거래법 제40조 담합 추정 경보",
                "diagnosis": "경쟁 병원과의 마케팅 자제 합의나 가격·예산 정보 교환은 공정거래법상 부당한 공동행위로 추정되어 형사처벌 및 과징금 대상임.",
                "remedy": "경쟁사 정보교환을 즉시 중단하고, 장기 공존 반복게임(delta >= 0.5)의 독자적 관찰 판단과 진료 차별화로 전략 전환."
            })
            severity = "CRITICAL"

        # 9. Labor Standard Art 20 signing bonus clawback check
        if getattr(payload, "has_signing_bonus_clawback_clause", False):
            triggers.append({
                "code": "[TRIGGER-GT-LABOR-20]",
                "severity": "HIGH",
                "name": "근로기준법 제20조 위약 예정 무효 경보",
                "diagnosis": "사이닝보너스 선지급 후 의무근무 위반 시 전액 반환하게 하는 약정은 위약금 예정으로 대법원 판례상 무효화될 위험이 큼.",
                "remedy": "'선지급 후 반환' 대신 2~3년에 걸친 '근속 조건부 분할 이연 지급' 구조로 계약 변경."
            })
            if severity != "CRITICAL":
                severity = "HIGH"

        is_safe = len(triggers) == 0
        return {
            "scenario": payload.scenario_name,
            "overall_status": "APPROVED" if is_safe else ("HALT_FATAL" if severity == "FATAL" else "TRIGGERED_WARNING"),
            "severity": severity,
            "triggered_count": len(triggers),
            "triggers": triggers
        }


def main():
    parser = argparse.ArgumentParser(description="Neuro-Symbolic Game Theory & Mechanism Design Decision Engine")
    subparsers = parser.add_subparsers(dest="command")

    audit_p = subparsers.add_parser("audit", help="Audit a scenario against the 6 Strategic Immune Triggers")
    audit_p.add_argument("--scenario", type=str, required=True, help="Scenario name")
    audit_p.add_argument("--holdup", action="store_true", help="Requires unilateral sunk cost without hostage")
    audit_p.add_argument("--past-favor", action="store_true", help="Relies on past favors without future incentives")
    audit_p.add_argument("--cheap-talk", action="store_true", help="Uses unbacked threat or bluff")
    audit_p.add_argument("--reputation-crack", action="store_true", help="Exposes core reputation to stalemate")
    audit_p.add_argument("--team-size", type=int, default=1, help="Team size N")
    audit_p.add_argument("--unobservable-effort", action="store_true", help="Individual effort unobservable")
    audit_p.add_argument("--over-engineer", action="store_true", help="Over-engineers non-bottlenecks")
    audit_p.add_argument("--ruin-bet", action="store_true", help="Downside exceeds safe capital")

    args = parser.parse_args()

    if args.command == "audit":
        payload = StrategicDecisionPayload(
            scenario_name=args.scenario,
            requires_unilateral_sunk_cost=args.holdup,
            has_binding_mutual_hostage=False,
            relies_on_past_favors_or_loyalty=args.past_favor,
            has_vested_future_incentives=False,
            team_size_n=args.team_size,
            individual_effort_observable=not args.unobservable_effort,
            uses_unbacked_threat_or_bluff=args.cheap_talk,
            exposes_core_reputation_to_stalemate=args.reputation_crack,
            over_engineers_non_bottleneck=args.over_engineer,
            downside_loss_exceeds_safe_capital=args.ruin_bet
        )
        res = GameTheoryImmuneAuditor.audit(payload)
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        parser.print_help()




class HospitalMechanismCalculator:
    """
    Mathematical decision calculators for hospital management & clinical operations
    """
    @staticmethod
    def loyalty_threshold(future_loyalty_payoff_L: float, outside_offer_D: float) -> Dict[str, Any]:
        """
        Calculates loyalty threshold probability p* = L / (L + D)
        """
        if future_loyalty_payoff_L + outside_offer_D <= 0:
            return {"error": "Invalid payoffs"}
        p_star = future_loyalty_payoff_L / (future_loyalty_payoff_L + outside_offer_D)
        return {
            "future_loyalty_payoff_L": future_loyalty_payoff_L,
            "outside_offer_D": outside_offer_D,
            "loyalty_threshold_p_star": round(p_star, 4),
            "loyalty_threshold_pct": round(p_star * 100, 2),
            "interpretation": f"상대방의 이직 성공 확률이 {round(p_star * 100, 1)}% 이하일 때 병원에 잔류함. L을 늘릴수록 잔류 내성 강화."
        }

    @staticmethod
    def shapley_spine_center() -> Dict[str, Any]:
        """
        Shapley value calculation for NDB Spine Center (Ortho O, Pain P, Rehab R)
        v(O)=6, v(P)=3, v(R)=1, v(OP)=12, v(OR)=9, v(PR)=5, v(OPR)=18
        """
        # Shapley values analytically computed over 6 permutations
        # O: 9.167 (50.9%), P: 5.667 (31.5%), R: 3.167 (17.6%)
        return {
            "grand_coalition_value": 18,
            "shapley_values": {
                "ortho_surgery_O": round(55.0 / 6.0, 2),   # 9.17
                "pain_intervention_P": round(34.0 / 6.0, 2),# 5.67
                "rehabilitation_R": round(19.0 / 6.0, 2)   # 3.17
            },
            "ratio_percentage": {
                "ortho_surgery_O": 50.9,
                "pain_intervention_P": 31.5,
                "rehabilitation_R": 17.6
            },
            "policy_implication": "단순 매출 비율(재활 1.8) 대신 섀플리 값 3.17을 배분해야 재활의학과의 다학제 협진 참여 유인이 유지됨."
        }

    @staticmethod
    def nursing_bankrun_threshold(stay_payoff: float = 6.0, solo_payoff: float = 2.0, leave_payoff: float = 5.0) -> Dict[str, Any]:
        """
        Coordination game threshold q* for nursing turnover bank run:
        q* * stay + (1 - q*) * solo >= leave <=> q* = (leave - solo) / (stay - solo)
        """
        q_star = (leave_payoff - solo_payoff) / (stay_payoff - solo_payoff)
        return {
            "stay_payoff": stay_payoff,
            "solo_left_payoff": solo_payoff,
            "leave_payoff": leave_payoff,
            "threshold_q_star": round(q_star, 4),
            "threshold_q_star_pct": round(q_star * 100, 2),
            "policy_insight": "동료 잔류 믿음이 q* 이상이어야 잔류함. '혼자 남을 때 대체인력 풀'을 제공해 solo_payoff를 2->4로 올리면 q*가 75%에서 50%로 대폭 개선됨."
        }

    @staticmethod
    def radiology_make_or_buy(unit_buy_cost_krw: int = 20000, monthly_admin_cost_krw: int = 8000000, monthly_fixed_make_cost_krw: int = 65000000) -> Dict[str, Any]:
        """
        Transaction cost economics make vs buy breakeven:
        unit_buy * N + admin == fixed_make <=> N* = (fixed_make - admin) / unit_buy
        """
        bep_n = int((monthly_fixed_make_cost_krw - monthly_admin_cost_krw) / unit_buy_cost_krw)
        return {
            "unit_buy_cost_krw": unit_buy_cost_krw,
            "monthly_admin_cost_krw": monthly_admin_cost_krw,
            "monthly_fixed_make_cost_krw": monthly_fixed_make_cost_krw,
            "breakeven_monthly_reads_N_star": bep_n,
            "decision_rule": f"월 판독량이 {bep_n:,}건을 초과하면 직영(Make)이 유리함."
        }


class DecisionPitfallsEvaluator:
    """
    Evaluator for Auction Succession, Voting Systems, and Bayesian Calibration
    """
    @staticmethod
    def succession_audit(is_sequential: bool, candidate_count: int) -> Dict[str, Any]:
        if is_sequential:
            return {
                "system": "순차적 심사 (Sequential Evaluation)",
                "risk": "HIGH_VULNERABILITY",
                "diagnosis": "초반 유력 후보는 사소한 흠결에 집중 견제되어 낙마하고, 마지막 후보는 대안 부재로 치명적 결격자임에도 졸속 당선될 위험 큼.",
                "remedy": "청나라 황태자 밀건법(密建法) 및 밀그롬 동시 경매 적용: 모든 후보를 동일 시점에 걸어두고 시작과 종료를 일치시켜 동시 비교·검증."
            }
        return {
            "system": "동시 심사 (Simultaneous Evaluation / 밀건법)",
            "status": "APPROVED",
            "diagnosis": f"{candidate_count}명의 후보가 상호 비교·학습을 거치며 정당한 가치 평가에 도달함."
        }

    @staticmethod
    def voting_simulation(first_choice_pct: Dict[str, float], pairwise_matrix: Optional[Dict[str, Dict[str, float]]] = None) -> Dict[str, Any]:
        plurality_winner = max(first_choice_pct, key=first_choice_pct.get)
        return {
            "plurality_winner": plurality_winner,
            "plurality_shares": first_choice_pct,
            "warning": "1인 1표 최선호 투표는 비호감도와 2·3순위 선호를 묵살하여 과반수가 반대하는 후보가 당선되는 왜곡 발생 가능(회식 메뉴 역설).",
            "recommendation": "선호 순위 투표용지(Ranked-Choice Ballot) 또는 보르다 투표(Borda Count) 도입 권고."
        }

    @staticmethod
    def bayesian_calibration(objective_base_rate_pct: float, subjective_belief_pct: float, occupation_context: str = "") -> Dict[str, Any]:
        bias = subjective_belief_pct - objective_base_rate_pct
        return {
            "occupation_context": occupation_context,
            "objective_base_rate_pct": objective_base_rate_pct,
            "subjective_belief_pct": subjective_belief_pct,
            "calibration_error_pct": round(bias, 2),
            "diagnosis": "과도한 부정 편향 (광해군 증후군: 기회 상실 위험)" if bias > 10 else ("과도한 긍정 편향 (콤모두스·연산군 증후군: 파멸 위험)" if bias < -10 else "영점 조절 양호 (Calibrated)"),
            "prescription": "직업적·일상적 협소한 표본을 벗어나, 객관적 통계와 독서를 통해 주관적 확률을 5% 수준으로 영점 조절해야 함."
        }


class BayesianFiveStepCalibrator:
    """
    5-Step Thought Calibration Engine: Eliminates AI Overconfidence and Anchoring
    """
    @staticmethod
    def calibrate(base_rate_pct: float, evidence_deltas: List[float], raw_ai_confidence_pct: float, is_high_stakes: bool = True) -> Dict[str, Any]:
        # Step 1: Clamp base rate (no 0% or 100%)
        prior = max(1.0, min(99.0, base_rate_pct))
        
        # Step 3: Explicit step update
        updated_prob = prior + sum(evidence_deltas)
        updated_prob = max(1.0, min(99.0, updated_prob))
        
        # Step 4: Confidence deflation (deflate raw AI overconfidence towards updated prob)
        # Brier score / temperature scaling penalty
        overconfidence_gap = raw_ai_confidence_pct - updated_prob
        deflation_penalty = overconfidence_gap * 0.4 if overconfidence_gap > 0 else 0
        calibrated_prob = round(updated_prob - deflation_penalty, 1)
        
        # Step 5: Action thresholding
        threshold = 90.0 if is_high_stakes else 60.0
        can_execute = calibrated_prob >= threshold
        
        action_decision = "EXECUTE" if can_execute else ("HALT_AND_PROBE" if calibrated_prob >= 40.0 else "REJECT_ABORT")
        missing_info_probe = None
        if action_decision == "HALT_AND_PROBE":
            missing_info_probe = "승률이 불확실한 구간입니다. 섣불리 결론 내지 말고, 가설 검증을 바꿀 '가장 중요한 단 하나의 추가 팩트'를 먼저 확인하십시오."

        return {
            "step1_prior_base_rate": prior,
            "step2_evidence_count": len(evidence_deltas),
            "step3_updated_prob": round(updated_prob, 1),
            "step4_raw_confidence": raw_ai_confidence_pct,
            "step4_calibrated_prob": calibrated_prob,
            "step5_stakes": "HIGH_STAKES (건강·대규모 자금, 기준선 90%)" if is_high_stakes else "LOW_STAKES (경상 업무, 기준선 60%)",
            "step5_threshold": threshold,
            "action_decision": action_decision,
            "missing_info_probe": missing_info_probe
        }


class EvolutionaryGameEvaluator:
    """
    Evaluator for Hamilton's Rule and Tit-for-Tat Reciprocal Cooperation
    """
    @staticmethod
    def hamilton_rule_audit(relatedness_r: float, benefit_B: float, cost_C: float) -> Dict[str, Any]:
        rb = relatedness_r * benefit_B
        net_altruistic_fitness = rb - cost_C
        is_viable = net_altruistic_fitness > 0
        return {
            "relatedness_r": relatedness_r,
            "benefit_B": benefit_B,
            "cost_C": cost_C,
            "rB": round(rb, 2),
            "altruism_viable": is_viable,
            "diagnosis": "유전자 사본 관점에서 이타적 헌신이 진화적으로 보상됨 (rB > C)" if is_viable else "개체의 희생이 유전적 이익을 초과하여 자연선택에서 도태됨 (rB <= C)",
            "management_translation": "직원은 r=0이므로 도덕적 헌신 강요 금지. 인센티브/지분 설계를 통해 인위적 공유도 r을 부여해야 함."
        }

    @staticmethod
    def tit_for_tat_strategy_audit(is_nice: bool, is_retaliatory: bool, is_forgiving: bool, is_clear: bool) -> Dict[str, Any]:
        flaws = []
        if not is_nice:
            flaws.append("먼저 배신(선제 공격)하여 불필요한 보복 악순환을 자초함.")
        if not is_retaliatory:
            flaws.append("배신당하고도 즉각 보복하지 않아 사기꾼과 무임승차자의 '호구(Sucker)'가 됨.")
        if not is_forgiving:
            flaws.append("상대가 협력으로 복귀해도 용서하지 않아 무한 치킨게임으로 공멸함.")
        if not is_clear:
            flaws.append("전략이 모호하여 상대방이 협력의 이득을 계산하지 못하고 오판을 유도함.")

        is_perfect_tft = len(flaws) == 0
        return {
            "strategy": "Tit-for-Tat (팃포탯)",
            "is_evolutionarily_stable": is_perfect_tft,
            "flaws": flaws,
            "score": f"{4 - len(flaws)} / 4",
            "golden_rule": "1) 먼저 신의(Nice), 2) 배신 시 즉각 보복(Retaliatory), 3) 복귀 시 즉각 용서(Forgiving), 4) 단순 투명한 원칙(Clear)."
        }


class HumanObjectiveEvaluator:
    """
    Evaluator for 3-Tier Human Objective Function: max u_i = f(Survival, Reproduction, Prosperity)
    """
    @staticmethod
    def evaluate_alignment(agent_survival_benefit: bool, agent_prosperity_benefit: bool, org_goal_benefit: bool) -> Dict[str, Any]:
        aligned = (agent_survival_benefit or agent_prosperity_benefit) and org_goal_benefit
        return {
            "agent_objective_served": agent_survival_benefit or agent_prosperity_benefit,
            "organizational_goal_served": org_goal_benefit,
            "incentive_aligned": aligned,
            "diagnosis": "유인 일치(Incentive Alignment) 성공: 직원이 자신의 생존과 번영을 위해 자발적으로 협력함." if aligned else "유인 불일치(Incentive Conflict): 도덕적 헌신 강요로 인해 무임승차 또는 이탈 위험 높음.",
            "prescription": "직원의 개인 목적함수(급여, 성장, 미래 안정)와 병원 목표를 1:1로 묶는 보상 메커니즘 재설계 필요."
        }

if __name__ == "__main__":
    main()
