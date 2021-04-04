# ssh

file { '/home/thurman/holberton-system_engineering-devops/0x0B-ssh/2-ssh_config':
  ensure => present
}->
file_line { 'Host_line':
  line   => 'Host',
  path   => '/home/thurman/holberton-system_engineering-devops/0x0B-ssh/2-ssh_config'
}
