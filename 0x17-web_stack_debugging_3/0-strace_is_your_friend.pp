# fixing Error 500 changing line
exec { 'Fixing line':
    command => '/usr/bin/sudo /bin/sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
}

