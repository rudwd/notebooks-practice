def get_version(version_file_name: str = "notebook/__init__.py") -> str:
    """
    Gets the version string from a file.
    :param version_file_name: File name containing the version info.
    :return: Version string
    :param version_file_name:
    :return:
    """
    with open(version_file_name, 'r') as f:
        version_file = f.read()
        # TODO: a quick hack. use a regex to verify the format. write a test for it.
        version = version_file.split('=')[1].strip().replace("'", "")
    return version
