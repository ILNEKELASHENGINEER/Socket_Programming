print("Selective Repeat Simulation\n")
window_size = int(input("Enter window size: "))

frame_count = 10  # Total number of frames
frames = list(range(frame_count))  # Simulated frames

print("\nSimulated Frames:")
print(*frames)

base = 0  # Base of the window
next_seq_num = 0  # Next sequence number
ack_received = [False] * frame_count  # Track acknowledgment status for each frame

while base < frame_count:
    for i in range(base, min(base + window_size, frame_count)):
        if not ack_received[i]:
            print(f"Sending Frame {frames[i]}")

    # Simulate the acknowledgment process for each frame individually
    for i in range(base, min(base + window_size, frame_count)):
        if not ack_received[i]:
            ack = int(input(f"Acknowledge Frame {frames[i]}? (1 for yes, 0 for no): "))
            if ack == 1:
                ack_received[i] = True

    # Move the window based on acknowledgments
    while base < frame_count and ack_received[base]:
        base += 1

    next_seq_num = base + window_size

print("\nAll frames have been sent and acknowledged.")
