sudo apt update
sudo apt install tor

cd /etc/tor/

sudo curl https://flownixincorporated.github.io/torrc -o torrc

cd

sudo service tor stop
sudo service tor start

echo Your DARK WEB address is :- 
sudo cat /var/lib/tor/hidden_service/hostname
