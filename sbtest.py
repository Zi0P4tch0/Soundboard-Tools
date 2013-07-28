#!/usr/local/bin/python

##########################################################################
#                                                                        #
#  This file is part of Soundboard.                                      #
#                                                                        #
#  Soundboard is free software: you can redistribute it and/or modify    #
#  it under the terms of the GNU General Public License as published by  #
#  the Free Software Foundation, either version 3 of the License, or     #
#  any later version.                                                    #
#                                                                        #
#  Soundboard is distributed in the hope that it will be useful,         #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#  GNU General Public License for more details.                          #
#                                                                        #
#  You should have received a copy of the GNU General Public License     #
#  along with Soundboard.  If not, see <http:#www.gnu.org/licenses/>.    #
#                                                                        #
##########################################################################

VERSION='1.1'

import os
import struct
import sys
from xml.dom import minidom

if __name__ == '__main__':
    
    print 'SoundBoard Test Tool v' + VERSION + '\n'
    
    if len(sys.argv) != 2:
        print 'Usage: ./sbtool.py SOUNDBOARD_FILE'
        print 'Example: ./sbtool.py soundboard.sb'
        sys.exit(1)
        
    if not os.path.isfile(sys.argv[1]):
        print 'Error: "' + sys.argv[1] + '" is not a file!'
        sys.exit(2)
        
    sb = open(sys.argv[1],'rb')
    
    sb_name_len = struct.unpack('<I',sb.read(4))[0]
    sb_name = str(sb.read(sb_name_len))
    sb_version_len = struct.unpack('<I',sb.read(4))[0]
    sb_version = str(sb.read(sb_version_len))
    sb_author_len = struct.unpack('<I',sb.read(4))[0]
    sb_author = str(sb.read(sb_author_len))
    sb_date_len = struct.unpack('<I',sb.read(4))[0]
    sb_date = str(sb.read(sb_date_len))
    
    print 'Soundboard: "' + sb_name + '".'
    print 'Version: "' + sb_version + '".'
    print 'Author: "' + sb_author + '".'
    print 'Date: "' + sb_date + '".'
    
    sb_icon_size = struct.unpack('<I',sb.read(4))[0]
    
    sb.read(sb_icon_size)
    
    print 'Icon Size: ' + str(sb_icon_size) + ' bytes.'
    
    sb_clips_len = struct.unpack('<I',sb.read(4))[0]
    
    print 'Clips: ' + str(sb_clips_len) + '.'
    
    for clip_no in range(0,sb_clips_len):
        
        sb_clip_title_len = struct.unpack('<I',sb.read(4))[0]
        sb_clip_title = str(sb.read(sb_clip_title_len))
        sb_clip_size = struct.unpack('<I',sb.read(4))[0]
        
        print 'Clip #' + str(clip_no+1) + ': "' + sb_clip_title + '" (size ' + str(sb_clip_size) + ' bytes).'
        
        sb.read(sb_clip_size)
    
    sb.close()
    