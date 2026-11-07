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


if __name__ == "__main__":
    main()
