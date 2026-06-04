"""
HOKAL Configuration File
ملف إعدادات HOKAL
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# Telegram Bot Configuration
# ==========================================
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")
TELEGRAM_ADMIN_ID = os.getenv("TELEGRAM_ADMIN_ID", "YOUR_ADMIN_ID")

# ==========================================
# Blockchain Configuration
# ==========================================
BLOCKCHAIN_RPCS = {
    "ethereum": os.getenv("ETH_RPC", "https://eth.llamarpc.com"),
    "polygon": os.getenv("POLYGON_RPC", "https://polygon-rpc.com"),
    "solana": os.getenv("SOLANA_RPC", "https://api.mainnet-beta.solana.com"),
    "bsc": os.getenv("BSC_RPC", "https://bsc-dataseed1.bnbchain.org:8545"),
    "arbitrum": os.getenv("ARB_RPC", "https://arb1.arbitrum.io/rpc"),
}

# ==========================================
# API Keys
# ==========================================
API_KEYS = {
    "etherscan": os.getenv("ETHERSCAN_API_KEY", ""),
    "polygonscan": os.getenv("POLYGONSCAN_API_KEY", ""),
    "bscscan": os.getenv("BSCSCAN_API_KEY", ""),
}

# ==========================================
# Database Configuration
# ==========================================
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///hokal.db")
DATABASE_POOL_SIZE = 10

# ==========================================
# Security Settings
# ==========================================
MAX_CONTRACT_SIZE = 50000  # bytes
TIMEOUT = 30  # seconds
RATE_LIMIT = 10  # requests per minute
ENABLE_SSL = True

# ==========================================
# Report Settings
# ==========================================
REPORT_FORMAT = "html"  # html, pdf, json
SAVE_REPORTS = True
REPORT_RETENTION_DAYS = 90

# ==========================================
# Logging Configuration
# ==========================================
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_FILE = "hokal.log"
LOG_MAX_SIZE = 10 * 1024 * 1024  # 10 MB

# ==========================================
# Wallet Configuration (Token Minter)
# ==========================================
PRIVATE_KEY = os.getenv("WALLET_PRIVATE_KEY", "")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS", "")

# ==========================================
# Email Configuration (for reports)
# ==========================================
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = 587
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")

# ==========================================
# Feature Flags
# ==========================================
ENABLE_AUDITOR = True
ENABLE_MINTER = True
ENABLE_ANALYTICS = True
ENABLE_NOTIFICATIONS = True

# ==========================================
# Advanced Settings
# ==========================================
DEBUG_MODE = os.getenv("DEBUG_MODE", "False") == "True"
VERBOSE_LOGGING = False
PERFORMANCE_MONITORING = True