from hashlib import sha1

class Generator(object):
    def generate_version(self, key, url, content):
        return sha1(content).hexdigest()

    def get_output(self):
        """
        Generates content for production mode.

        Yields tuples of the form:
        key, url, content

        Here, key must be the same as for get_dev_output_names().
        """
        for key, url, hash in self.get_dev_output_names():
            yield key, url, self.get_dev_output(url)[0]

    def get_dev_output(self, name):
        """
        Generates content for dev mode.

        Yields tuples of the form:
        content, mimetype
        """
        raise NotImplementedError()

    def get_dev_output_names(self):
        """
        Generates file names for dev mode.

        Yields tuples of the form:
        key, url, version_hash

        Here, key must be the same as for get_output_names().
        """
        raise NotImplementedError()
