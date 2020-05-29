# fix hard, soft nofile
exec {'fix soft':
path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command => "sudo sed -i 's/holberton soft nofile 4/holerton soft nofile 700000/' /etc/security/limits.conf; /sbin/sysctl -p",
}
exec {'fix hard':
path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command => "sudo sed -i 's/holberton hard nofile 5/holerton hard nofile 700000/' /etc/security/limits.conf; /sbin/sysctl -p",
}
