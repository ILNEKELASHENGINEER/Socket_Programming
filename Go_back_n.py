import time
print("Go-Back-N Simulation\n")
window_size = int(input("Enter window size: "))
frame_count = 10  # Total number of frames
frames = list(range(frame_count))# Simulated frames
print(frames)
print("\nSimulated Frames:")
print(*frames)
base = 0  # Base of the window
next_seq_num = 0  # Next sequence number
timeout = 3.0  # Timeout in seconds (adjust as needed)
while base < frame_count:
    for i in range(base, min(base + window_size, frame_count)):
        print(f"Sending frame {frames[i]}")

    # Simulate the acknowledgment process for the oldest frame in the window
    ack = int(input(f"Acknowledge frame {frames[base]}? (1 for yes, 0 for no): "))
    
    if ack == 1:
        base += 1
        next_seq_num += 1
    else:
        print(f"Timeout! Retransmitting frames from {base} to {base + window_size - 1}")
        next_seq_num = base

    time.sleep(timeout)

print("\nAll frames have been sent and acknowledged.")
