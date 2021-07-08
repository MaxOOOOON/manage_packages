# manage_packages

Код взят из репозитория https://github.com/LukeShirnia/OOM-Killer-score
Программа выводит в консоль список запущенных процессов с oom_score.

Сборка rpm выполнялась командой 
rpmbuild -bb score_check.spec 
-только RPM 

Установка приложения 
rpm -i Score-check-oom-1-1.x86_64.rpm

Запуск приложения 
score_check


Репозиторий размещен по адресу http://185.177.95.135/repo/
Nginx запущен в docker контейнере на vds


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