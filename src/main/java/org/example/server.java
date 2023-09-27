package org.example;

import java.io.*;
import java.net.Socket;

public class server implements Runnable{
    private Socket socket;
    private BufferedReader bufferedReader;
    private BufferedWriter bufferedWriter;
    public static String commandFromClient;



    public server(Socket socket){
    try {
        this.socket = socket;
        this.bufferedWriter = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
        this.bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));

    } catch (IOException e) {
        closeProgram(socket, bufferedReader, bufferedWriter);
        }
    }

    public void run() {
        while (socket.isConnected()) {
            try {
                commandFromClient = bufferedReader.readLine();
            }catch (IOException e) {
                System.out.println("Unable to send message");
            }
        }
    }

    public void closeProgram(Socket socket, BufferedReader bufferedReader, BufferedWriter bufferedWriter) {
        try {
            if (bufferedReader != null) {
                bufferedReader.close();
            }
            if (bufferedWriter != null) {
                bufferedWriter.close();
            }
            if (socket != null) {
                socket.close();
            }
        } catch (IOException e) {
            System.out.println("Unable to close the program ");
        }

    }
}
