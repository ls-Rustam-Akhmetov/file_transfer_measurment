class ServerAccess:
    def __init__(self, hostname: str, login: str, password: str, src_file_path: str, dst_file_path: str):
        self.hostname: str = hostname
        self.login: str = login
        self.password: str = password
        self.src_file_path: str = src_file_path
        self.dst_file_path: str = dst_file_path
