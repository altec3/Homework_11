import json
CANDIDATES = "candidates.json"


def load_candidates_from_json(path: str = CANDIDATES) -> list[dict]:
    """
    Возвращает список всех кандидатов

    :param path:
    :return:
    """
    with open(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def get_candidate_by_id(uid: int) -> dict | None:
    """
    Возвращает одного кандидата по его id

    :param uid:
    :return:
    """
    lst: list[dict] = load_candidates_from_json()
    for candidate in lst:
        if candidate["id"] == uid:
            return candidate
    return None


def get_candidates_by_name(candidate_name: str) -> list[dict] | None:
    """
    Возвращает кандидатов по имени

    :param candidate_name:
    :return:
    """
    candidates = []
    lst: list[dict] = load_candidates_from_json()
    for candidate in lst:
        if candidate_name.lower() in candidate["name"].lower():
            candidates.append(candidate)
    if candidates:
        return candidates
    return None


def get_candidates_by_skill(skill_name: str) -> list[dict] | None:
    """
    Возвращает кандидатов по навыку

    :param skill_name:
    :return:
    """
    candidates = []
    lst: list[dict] = load_candidates_from_json()
    for candidate in lst:
        skills: list = candidate["skills"].lower().split(",")
        if skill_name.lower() in skills:
            candidates.append(candidate)
    if candidates:
        return candidates
    return None
