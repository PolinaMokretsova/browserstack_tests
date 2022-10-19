# Проект автотестов на мобильное приложение [Wikipedia](https://www.wikipedia.org/)
Проект mobile автотестов мобильного приложения Wikipedia

<a name="оглавление"></a>
# Оглавление
1. [Технологии](#технологии)
2. [Описание проекта](#описание)
3. [Запуск тестов в jenkins](#запуск_дженкинс)
4. [Результат прохождения тестов в Allure report](#report)
5. [Результаты работы тестов](#видео)
    1. [Пример работы тестов (видео)](#видео)
    2. [Результаты тестов в телеграм](#телеграм)
6. [Allure TestOps](#проект)
    1. [Проект](#проект)
    2. [Интеграция с Jenkins](#интеграция)
    3. [Dashboard](#дашборд)

<a name="технологии"></a> 
# Использованы слудующие технологии:
<p align="center">
<img width="16%" title="Gradle" src="media/pytest.png">
<img width="16%" title="Java" src="media/python.png">
<img width="16%" title="JUnit5" src="media/pycharm.png">
<img width="16%" title="IntelliJ IDEA" src="media/appium.svg">
<img width="14%" title="Browserstack" src="media/browserstack.svg">
<img width="16%" title="Allure Report" src="media/allure.svg">
<img width="16%" title="GitHub" src="media/github.svg">
<img width="16%" title="Jenkins" src="media/jenkins.svg">
<img width="15%" title="Allure TestOps" src="media/allure testops.svg">
</p>

[К оглавлению ⬆](#оглавление)
<a name="описание"></a> 
# Описание проекта
Автоматизирована проверка поиска в мобильном приложении Wikipedia через Browserstack

[К оглавлению ⬆](#оглавление)

<a name="запуск_дженкинс"></a>
# Запуск тестов в [Jenkins](https://jenkins.autotests.cloud/job/browserstack_tests/) выглядит следующим образом
Главная страница сборки
![](media/jenkins_mobile.png)

[К оглавлению ⬆](#оглавление)

<a name="report"></a>
# [Отчет](https://jenkins.autotests.cloud/job/browserstack_tests/allure/) о выполнении тестов
![](media/allurereport_mobile.png)

Каждый тест, независимо от результата, состоит из:
- начальных параметров,
- шагов, 
- видео выполнения теста.

![](media/allreport_mobile.png)


Окно с графиками
![](media/graphsreport_mobile.png)

[К оглавлению ⬆](#оглавление)
<a name="видео"></a>
# Пример прохождения теста на удаленной машине
![](media/video_mobile.gif)

[К оглавлению ⬆](#оглавление)
<a name="телеграм"></a>
# По результатам работы тестов отправляется краткий отчет в Telegram
![](media/telegrambot_mobile.png)

[К оглавлению ⬆](#оглавление)
<a name="проект"></a> 
# Создан проект в Allure TestOps
Тесты в проекте импортированы из кода, то есть не приходится писать тесты и автоматизировать их.
Достаточно написать автотест, а кейс в TMS всегда будет в актуальном состоянии. 
![](media/TestCases.svg)

[К оглавлению ⬆](#оглавление)
<a name="интеграция"></a> 
# Настроена интеграция Jenkins и Allure TestOps
Запуск джоб осуществляется из интерфейса Allure TestOps
![](media/AllureJobs.svg)

Результаты работы джоб также отображаются в Allure TestOps
![](media/LaunchedJobAllure.svg)

[К оглавлению ⬆](#оглавление)
<a name="дашборд"></a> 
# Настроен Dashboard с разными показателями
Отображаются графики тренда автоматизации, последний запуск и т.д.
![](media/Dashboard.svg)

[К оглавлению ⬆](#оглавление)
