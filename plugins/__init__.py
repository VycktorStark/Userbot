__all__ = ['plugins_']
def values_plugin(path):
	import os, re, time
	pluginsFile = []
	curPath = os.path.dirname(os.path.realpath(__file__))
	_path = "/{}/".format(path)
	path_ = "/{}".format(path)
	updateTime = time.strftime('    - Date: %d/%m \n    - Time: %H:%M:%S', time.localtime(os.path.getatime((curPath + _path))))
	Files = [curPath + _path + f for f in os.listdir(curPath + path_) if re.search('^.+\.py$', f)]
	for files in Files:
		values = {}
		with open(files, encoding='utf-8') as file:
			code = compile(file.read(), files, 'exec')
			exec(code, values)
			pluginsFile.append(values['plugin'])
	return pluginsFile, updateTime
def plugins_():
		global plugins, group, private, alluser, sudo
		plugins = []
		group, update_group = values_plugin('group')
		plugins += group
		private, update_private = values_plugin('private')
		plugins += private
		sudo, update_sudo = values_plugin('sudo')
		plugins += sudo
		alluser, update_alluser = values_plugin('alluser')
		plugins += alluser
		return plugins
