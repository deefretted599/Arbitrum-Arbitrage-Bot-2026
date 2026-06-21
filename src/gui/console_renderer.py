
from utils.logger import log_info

class ConsoleRenderer:
    def __init__(self):
        self.menu_visible = False

    def toggle_menu(self):
        self.menu_visible = not self.menu_visible
        if self.menu_visible:
            self.show_menu()
        else:
            log_info("Menu hidden")

    def show_menu(self):
        print("╔══════════════════════════════════════════════════════════╗")
        print("║   ARBITRUM ARBITRAGE BOT v1.0                          ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║  F2 - Start Scanning                                    ║")
        print("║  F3 - Stop All                                          ║")
        print("║  F4 - Manual Arbitrage                                  ║")
        print("║  F5 - Show Profit (P&L)                                 ║")
        print("║  F6 - Toggle Telegram Alerts                            ║")
        print("║  F9 - Exit                                              ║")
        print("╚══════════════════════════════════════════════════════════╝")
