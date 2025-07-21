"""
Text Adventure Game - Petualangan di Hutan Mistis
Game petualangan berbasis teks dengan sistem inventory dan battle
"""

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = ["pedang kayu", "ramuan kesehatan"]
        self.location = "hutan_pintu_masuk"
        
    def show_status(self):
        print(f"\n=== STATUS {self.name.upper()} ===")
        print(f"❤️  Kesehatan: {self.health}/100")
        print(f"🎒 Inventory: {', '.join(self.inventory)}")
        print("=" * 30)

class Game:
    def __init__(self):
        self.locations = {
            "hutan_pintu_masuk": {
                "description": "🌲 Anda berada di pintu masuk hutan yang gelap dan misterius.",
                "exits": {"utara": "hutan_tengah", "timur": "danau"},
                "items": ["tongkat sihir"],
                "enemy": None
            },
            "hutan_tengah": {
                "description": "🕷️ Di tengah hutan, Anda melihat jaring laba-laba raksasa.",
                "exits": {"selatan": "hutan_pintu_masuk", "utara": "goa"},
                "items": [],
                "enemy": "laba-laba raksasa"
            },
            "danau": {
                "description": "🏞️ Danau yang jernih dengan ikan-ikan emas berenang.",
                "exits": {"barat": "hutan_pintu_masuk"},
                "items": ["ikan emas", "kristal biru"],
                "enemy": None
            },
            "goa": {
                "description": "⚡ Goa gelap dengan suara aneh dari dalam.",
                "exits": {"selatan": "hutan_tengah"},
                "items": ["harta karun"],
                "enemy": "naga kecil"
            }
        }
        
    def start_game(self):
        print("🎮 SELAMAT DATANG DI PETUALANGAN HUTAN MISTIS 🎮")
        print("=" * 50)
        name = input("Masukkan nama petualang Anda: ")
        self.player = Player(name)
        
        print(f"\nSelamat datang, {name}! Petualangan Anda dimulai...")
        time.sleep(1)
        
        while self.player.health > 0:
            self.show_current_location()
            self.player.show_status()
            self.handle_input()
            
        print(f"💀 {self.player.name} telah gugur dalam petualangan...")
        
    def show_current_location(self):
        location = self.locations[self.player.location]
        print(f"\n📍 LOKASI: {self.player.location.replace('_', ' ').title()}")
        print(location["description"])
        
        if location["items"]:
            print(f"🎁 Item tersedia: {', '.join(location['items'])}")
            
        if location["enemy"]:
            print(f"⚔️  BAHAYA! {location['enemy']} menghadang!")
            
        exits = ", ".join(location["exits"].keys())
        print(f"🚪 Keluar: {exits}")
        
    def handle_input(self):
        command = input("\n> Apa yang ingin Anda lakukan? ").lower().strip()
        
        if command in ["keluar", "quit", "exit"]:
            print("Terima kasih telah bermain!")
            exit()
        elif command.startswith("pergi "):
            direction = command.split()[1]
            self.move_player(direction)
        elif command.startswith("ambil "):
            item = command.replace("ambil ", "")
            self.take_item(item)
        elif command == "serang":
            self.battle()
        elif command == "inventory":
            print(f"🎒 Inventory: {', '.join(self.player.inventory)}")
        elif command == "help":
            self.show_help()
        else:
            print("❌ Perintah tidak dikenali. Ketik 'help' untuk bantuan.")
            
    def move_player(self, direction):
        current_location = self.locations[self.player.location]
        if direction in current_location["exits"]:
            self.player.location = current_location["exits"][direction]
            print(f"🚶 Anda bergerak ke {direction}...")
            time.sleep(1)
        else:
            print("❌ Anda tidak bisa pergi ke arah itu!")
            
    def take_item(self, item):
        location = self.locations[self.player.location]
        if item in location["items"]:
            self.player.inventory.append(item)
            location["items"].remove(item)
            print(f"✅ Anda mengambil {item}!")
        else:
            print("❌ Item tidak ditemukan di sini!")
            
    def battle(self):
        location = self.locations[self.player.location]
        if not location["enemy"]:
            print("❌ Tidak ada musuh di sini!")
            return
            
        enemy = location["enemy"]
        enemy_health = random.randint(30, 60)
        
        print(f"\n⚔️  PERTARUNGAN dengan {enemy}!")
        
        while enemy_health > 0 and self.player.health > 0:
            # Player attack
            damage = random.randint(15, 25)
            enemy_health -= damage
            print(f"💥 Anda menyerang {enemy} untuk {damage} damage!")
            
            if enemy_health <= 0:
                print(f"🏆 Anda mengalahkan {enemy}!")
                location["enemy"] = None
                reward = random.choice(["pedang baja", "ramuan kekuatan", "emas"])
                self.player.inventory.append(reward)
                print(f"🎁 Anda mendapat {reward}!")
                break
                
            # Enemy attack
            enemy_damage = random.randint(10, 20)
            self.player.health -= enemy_damage
            print(f"💢 {enemy} menyerang Anda untuk {enemy_damage} damage!")
            
            time.sleep(1)
            
    def show_help(self):
        print("\n📚 BANTUAN:")
        print("- pergi [arah]: bergerak ke arah (utara/selatan/timur/barat)")
        print("- ambil [item]: mengambil item")
        print("- serang: menyerang musuh")
        print("- inventory: lihat barang yang dimiliki")
        print("- help: tampilkan bantuan")
        print("- keluar: keluar dari game")

def main():
    game = Game()
    game.start_game()

if __name__ == "__main__":
    main()
