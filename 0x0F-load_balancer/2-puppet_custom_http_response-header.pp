# Configuring Http header
exec { 'HTTP_Header':
  command  => 'sudo apt-get update -y; sudo apt-get install nginx -y; sudo sed -i "35i\ add_header X-Served-By \$HOSTNAME;" /etc/nginx/sites-available/default; sudo service nginx start',
}
