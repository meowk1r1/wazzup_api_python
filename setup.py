from setuptools import setup, find_packages

setup(
    name='wazzup_api_python',  # Название вашей библиотеки
    version='0.1.0',  # Версия вашей библиотеки
    author='meowk1r1',  # Ваше имя или псевдоним
    author_email='dorentroof@ya.ru',  # Ваш email
    description='Python клиент для API Wazzup24.',  # Краткое описание
    long_description=open('README.md').read(),  # Длинное описание, как правило, это содержимое файла README.md
    long_description_content_type='text/markdown',  # Указывает, что формат длинного описания - markdown
    url='https://github.com/meowk1r1/wazzup_api_python',  # Ссылка на репозиторий вашего проекта
    packages=find_packages(),  # Автоматически находит пакеты в вашем проекте
    install_requires=[
        'requests',  # Указываем зависимость от библиотеки requests
    ],
    classifiers=[
        'Programming Language :: Python :: 3',  # Укажите поддерживаемую версию Python
        'License :: OSI Approved :: MIT License',  # Лицензия, под которой распространяется ваш проект
        'Operating System :: OS Independent',  # Ваш проект может быть установлен на любой ОС
    ],
    python_requires='>=3.6',  # Минимальная версия Python, необходимая для работы вашего пакета
)
