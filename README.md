# sf_site


Расположение 

Main – это всегда актуальная версия существующего кода.

Для каждого нового компонента или функциональности создается отдельная feature-ветка, которая отличается от обычной только префиксом feature/. Это обеспечивает независимую разработку.

Все новые изменения вносятся напрямую в ветку Main через PR. После их должен проверить технический руководитель и провести слияние с веткой Main.

Код который развернут на продакшене помечается меткой prod. Таким образом, production-код и main-код – это не одно и то же, но в тоже процесс не усложнен большим количеством веток и слияний, а найти production-код всегда можно по метке.

Install
git clone https://github.com/needkeep/sf_site.git


Начало новой ветки:

git checkout master
git pull
git checkout -b название_нового_бранча

Коммит:

git add . добавить все в свой локальный репозиторий

Сохранить - git commit -m "some commit message"

Загрузить свою ветку в репозиторий - git push origin название_ветки

Название можно проверить в IDE или через git status

Финальный мердж:

git checkout master
git pull origin master
git merge название_твоей_ветки
git push origin master