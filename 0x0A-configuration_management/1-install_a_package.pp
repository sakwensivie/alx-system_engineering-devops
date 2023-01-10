# A script to install the puppe-ling pacakge

package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
