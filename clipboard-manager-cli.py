import pyperclip

class ClipboardManager:
    def __init__(self):
        self.history = []
        self.current_value = None

    def get_clipboard(self):
        value = pyperclip.paste()
        if value != self.current_value:
            self.history.append(value)
            self.current_value = value
        return value
    
    def show_history(self):
        if self.history:
            for idx, value in enumerate(self.history, start=1):
                print(f"{idx}: {value}")
        else:
            print("No history available.")

    def clear_clipboard(self):
        pyperclip.copy('')
        self.current_value = ''
        print("Clipboard cleared.")

if __name__ == "__main__":
    manager = ClipboardManager()

    while True:
        print("\nMenu:")
        print("1. Get current clipboard value")
        print("2. Show clipboard history")
        print("3. Clear clipboard")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            current_value = manager.get_clipboard()
            print(f"Current clipboard value: {current_value}")
        
        elif choice == '2':
            manager.show_history()
        
        elif choice == '3':
            manager.clear_clipboard()
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
