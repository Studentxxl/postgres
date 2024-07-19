

from jinja2 import Template


template = Template('Hello {{ name }}!')
print(template.render(name='John Doe'))



content = {'a': 5, 'b': 2}
tpl = 'Сумма чисел {{ a }} и {{ b }} равна {{ a + b }}'
print(Template(tpl).render(content))


tpl = """{{ title }}
{{ '-' * title|length }}
{% for n, user in enumerate(users, 1) %}
{{ n }}. {{ user.name }} - должность: {{ user.status }}, оклад: ${{ user.salary }}
{% endfor %}
"""
# собираем данные для шаблона
content = {}
content['title'] = 'Итерация по пользователям'
content['users'] = []
content['users'].append({'name': 'Маша', 'status': 'Менеджер', 'salary': 1500})
content['users'].append({'name': 'Света', 'status': 'Дизайнер', 'salary': 1000})
content['users'].append({'name': 'Игорь', 'status': 'Программист', 'salary': 2000})
# В словаре передаем в шаблон функцию Python
content['enumerate'] = enumerate
# Смотрим, что получилось
print(Template(tpl, trim_blocks=True).render(content))
# Итерация по пользователям
# -------------------------
# 1. Маша - должность: Менеджер, оклад: $1500
# 2. Света - должность: Дизайнер, оклад: $1000
# 3. Игорь - должность: Программист, оклад: $2000


















