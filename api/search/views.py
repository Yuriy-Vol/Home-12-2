import logging

from functions import json_load, search_word
from flask import Blueprint, render_template, request
from config import POST_PATH
import os.path

logging.basicConfig(level=logging.INFO, filename="logging.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")


@search_blueprint.route("/search/")
def search_page():
    search_arg = request.args.get("s", "").lower()
    if os.path.exists(POST_PATH):
        try:
            search_list = search_word(json_load(POST_PATH), search_arg)
        except Exception:
            logging.error('ошибка загрузки json')
            return 'ошибка загрузки json'
        return render_template("post_list.html", search_arg=search_arg, list=search_list)
    logging.error(f'файла {POST_PATH} не существует')
    return f'файла {POST_PATH} не существует'
