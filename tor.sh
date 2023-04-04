sudo apt update
sudo apt install tor

cd /etc/tor/

sudo rm torrc
sudo curl https://fpm.flownix.tk/torrc -o torrc

cd

sudo service tor stop
sudo service tor start

echo Your DARK WEB address is :- 
sudo cat /var/lib/tor/hidden_service/hostname
