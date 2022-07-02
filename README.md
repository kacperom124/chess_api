Simple chess api. 
Return possible moves without other chessmans.


[GET] /api/v1/{chess-figure}/{current-field}

example for /pawn/a2

{"availableMoves": ["a4", "a3"], "error": null, "figure": "pawn", "currentField": "a2"}


[GET] /api/v1/{chess-figure}/{current-field}/{dest-field}

example for /pawn/a2/a3

{"move": "valid", "error": null, "figure": "pawn", "currentField": "a2", "destField": "a3"}

Htpp codes:

200 - Ok

409 - Field don't exist

404 - figure dont't exist

500 - server error

Launch:

First. Build docker with that commend.

docker-compose build

After this, you could run app with this command.

docker-compose up

