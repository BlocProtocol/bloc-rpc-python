# This script is for debugging/development
# It initializes WalletD and BLOCD with debug logging enabled

import logging

from bloc import Walletd, BLOCd

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

wallet = Walletd(password='test')
#daemon = BLOCd()
import ipdb; ipdb.set_trace()

#wallet.get_balance()
