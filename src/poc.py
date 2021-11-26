# Proof of concept to check modules working and
# project setup correctly

import sys
from pyral import Rally, rallyWorkset

options = [opt for opt in sys.argv[1:] if opt.startswith('--')]
server, user, password, apikey, workspace, project = rallyWorkset(options)

print(" ".join('|%s|' % opt for opt in [server, user, password, apikey, workspace, project]))