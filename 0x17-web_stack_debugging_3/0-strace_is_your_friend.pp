# Fixing wp issue
exec {'wp-settings':
  path    => ['/usr/bin', '/usr/sbin', '/bin/'],
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}