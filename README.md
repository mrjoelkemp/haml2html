HAML2HTML
===========

Created by: Joel Kemp, [@mrjoelkemp](https://twitter.com/#!/mrjoelkemp)

## Purpose

Converts the HAML files in the passed input directory into HTML files stored in the passed output directory.

## Dependencies

[HAML Gem](http://rubygems.org/gems/haml-rails): provides the HAML converter runtime.

## Usage	

`python haml2html.py [input_dir] [output_dir]`

* If no arguments are supplied, script parses the current directory.

### Output

Parsed files have the same filename as the original HAML files but with the .html extension.

## Notes

This was created to convert views within a Rails app to pure HTML for use in Adobe Edge. 

You can wrap the call to this script as a Rake task to automate view parsing:

	desc "Parse haml views"
	task :parse_haml do
	  print "\nCalling Python Haml Conversion Script\n"
	  system("python script/parsehaml.py")
	end
	
* This assumes that you've placed the script in `app/script` and want the parsed files in the current directory. Tweak the Rake task based on your needs.


**Happy coding!**