import json
import os.path
import logging
from config import UPLOAD_FOLDER

logging.basicConfig(level=logging.INFO, filename="logging.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


# Загрузка данных из json файла
def json_load(path):
    if os.path.exists(path):
        with open(path, "r", encoding="UTF-8") as f:
            try:
                full_list = json.load(f)
            except json.decoder.JSONDecodeError:
                logging.error('ошибка загрузки json')
                return 'ошибка загрузки json'
            else:
                return full_list
    logging.error('Файл posts.json отсутствует')
    return 'Файл posts.json отсутствует'


# Поиск постов по ключевому слову
def search_word(full_list: dict, search_arg: str) -> list:
    search_list = []
    for post in full_list:
        if search_arg.lower() in post["content"].lower():
            search_list.append(post)
    return search_list


# Сохранение картинки при добавлении поста
def save_picture(picture):
    picture_filename = picture.filename
    path_picture = UPLOAD_FOLDER + picture_filename
    picture.save(path_picture)
    return path_picture[1:]


# Сохранение поста в json файл
def save_post(post: dict, path):
    posts = json_load(path)
    posts.append(post)
    with open(path, "w", encoding="UTF-8") as f:
        try:
            json.dump(posts, f, ensure_ascii=False, sort_keys=True, indent="\t")
        except Exception:
            logging.error('Ошибка сохранения поста')
            return 'Ошибка сохранения поста'
