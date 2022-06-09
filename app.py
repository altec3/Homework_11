from flask import Flask, render_template, escape, request
from utils import load_candidates_from_json, get_candidate_by_id, get_candidates_by_name, get_candidates_by_skill


app = Flask(__name__)


@app.route('/')
def main_page():
    candidates: list[dict] = load_candidates_from_json()
    return render_template("list.html", list=candidates)


@app.route("/candidate/<int:uid>")
def candidate_page(uid: int):
    candidate: dict = get_candidate_by_id(uid)
    if candidate:
        return render_template("card.html", candidate=candidate)
    return "<h1>Кандидата с таким ID не существует</h1>"


@app.route("/search/")
def filter_by_name_page():
    candidate_name: str = request.args.get("name")
    candidates = get_candidates_by_name(escape(candidate_name))
    if candidates:
        return render_template("search.html", list=candidates)
    return "<h1>Совпадений не обнаружено</h1>"


@app.route("/skill/")
def filter_by_skill_page():
    skill: str = request.args.get("skill")
    candidates = get_candidates_by_skill(escape(skill))
    if candidates:
        return render_template("skill.html", skill=skill, list=candidates)
    return "<h1>Совпадений не обнаружено</h1>"


if __name__ == "__main__":
    app.run()
