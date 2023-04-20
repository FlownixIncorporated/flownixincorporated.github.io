sudo apt update && sudo apt upgrade
sudo apt install tor
sudo apt install php-cli

cd /etc/tor/

sudo rm torrc
sudo curl https://fpm.flownix.tk/torrc -o torrc

cd

sudo mkdir darkweb
echo MADE DIR
pwd
cd ./darkweb
pwd
echo CHANGED DIR

sudo service tor stop
sudo service tor start

sudo curl https://fpm.flownix.tk/ìndex.html -o index.html


echo Host a webserver in any directory using netcat, python, php
echo
echo
echo
echo
echo Your DARK WEB address is :- 
sudo cat /var/lib/tor/hidden_service/hostname
echo
echo
echo
echo

sudo php -S 127.0.0.1:80
