
from utils.logger import log_info

class Scanner:
    def __init__(self, config):
        self.config = config
        self.pairs = [
            ("WETH", "USDC"),
            ("WETH", "USDT"),
            ("ARB", "USDC"),
            ("ARB", "USDT"),
            ("GMX", "USDC"),
            ("GMX", "USDT"),
            ("MAGIC", "USDC"),
            ("MAGIC", "USDT"),
        ]

    def scan(self):
        log_info(f"Scanning {len(self.pairs)} trading pairs...")
        # Simulate price data
        return {}
