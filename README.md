# manage_packages
Задания:
1)Создать свой RPM пакет  (можно взять свое приложение, либо собрать, например, апач с определенными опциями)  
2) Создать свой репозиторий и разместить там ранее собранный RPM


Код взят из репозитория https://github.com/LukeShirnia/OOM-Killer-score
Программа выводит в консоль список запущенных процессов с oom_score.

1) Сборка rpm выполнялась командой 
rpmbuild -bb score_check.spec 
-только RPM 

Установка приложения 
rpm -i Score-check-oom-1-1.x86_64.rpm

Запуск приложения 
score_check


2) Репозиторий размещен по адресу http://185.177.95.135/repo/
Nginx запущен в docker контейнере на vds
Команда для запуска контейнера : docker run \--name nginx \-v /srv/nginx/:/usr/share/nginx/html \-p 80:80 \-d nginx

Создание репозитория в ubuntu: 
createrepo_c /srv/nginx/repo/
где /srv/nginx/repo/ - каталог с rpm 

Добавление репозитория

cat >> /etc/yum.repos.d/otus.repo << EOF
[otus]
name=otus
baseurl=http://185.177.95.135/repo/
gpgcheck=0
enabled=1
EOF

Установка приложения
yum install -y Score-check-oom-1-1.x86_64.rpm
