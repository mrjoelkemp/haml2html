#!/bin/python3
# Author: 	Joel Kemp
# File:		haml2html.py
# Purpose:	Converts the haml files in the passed input directory into 
#			html files stored in the passed output directory.
# Notes:	Assumes that you have a HAML gem installed; necessary to use the haml converter program.
# Usage:	haml2html input_dir output_dir

import os
import subprocess
import sys			# For parsing command line arguments

def get_haml_filenames(dir):
# Purpose:	Finds the files in the passed dir containing a .HAML extension
# Precond: 	dir is a proper filepath
# Format:	app/views/foo/
# Returns:	A hash of filenames and filepaths for HAML files.
	filenames = []
	filepaths = []
	
	for dname, dirnames, fnames in os.walk(dir):		
		for filename in fnames:
			# If the filename doesn't contain haml, skip it
			if (".haml" in filename.lower()):
				filepath = os.path.join(dname, filename)
				filenames.append(filename)
				filepaths.append(filepath)
				print ("HAML:", filepath)
	
	# We should have the same amount of data for each list
	if len(filenames) != len(filepaths): raise AssertionError
	
	return {"filenames": filenames, "filepaths": filepaths}

def create_dir(dir):
# Purpose: 	Creates the directory from the passed path if the directory doesn't exist
# Precond: 	dir is a proper filepath
# Format:	app/views/foo/

	# If the directory doesn't exist
	if (not os.path.exists(dir)):	
		# Create it
		os.mkdir(dir)
		print(dir, "created!")

def haml2html(hamls, output_path):
# Purpose: 	Converts the passed HAML files into HTML files using the HAML parser
#			and stores the converted
# Notes: 	Makes a system call to use HAML's parser
# Command:	haml _path/input.haml _path/output.html
# Returns:	The number of HAML files converted
	
	filenames = hamls["filenames"]
	filepaths = hamls["filepaths"]
	
	output_file_ext = ".html"
	num_converted = 0
	
	for i in range(len(filepaths)):
		# filepaths contains the entire path + filename + extension for input file
		input = filepaths[i]
				
		input_name = filenames[i]
		
		# Keep the non-extension part of the filename
		input_name = input_name.split(".")[0]
		
		output = output_path + input_name + output_file_ext
		print(input, "to", output)
		
		# Parse the haml file
		# Syntax: haml _path/filename.haml _ouput_path/filename.html		
		command = ["haml", "--trace", input, output]
		
		# Execute the shell command
		p = subprocess.Popen(command)
		
		num_converted += 1
	
	return num_converted
	
def main():
	args = sys.argv
	
	input_arg_index = 1
	output_arg_index = 2
	num_args = len(args)
	
	# If the user doesn't supply arguments, assume the current directory
	input_dir = "." if (num_args == 0) else args[1]
	output_dir = "." if (num_args == 1) else args[2]
		
	print("Locating HAML files in", input_dir)
	hamls = get_haml_filenames(input_dir)
	
	print("Making sure", output_dir, "exists")
	create_dir(output_dir)
	
	print ("Converting HAML files from", input_dir, "to HTML files in", output_dir)
	num_converted = haml2html(hamls, output_dir)
	
	file_plural = "file" if num_converted == 1 else "files"
	print(num_converted, "HAML " + file_plural +" converted!")
	
main()