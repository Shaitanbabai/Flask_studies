import os
import json
from flask import Flask, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from forms import UserForm
from config import Config  # Импортируем конфигурацию

app = Flask(__name__)
app.config.from_object(Config)  # Загрузка конфигурации из Config

# Функция для загрузки данных из файла JSON
def load_users_data():
    if os.path.exists(app.config['JSON_DATA_FILE']):
        with open(app.config['JSON_DATA_FILE'], 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  # Если файл пустой или содержит некорректный JSON, возвращаем пустой список
    return []

# Функция для сохранения данных в файл JSON
def save_users_data(card_data):
    with open(app.config['JSON_DATA_FILE'], 'w', encoding='utf-8') as file:
        json.dump(card_data, file, ensure_ascii=False, indent=4)

users_data = load_users_data()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        user_info = {
            'name': form.name.data,
            'email': form.email.data,
            'birth_date': form.birth_date.data.strftime('%Y-%m-%d'),
            'city': form.city.data,
            'photo': filename
        }
        users_data.append(user_info)
        save_users_data(users_data)  # Сохраняем данные при каждом добавлении пользователя
        return redirect(url_for('index'))

    return render_template('index.html', form=form, users=users_data)

if __name__ == '__main__':
    app.run(debug=True)