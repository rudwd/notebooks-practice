def get_version(version_file_name: str = "notebook/__init__.py") -> str:
    with open(version_file_name, 'r') as f:
        version_file = f.read()
        # TODO: a quick hack. use a regex to verify the format. write a test for it.
        version = version_file.split('=')[1].strip().replace("'", "")
    return version
