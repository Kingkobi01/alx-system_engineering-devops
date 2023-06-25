# Kill a command call killmenow with a puppet manifest

exec {'kill_killmenow_process':
    command => '/usr/bin/pkill killmenow',
}
