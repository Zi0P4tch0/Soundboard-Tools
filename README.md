#License

	This file is part of Soundboard.

	Soundboard is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	any later version.

	Soundboard is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with Soundboard.  If not, see <http://www.gnu.org/licenses/>.
	

#Soundboard-Tools

These tools are written in Python.
I use them to generate the soundboard file.

###sbtool

"sbtool" reads the soundboard details from a XML file, with this format, and generates a soundboard (.sb) file.

	<soundboard name="Test Soundboard" version="1.0" author="Zi0P4tch0" date="24/7/2013">
		<icon file="icon.png"/>
		<clips>
			<clip title="Example Clip #1" file="1.mp3"/>
			<clip title="Example Clip #2" file="2.mp3"/>
			<!-- other clips here -->
		</clips>
	</soundboard>

###sbtest

"sbtest" checks the soundboard and prints all details on the screen.