infura_api_key = 'a9d6b1764a464faaa8f0399958601361'
endpoints_net = {
    'eth': 'https://mainnet.infura.io/v3/',
    'avalanche': 'https://avalanche-mainnet.infura.io/v3/',
    'arbitrum': 'https://arbitrum-mainnet.infura.io/v3/',
    'celo': 'https://celo-mainnet.infura.io/v3/',
    'goerli': 'https://goerli.infura.io/v3/',
    'sepolia': 'https://sepolia.infura.io/v3/',
    'linea': 'https://linea-mainnet.infura.io/v3/',
    'optimism': 'https://optimism-mainnet.infura.io/v3/',
    'palm': 'https://palm-mainnet.infura.io/v3/',
    'polygon': 'https://polygon-mainnet.infura.io/v3/',
    'bnb': 'https://bsc-dataseed.binance.org/',
    'metis': 'https://stardust.metis.io/',
}

endpoints = {}

for endpoint_net_name, endpoint_net_value in endpoints_net.items():
    if endpoint_net_name == 'bnb' or endpoint_net_name == 'optimism':
        endpoints[endpoint_net_name] = endpoint_net_value
    else:
        endpoints[endpoint_net_name] = endpoint_net_value + infura_api_key

if __name__ == '__main__':
    print(endpoints)

