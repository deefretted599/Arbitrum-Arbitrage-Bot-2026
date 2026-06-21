
import sys
import time
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from core.arbitrage_engine import ArbitrageEngine
from core.scanner import Scanner
from utils.logger import log_info, log_success
from utils.config_loader import load_config
from utils.hotkey_manager import HotkeyManager
from gui.console_renderer import ConsoleRenderer

def main():
    log_info("Arbitrum Arbitrage Bot v1.0 starting...")
    config = load_config("config.ini")
    engine = ArbitrageEngine(config)
    scanner = Scanner(config)
    hotkey_mgr = HotkeyManager()
    renderer = ConsoleRenderer()

    hotkey_mgr.register_hotkey('f1', lambda: renderer.toggle_menu())
    hotkey_mgr.register_hotkey('f2', lambda: engine.start())
    hotkey_mgr.register_hotkey('f3', lambda: engine.stop())
    hotkey_mgr.register_hotkey('f4', lambda: engine.manual_arbitrage())
    hotkey_mgr.register_hotkey('f5', lambda: engine.show_profit())
    hotkey_mgr.register_hotkey('f6', lambda: engine.toggle_alerts())
    hotkey_mgr.register_hotkey('f9', lambda: sys.exit(0))

    log_success("Bot ready. Press F1 for menu.")
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        log_info("Shutting down...")
        sys.exit(0)

if __name__ == "__main__":
    main()
