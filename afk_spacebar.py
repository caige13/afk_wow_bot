import time
import random

try:
    import pynput
    from pynput.keyboard import Key, Controller
except ImportError:
    print("pynput not installed. Run: pip install pynput")
    exit(1)

keyboard = Controller()

def press_spacebar():
    """Press spacebar with random 50-100ms hold duration."""
    hold_time = random.uniform(0.050, 0.100)  # 50-100ms
    keyboard.press(Key.space)
    time.sleep(hold_time)
    keyboard.release(Key.space)
    print(f"Pressed spacebar (held for {hold_time*1000:.0f}ms)")

def main():
    print("AFK Spacebar Bot started")
    print("Press Ctrl+C to stop")
    print("-" * 30)

    try:
        while True:
            # Wait 5-10 minutes (300-600 seconds)
            wait_time = random.uniform(300, 600)
            print(f"Next press in {wait_time/60:.1f} minutes...")
            time.sleep(wait_time)
            press_spacebar()
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()
