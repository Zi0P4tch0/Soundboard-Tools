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

from xml.dom import minidom

import os
import struct
import sys

if __name__ == '__main__':
    
    print 'SoundBoard Tool v' + VERSION + '\n'
    
    if len(sys.argv) != 2:
        print 'Usage: ./sbtool.py SOUNDBOARD_XML_FILE'
        print 'Example: ./sbtool.py info.xml'
        sys.exit(1)
        
    xml = None
        
    try:
        xml = minidom.parse(sys.argv[1])
    except IOError,e:
        print 'Error occurred during xml parsing: "' + str(e) + '"'
        sys.exit(1)
    
    sb = xml.getElementsByTagName('soundboard')[0]
    
    sb_name = sb.attributes['name'].value.encode('utf-8')
    sb_version = sb.attributes['version'].value.encode('utf-8')
    sb_author = sb.attributes['author'].value.encode('utf-8')
    sb_date = sb.attributes['date'].value.encode('utf-8')
    
    output_filename = sb_name.replace(' ','_')+'.sb'
    
    print 'Generating "' + output_filename + '"...'
    
    output = open(output_filename,'wb')
        
    output.write(struct.pack('<I',len(sb_name)))
    output.write(sb_name)
    output.write(struct.pack('<I',len(sb_version)))
    output.write(sb_version)
    output.write(struct.pack('<I',len(sb_author)))
    output.write(sb_author)
    output.write(struct.pack('<I',len(sb_date)))
    output.write(sb_date)
        
    icon = sb.getElementsByTagName('icon')[0].attributes['file'].value
    
    if not os.path.isfile(icon):
        print 'Missing icon file: "' + icon + '"!'
        output.close()
        sys.exit(2)
        
    icon_size = int(os.path.getsize(icon))
    
    print 'Embedding icon "' + icon + '" (size: ' + str(icon_size) + ' bytes)...'
    
    output.write(struct.pack('<I',icon_size))
    output.write(open(icon,'rb').read())
    
    clips = sb.getElementsByTagName('clips')[0].getElementsByTagName('clip')
    
    output.write(struct.pack('<I',len(clips)))
    
    #Let's handle duplicates
    for i in range(0,len(clips)):
        
        dup = 0;
        current_clip = clips[i].attributes['title'].value
        
        for j in range(i+1,len(clips)):
            
            counter_clip = clips[j].attributes['title'].value
            if counter_clip == current_clip:
                clips[j].attributes['title'] = current_clip + ' #' + str((dup+2))
                dup = dup + 1 
                
    for clip in clips:
        
        clip_title = clip.attributes['title'].value.encode('utf-8')
        clip_file = clip.attributes['file'].value
        
        if not os.path.isfile(clip_file):
            print 'Missing clip file: "' + clip_file + '"!'
            output.close()
            sys.exit(3)
        
        print 'Embedding clip "' + clip_title + '"...'
        
        output.write(struct.pack('<I',len(clip_title)))
        output.write(clip_title)
        
        clip_size = int(os.path.getsize(clip_file))
        
        output.write(struct.pack('<I',clip_size))
        output.write(open(clip_file,'rb').read())
    
    output.close()
