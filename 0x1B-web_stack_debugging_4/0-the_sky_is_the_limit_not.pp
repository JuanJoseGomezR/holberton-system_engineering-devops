# change amount of requests limit
exec { 'increase-ULIMIT':
	  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 3000\"/g" /etc/default/nginx',
		    path    => ['/bin']
}
exec { 'restart-nginx':
	  command  => 'service nginx restart',
		     provider => shell,
		       require  => Exec['increase-ULIMIT']
}

