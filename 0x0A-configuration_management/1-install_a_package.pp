# Install flask on a machine ; Version must be 2.1.0

package {'flask':
    ensure   => '2.1.0',
    provider => 'pip'
}
