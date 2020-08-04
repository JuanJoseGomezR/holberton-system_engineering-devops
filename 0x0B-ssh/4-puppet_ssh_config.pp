# Bash script that set up your client SSH configuration file so 
# that you can connect to a server without typing a password

file_line { 'declare file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'passwd auth off':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
}