#
import os
import ProxyCloud

BOT_TOKEN = 'xxxx' #Aqui va el token del bot
API_ID =  'xxxxxxx' #Tu api id de telegram
API_HASH = 'xxxxxx' #Tu api id de telegram
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','xxxxx').split(';')

static_proxy = 'socks5h://KHGDJEYGJGLHFEYDKDKECDYKGJCERKCJLJGJLH'
PROXY = ProxyCloud.parse(static_proxy)

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
  
#Lo siguiente son las tablas de la base de datos de usarios, 
#es obligatorio agregar a aquellos usarios estaticos puestos en el main.py
#los agregados mediante /add no es necesario
#ponerlos valor 0 siempre

space = {}
space['xxxxx'] = 0

