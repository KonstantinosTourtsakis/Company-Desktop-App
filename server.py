from vidstream import StreamingServer

receiver = StreamingServer('192.168.1.69', 9999)
receiver.start_server()

print("Server is running... ")
while input("") != "exit()":
    continue
receiver.stop_server()