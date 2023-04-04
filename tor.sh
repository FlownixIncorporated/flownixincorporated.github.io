sudo apt install tor

cd /etc/tor/

sudo curl https://flownixincorporated.github.io/torrc -o torrc

cd

sudo service tor stop
sudo service tor start
