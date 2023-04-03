sudo apt update
sudo apt install tor
sudo apt install npm

cd /etc/tor/

sudo curl https://flownixincorporated.github.io/torrc -o torrc

cd

sudo service tor stop
sudo service tor start

sudo npm -s 127.0.0.1:8000
