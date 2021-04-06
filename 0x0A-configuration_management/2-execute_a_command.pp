# Execute command
exec { "killmenow":
command => 'pkill -f killmenow',
path    => 'shell',
}
