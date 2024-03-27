"""
Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через
контекст.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def news():
    news_list = [
        {
            'news_headline': 'Заголовок новости 1',
            'news_description': 'Описание новости 1',
            'publication_date': '25-03-2024',
        },
        {
            'news_headline': 'Заголовок новости 2',
            'news_description': 'Описание новости 2',
            'publication_date': '26-03-2024',
        },
        {
            'news_headline': 'Заголовок новости 3',
            'news_description': 'Описание новости 3',
            'publication_date': '27-03-2024',
        },
    ]
    context = {'news': news_list}
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
