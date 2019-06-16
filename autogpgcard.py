#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pexpect

child = pexpect.spawnu('gpg --card-edit')
child.expect('gpg/card> ')
child.sendline('admin')
child.expect('Admin commands are allowed')
child.sendline('name')
child.expect("Cardholder's surname: ")
child.sendline('Dayleryan')
child.expect("Cardholder's given name: ")
child.sendline('Ardavast')
child.expect("Admin PIN:")
child.sendline('12345678')

child.expect('gpg/card> ')
child.sendline('lang')
child.expect('Language preferences: ')
child.sendline('en')

child.expect('gpg/card> ')
child.sendline('sex')
child.expect('Sex \(\(M\)ale, \(F\)emale or space\): ')
child.sendline('m')

child.expect('gpg/card> ')
child.sendline('login')
child.expect('Login data \(account name\): ')
child.sendline('ardavast')

child.expect('gpg/card> ')
child.sendline('quit')
