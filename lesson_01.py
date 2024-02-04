from utils.get_web3 import init_web3, logger
from utils.network_endpoints import endpoints


def inquiry_account_balance(wallet_address=None):
    if not all([wallet_address]):
        logger.error('参数不足')
        return

    status = web3.is_connected()
    if status:
        block_number = web3.eth.block_number
        wallet_address = web3.to_checksum_address(wallet_address)

        # 账户余额(wei)
        balance = web3.eth.get_balance(wallet_address)
        # 账户余额(币种token)
        token = web3.from_wei(balance, 'ether')
        logger.info(' | '.join((str(item) for item in
                                ['区块高度'.center(6), '钱包地址'.center(39), '余额(wei)'.center(17),
                                 '余额(token)'.center(8)])))
        logger.info(
            ' | '.join(
                ([str(block_number).center(6), wallet_address, str(balance).center(9), str(token).center(11)])))

    else:
        logger.error('infura出错啦,请校验是否正常...')


if __name__ == '__main__':
    # net_name = 'eth'
    net_names = endpoints.keys()
    for net_name in net_names:
        web3 = init_web3(net_name=net_name, proxies=True)
        wallet_address = "0x96bceeF977b08D2895e52D7848aa874Fa9F29450"
        inquiry_account_balance(wallet_address=wallet_address)
