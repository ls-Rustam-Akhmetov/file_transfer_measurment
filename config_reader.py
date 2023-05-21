import configparser

from model import ServerAccess


def get_test_config() -> ServerAccess:
    config = configparser.ConfigParser()
    config.read('server_props.ini')
    host = config['server']['hostname']
    login = config['server']['login']
    password = config['server']['password']
    src_file_path = config['server']['src_file_path']
    dst_file_path = config['server']['dst_file_path']
    return ServerAccess(host, login, password, src_file_path, dst_file_path)
