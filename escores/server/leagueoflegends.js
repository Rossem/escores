var id_count = 3357; 
matches = new Mongo.Collection("leagueoflegendsMatches");



function getMatch(id) {
    var url = "http://na.lolesports.com:80/api/match/" + id.toString() + ".json"
    var result = Meteor.http.get(url);
    var parsedData = JSON.parse(result.content);

    if (result.statusCode == 200) {
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
}


    
if (Meteor.isServer) {
   Meteor.setInterval(function() {getMatch(id_count);}, 60);
}
