package org.example;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class serverHandler {
    private final ServerSocket serverSocket;

    public static int port = 5000;
    public serverHandler(ServerSocket serverSocket) {
        this.serverSocket = serverSocket;
    }


    public void startServers() {

        try {
            while (!serverSocket.isClosed()) {

                Socket socket = serverSocket.accept();
                System.out.println("A new client has connected!");
                Runnable server = new server(socket);
                Thread task = new Thread(server);
                task.start();
            }
        } catch (IOException e){
        closeServeSocket();
        }
    }
    public void closeServeSocket () {
        try {
            if (serverSocket != null) {
                serverSocket.close();
            }
        } catch (IOException e) {
            System.out.println(" ");
        }
    }

    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket= new ServerSocket(port);
        serverHandler serverHandler = new serverHandler(serverSocket);
        System.out.println("Server running waiting for clients to connect...");

        serverHandler.startServers();
    }
}

