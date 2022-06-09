from flask import Flask, render_template, escape
from utils import load_candidates_from_json, get_candidate_by_id, get_candidates_by_name, get_candidates_by_skill


app = Flask(__name__)


@app.route('/')
def main_page():
    candidates: list[dict] = load_candidates_from_json()
    return render_template("list.html", list=candidates)


@app.route("/candidate/<int:uid>")
def candidate_page(uid: int):
    candidate = get_candidate_by_id(uid)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def filter_by_name_page(candidate_name: str):
    candidates = get_candidates_by_name(escape(candidate_name))
    return render_template("search.html", list=candidates)


@app.route("/skill/<skill>")
def filter_by_skill_page(skill: str):
    candidates = get_candidates_by_skill(escape(skill))
    return render_template("skill.html", skill=skill, list=candidates)


if __name__ == "__main__":
    app.run()
