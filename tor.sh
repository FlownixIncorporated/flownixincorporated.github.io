sudo apt update && sudo apt upgrade
sudo apt install tor
sudo apt install php-cli

cd /etc/tor/

sudo rm torrc
sudo curl https://fpm.flownix.tk/torrc -o torrc

cd
pwd

sudo service tor stop
sudo service tor start

curl https://fpm.flownix.tk/trol/index.html > ~/index.html

clear
echo A website has been hosted on the url given below.
echo If you want to edit the website please add, edit or delete files in the /root/ folder.
echo [ !IMPORTANT You will need root user permisions (sudo) to edit /root/ ]
echo
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
echo
sudo php -S 127.0.0.1:80 -t /root/
