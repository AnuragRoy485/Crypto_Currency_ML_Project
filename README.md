# Crypto_Currency_ML_Project
This Tool Classifies Different Wallet Address Types Like BTC, Ethereum and Etc.

# ETHEREUM DEMO IMAGE
![WhatsApp Image 2024-05-23 at 19 53 31_73c0e8b5](https://github.com/AnuragRoy485/Crypto_Currency_ML_Project/assets/76765293/9ed2a117-c7ea-456a-92df-675aff2dbad1)

# How to run the application
 1: Open the project in vs code.
 2: run “pip install-r requirements.txt”
 3: and then run the model.py file from the run button.
 ![image](https://github.com/AnuragRoy485/Crypto_Currency_ML_Project/assets/76765293/c8926176-45ba-4eb6-9ee3-b3f8c62e575e)

# Limitations:
 Due to hidden services and hidden cryptocurrencies the dataset is not yet fully trained to
 identify any type of cryptos out there because resources from the web are limited and
 changes from time to time
 Used dataset
 [
 {
 },
 {
 },
 {
 },
 {
 "name": "Bitcoin",
 "symbol": "BTC",
 "patterns": ["^1", "^3", "^bc1"]
 "name": "Ethereum",
 "symbol": "ETH",
 "patterns": ["^0x"]
 "name": "BNB",
 "symbol": "BNB",
 "patterns": ["^bnb"]
 "name": "Solana",
    "symbol": "SOL",
    "patterns": ["^[1-9A-HJ-NP-Za-km-z]{32,44}$"]
  },
  {
    "name": "XRP",
    "symbol": "XRP",
    "patterns": ["^r"]
  },
  {
    "name": "Dogecoin",
    "symbol": "DOGE",
    "patterns": ["^D"]
  },
  {
    "name": "Toncoin",
    "symbol": "TON",
    "patterns": ["^EQ"]
  },
  {
    "name": "Cardano",
    "symbol": "ADA",
    "patterns": ["^addr1"]
  },
  {
    "name": "Avalanche",
    "symbol": "AVAX",
    "patterns": ["^X-", "^C-", "^P-"]
  },
  {
    "name": "Polkadot",
    "symbol": "DOT",
    "patterns": ["^1", "^1[3-9A-HJ-NP-Za-km-z]{46}$"]
  },
  {
    "name": "TRON",
    "symbol": "TRX",
    "patterns": ["^T"]
  },
  {
    "name": "Bitcoin Cash",
    "symbol": "BCH",
    "patterns": ["^q", "^p", "^bitcoincash:q"]
  },
  {
    "name": "NEAR Protocol",
    "symbol": "NEAR",
    "patterns": ["^[a-z0-9-_]{2,64}$"]
  },
  {
    "name": "Litecoin",
    "symbol": "LTC",
    "patterns": ["^L", "^M", "^ltc1"]
  },
  {
    "name": "Internet Computer",
    "symbol": "ICP",
    "patterns": ["^[a-z2-7]{11}(-[a-z2-7]{5}){4}-[a-z2-7]{6}$"]
  },
  {
    "name": "Filecoin",
    "symbol": "FIL",
    "patterns": ["^f1", "^f3"]
  },
  {
    "name": "Kaspa",
    "symbol": "KAS",
    "patterns": ["^kaspa"]
  },
  {
    "name": "Cosmos",
    "symbol": "ATOM",
    "patterns": ["^cosmos"]
  },
  {
    "name": "Stellar",
    "symbol": "XLM",
    "patterns": ["^G"]
  },
  {
    "name": "Stacks",
    "symbol": "STX",
    "patterns": ["^SP", "^SM"]
  },
  {
    "name": "Arweave",
    "symbol": "AR",
    "patterns": ["^[a-z0-9_-]{43}$"]
  },
  {
    "name": "Monero",
    "symbol": "XMR",
    "patterns": ["^4", "^8"]
  },
  {
    "name": "Bonk",
    "symbol": "BONK",
    "patterns": ["^[1-9A-HJ-NP-Za-km-z]{32,44}$"]
  },
  {
    "name": "THORChain",
    "symbol": "RUNE",
    "patterns": ["^thor"]
  },
  {
    "name": "Sei",
    "symbol": "SEI",
    "patterns": ["^[a-z0-9]{1,}$"]
  },
  {
    "name": "Algorand",
    "symbol": "ALGO",
    "patterns": ["^A"]
  },
  {
    "name": "Beam",
    "symbol": "BEAM",
    "patterns": ["^bm"]
  },
  {
    "name": "Akash Network",
    "symbol": "AKT",
    "patterns": ["^akash"]
  },
  {
    "name": "Bitcoin SV",
    "symbol": "BSV",
    "patterns": ["^1", "^3", "^bc1"]
  },
  {
    "name": "BitTorrent (New)",
    "symbol": "BTT",
    "patterns": ["^T"]
  },
  {
    "name": "Neo",
    "symbol": "NEO",
    "patterns": ["^A"]
  },
  {
    "name": "MultiversX",
    "symbol": "EGLD",
    "patterns": ["^erd"]
  },
  {
    "name": "Ronin",
    "symbol": "RON",
    "patterns": ["^ronin:"]
  },
  {
    "name": "eCash",
    "symbol": "XEC",
    "patterns": ["^q", "^p"]
  },
  {
    "name": "Tezos",
    "symbol": "XTZ",
    "patterns": ["^tz"]
  },
  {
    "name": "Conflux",
    "symbol": "CFX",
    "patterns": ["^cfx:"]
  },
  {
    "name": "Mina",
    "symbol": "MINA",
    "patterns": ["^[a-km-zA-HJ-NP-Z0-9]{35}$"]
  },
  {
    "name": "ORDI",
    "symbol": "ORDI",
    "patterns": ["^bc1"]
  },
  {
    "name": "IOTA",
    "symbol": "IOTA",
    "patterns": ["^iota1"]
  },
  {
    "name": "Helium",
    "symbol": "HNT",
    "patterns": ["^13"]
  },
  {
    "name": "Dash",
    "symbol": "DASH",
    "patterns": ["^X"]
  },
  {
    "name": "NEM",
    "symbol": "XEM",
    "patterns": ["^N"]
  },
  {
    "name": "Decred",
    "symbol": "DCR",
    "patterns": ["^D"]
  },
  {
    "name": "Gas",
"symbol": "GAS",
 "patterns": ["^A"]
 },
 {
 },
 {
 }
 ]
 "name": "Chia",
 "symbol": "XCH",
 "patterns": ["^xch"]
 "name": "Harmony",
 "symbol": "ONE",
 "patterns": ["^one1"
