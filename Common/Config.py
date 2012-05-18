#Tophat config files

import imp
from os import name
from sys import exit

def loadConfig(path):
		"""
			Arguments:
					path	--	String

			Returning:
					Config object.
			
			Exceptions:
					Generic python Exception if error is found.
	
			Description:
					loadConfig takes in a string and attempts to import the file at that location 
					in the file system if it fails it will throw an exception and quit. It will 
					otherwise return an	object with the required config keys. If not all the keys 
					are there or there is errors in the syntax of the config it will throw an 
					exception and shutdown TopHat.
		"""
		
		if type(path) is not str:
				raise Exception('path is not a string, gtfo')
			
		try:
				module=imp.load_source('TopHatConfig', path)
		except IOError as detail:
				raise Exception('Could not open %s: %s' % (path, detail))

		except NameError as detail:
				raise Exception('Extraneous key found in %s: %s' %(path, detail))
				exit(1)
		except SyntaxError as detail:
				raise Exception('Bad Syntax in %s: %s' % (path, detail))
		
		if not hasattr(module, 'TopHatConfig'):
				raise Exception('No TopHatConfig Function found in %s.\nPlease read our wiki: http://wiki.tophat.ie' % path)
				exit(1)
		conf=module.TopHatConfig()
		if not hasattr(conf, 'SSLKeyPath'):
				raise Exception('Please specify where the SSL Key is located:\nSSLKeyPath = \'/path/to/key\'')
				exit(1)
		if not hasattr(conf, 'SSLCertPath'):
				raise Exception('Please specify where the SSL Cert is located:\nSSLCertPath = \'/path/to/cert\'')
				exit(1)
		if not hasattr(conf, 'Port'):
				raise Exception('Please specify what port TopHat is to listen to:\nPort=443')
				exit(1)
		if not hasattr(conf, 'Interface'):
				raise Exception('Please specify what address to listen on, 0.0.0.0 for all addresses:\nInterface=\'0.0.0.0\'')
				exit(1)
		
		if not hasattr(conf, 'User'):
				raise Exception('Please specify what user TopHat drops privileges to:\nUser = \'username\'')
				exit(1)
		
		if not hasattr(conf, 'Group'):
				raise Exception('Please specify what group TopHat drops privileges to:\nGroup = \'groupname\'')
				exit(1)
		if not hasattr(conf, 'LogFile'):
				raise Exception('Please specify where TopHat will log to:\nLogFile = \'/path/to/logfile\'')
				exit(1)