# KILL IT

exec {'pkill':
  command => 'pkill killmenow',
  path    => '/usr/bin'
}
