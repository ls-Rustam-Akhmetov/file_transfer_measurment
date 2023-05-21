import os

import paramiko
from scp import SCPClient

from model import ServerAccess


def paramiko_sftp_send_file(server: ServerAccess):
    ssh = paramiko.SSHClient()
    # paramiko.util.log_to_file('log/paramiko.log')
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))

    try:
        ssh.connect(server.hostname, username=server.login, password=server.password, compress=True)
        sftp = ssh.open_sftp()
        sftp.put(server.src_file_path, server.dst_file_path)
        sftp.close()

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check the credentials.")
    except paramiko.SSHException as e:
        print(f"SSH connection failed: {str(e)}")
    finally:
        # Close the SSH connection
        ssh.close()


def paramiko_sftp_remove_remote_file(server: ServerAccess):
    # Create an SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the remote server
        client.connect(server.hostname, username=server.login, password=server.password)

        # Remove the file
        sftp = client.open_sftp()
        sftp.remove(server.dst_file_path)
        sftp.close()

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check the credentials.")
    except paramiko.SSHException as e:
        print(f"SSH connection failed: {str(e)}")
    finally:
        # Close the SSH connection
        client.close()


def paramiko_scp_send_file(server: ServerAccess):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(server.hostname, username=server.login, password=server.password, compress=True)

        with SCPClient(ssh.get_transport()) as scp:
            scp.put(server.src_file_path, server.dst_file_path)

        print("File sent successfully.")
    except paramiko.AuthenticationException:
        print("Authentication failed. Please check the credentials.")
    except paramiko.SSHException as e:
        print(f"SSH connection failed: {str(e)}")
    finally:
        ssh.close()
