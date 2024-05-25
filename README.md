# RockPaperScissors

## Description
This is a simple client-server application that allows two clients to play a game of Rock-Paper-Scissors against each other. The server handles game logic and maintains the scores until one player wins the match.

## Features
Concurrent Client Handling: Handles multiple clients and pairs them for a game.

Game Logic: Implements the rules of Rock-Paper-Scissors.

Score Management: Tracks and updates scores until a player wins the match.

## RockPaperScissors Client
Connection Setup:

Connects to the server using IP 127.0.0.1 and port 5000.

Game Interaction:

Receives messages from the server and follows prompts to enter moves.
Continuously updates the score and displays the current game status.
Ends the game when a player wins 3 rounds.
## Rock-Paper-Scissors Server
Connection Management:

Listens for incoming client connections on IP 127.0.0.1 and port 5000.

Handles new client connections and pairs clients for a game.

Game Logic:

Implements the rules of Rock-Paper-Scissors.

Tracks and updates scores for each player.

Manages the game state and communicates results to clients.
## SocketWrapper Class
A utility class to manage socket communication, ensuring messages are correctly sent and received with a delimiter for message separation.
