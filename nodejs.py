import pkg_resources

class Buildpack():
	def detect(self, files, **kwargs):
		return 'package.json' in files

	def get_build_context_path(self):
		return pkg_resources.resource_filename(__name__, 'build-context')