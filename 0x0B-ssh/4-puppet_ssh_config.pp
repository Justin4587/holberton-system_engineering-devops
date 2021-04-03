# ssh

class { 'ssh::client':
  PasswordAuthentication  =>  'no',
  user                    => 'ubuntu',
  type                    => 'ssh-rsa',
  key                     => '~/.ssh/holberton',
}
