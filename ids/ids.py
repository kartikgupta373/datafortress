from datafortress.forms import VideoForm


def ids():
    form = VideoForm()
    cols ="""duration, 
    protocol_type, 
    service, 
    flag, 
    src_bytes, 
    dst_bytes, 
    land, 
    wrong_fragment, 
    urgent, 
    hot, 
    num_failed_logins, 
    logged_in, 
    num_compromised, 
    root_shell, 
    su_attempted, 
    num_root, 
    num_file_creations, 
    num_shells, 
    num_access_files, 
    num_outbound_cmds, 
    is_host_login, 
    is_guest_login, 
    count, 
    srv_count, 
    serror_rate, 
    srv_serror_rate, 
    rerror_rate, 
    srv_rerror_rate, 
    same_srv_rate, 
    diff_srv_rate, 
    srv_diff_host_rate, 
    dst_host_count, 
    dst_host_srv_count, 
    dst_host_same_srv_rate, 
    dst_host_diff_srv_rate, 
    dst_host_same_src_port_rate, 
    dst_host_srv_diff_host_rate, 
    dst_host_serror_rate, 
    dst_host_srv_serror_rate, 
    dst_host_rerror_rate, 
    dst_host_srv_rerror_rate"""

    columns =[] 
    for c in cols.split(', '): 
        if(c.strip()): 
            columns.append(c.strip()) 
    columns.append('target') 

    
    attacks_types = { 
        'normal': 'normal', 
    'back': 'dos', 
    'buffer_overflow': 'u2r', 
    'ftp_write': 'r2l', 
    'guess_passwd': 'r2l', 
    'imap': 'r2l', 
    'ipsweep': 'probe', 
    'land': 'dos', 
    'loadmodule': 'u2r', 
    'multihop': 'r2l', 
    'neptune': 'dos', 
    'nmap': 'probe', 
    'perl': 'u2r', 
    'phf': 'r2l', 
    'pod': 'dos', 
    'portsweep': 'probe', 
    'rootkit': 'u2r', 
    'satan': 'probe', 
    'smurf': 'dos', 
    'spy': 'r2l', 
    'teardrop': 'dos', 
    'warezclient': 'r2l', 
    'warezmaster': 'r2l', 
    } 

    # reading features list 
    with open("C:\Users\MSI1\Documents\python project\django\df\major\ids\hard_signatures", 'r') as f: 
        print(f.read())
        signatures = VideoForm.video()
        attacks_types = subprocess.run(["C:\Program Files\ClamAV\clamdscan.exe", "-i", filepath], capture_output=True, text=True)
         
                    

