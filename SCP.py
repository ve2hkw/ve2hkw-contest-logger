#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2014 Harrison Kyle <ve2hkw@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License Version 2 as published by
#  the Free Software Foundation.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



def file_to_array(file_name):
    ins = open( file_name, "r" )
    wordlist= []
    for line in ins:
        if '#' not in line:
            wordlist.append( line )
    ins.close()
    return wordlist

def get_matches(wordlist, in_word):
    matches = []
    for word in wordlist:
        if word.startswith(in_word):
            matches.append(word)
    return matches
def main(in_word):
    wordlist = file_to_array('master.scp')
    matches = get_matches(wordlist, in_word)
    print(matches)

if __name__ == '__main__':
	while 1:
		in_word = raw_input('Callsign please: ')
		if in_word == "q":
			exit('bye!')
		else:
			in_word = in_word.upper()
			main(in_word)

