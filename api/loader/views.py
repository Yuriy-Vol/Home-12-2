import logging

from flask import Blueprint, render_template, request
import os.path
from config import POST_PATH
from functions import save_picture, save_post

logging.basicConfig(level=logging.INFO, filename="logging.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route("/post")
def load_post_page():
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def load_post():
    add_picture = request.files.get("picture")
    if add_picture.filename.rsplit(".", maxsplit=1)[1] not in ['jpg', 'png', 'jpeg']:
        logging.error('фото не jpg, png, jpeg')
        return 'фото не jpg, png, jpeg'
    add_content = request.form.get("content")

    if add_content and add_picture:
        path_picture = save_picture(add_picture)
        post = {"pic": path_picture, "content": add_content}
        if os.path.exists(POST_PATH):
            try:
                save_post(post, POST_PATH)
            except Exception:
                logging.error('Ошибка загрузки Json')
                return 'Ошибка загрузки Json'
        else:
            logging.error(f'файла {POST_PATH} не существует')
            return f'файла {POST_PATH} не существует'
        logging.info("пост добавлен")
        return render_template("post_uploaded.html", post=post)
    else:
        logging.error('Недостаточно данных для добавления поста')
        return 'Недостаточно данных для добавления поста'
