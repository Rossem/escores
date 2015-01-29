var id_count = 3357; 
matches = new Mongo.Collection("leagueoflegendsMatches");



function getMatch(id) {
    var data = Meteor.http.call("GET", "http://na.lolesports.com:80/api/match/" + id.toString() + ".json");
    var parsedData = JSON.parse(data);

    if (parsedData['ifFinished'] != '0') {
        id_count += 1;
        matches.insert({
            tournament: parsedData['tournament'],
            dateTime: parsedData['dateTime'],
            winnerId: parsedData['winnerId'],
            matchId: parsedData['matchId'],
            maxGames: parsedData['maxGames'],
            blue: parsedData['contestants']['blue'],
            red: parsedData['contestants']['red'],
            liveStreams: parsedData['liveStreams'],
            polldaddyId: parsedData['polldaddyId'],
            games: parsedData['games'],
            name: parsedData['name']
        })
    }
}


    
if (Meteor.isServer) {
   Meteor.setInterval(getMatch(id_count), 60);
}
