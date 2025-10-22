# ServerChatFM
Codice in python che assume il ruolo di server WebServer. 
Tramite un protocollo predefinito vengono scambiati i messaggi che interpretati dal server viene restituito un valore che dipende dal contenuto della richiesta.

per attivare l'ambiente virtuale si usa:
`source venv/bin/activate` 

per eseguire il "client" esegui nel terminale, dopo aver eseguito il comando precedente, il seguente:
`python -m websockets ws://10.3.2.128:8765` 